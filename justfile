open_cmd := if os() == "linux" { "xdg-open" } else { "open" }
project_url := "http://localhost:8000"
project_name := `basename $(dirname $(realpath $0))`
gitignore_file := ".gitignore"
gitignore_contents := "*.pyc\n.venv\ndb.sqlite3\n.env\n/media\n/static"
req_file := "requirements.txt"
req_contents := "django"

alias mm := mmigrate
alias sh := shell
alias doc := djangodoc
alias run := runserver

csv:
    python manage.py import_competitors competitor/competitors.csv
    python manage.py import_teachers teacher/profesores.csv
    python manage.py import_judges judge/jueces.csv 
# Run development server
runserver: database redis
    python manage.py runserver

# Make a Python virtualenv
mkvenv: mkignore mkreq
    python -m venv .venv --prompt {{ project_name }}

# Run development server on all interfaces at port 80
runserver0: database redis
    python manage.py runserver 0.0.0.0:80

# Check whole project
check:
    python manage.py check

# Open project in web browser
open:
    {{ open_cmd }} {{ project_url }}

# Open python shell with django settings
shell: database
    python manage.py shell

# Clean all precompiled python files
clean:
    #!/usr/bin/env bash
    find . -name '__pycache__' -not -path "./.venv/*" -prune -exec rm -rf {} \;
    find . -name '*.pyc' -not -path "./.venv/*" -exec rm {} \;
    find . -name '.DS_Store' -not -path "./.venv/*" -exec rm {} \;
    rm -rf .mypy_cache

# Create database migrations for single app or whole project
makemigrations app="": database
    python manage.py makemigrations {{ app }}

# Run pending migrations for single app or whole project
migrate app="": database
    python manage.py migrate {{ app }}

# Run both makemigrations & migrate commands
mmigrate app="": database
    python manage.py makemigrations {{ app }} && python manage.py migrate {{ app }}

# Show database migrations for single app or whole project
showmigrations app="": database
    python manage.py showmigrations {{ app }}

# Create a new app (also adding it to INSTALLED_APPS)
startapp app:
    #!/usr/bin/env bash
    python manage.py startapp {{ app }}
    APP_CLASS={{ app }}
    APP_CONFIG="{{ app }}.apps.${APP_CLASS^}Config"
    perl -0pi -e "s/(INSTALLED_APPS *= *\[)(.*?)(\])/\1\2    '$APP_CONFIG',\n\3/smg" $(find . -name settings.py)

# Delete an existing app
deleteapp app:
    #!/usr/bin/env bash
    read -p 'Do you wish to delete "{{ app }}" app? ' -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        rm -fr {{ app }}
    fi

# Show SQL behind a migration for a single app
sql app migration_id:
    python manage.py sqlmigrate {{ app }} {{ migration_id }}

# Create superuser for django admin
su: database
    python manage.py createsuperuser

# Dump database data in json format
dumpdata app="" output=(project_name + ".json"): database
    python manage.py dumpdata {{ app }} --indent=2 --output={{ output }}

# Load database data from json format
loaddata input: database
    python manage.py loaddata {{ input }}

# Open debug python shell with django settings
dshell:
    python manage.py debugsqlshell

# Copy static assets to STATIC_ROOT
collectstatic:
    python manage.py collectstatic

# Open Django documentation for query
djangodoc query: check_venv
    #!/usr/bin/env bash
    DJANGO_VERSION=$(python -m django --version)
    DJANGO_MAJOR_VERSION=$(echo $DJANGO_VERSION | perl -ne 's/(\d.\d).*/\1/; print')
    QUERY_URL="https://docs.djangoproject.com/en/${DJANGO_MAJOR_VERSION}/search/?q={{ query }}"
    {{ open_cmd }} $QUERY_URL

# Create a zip file with the whole project
zip: clean
    #!/usr/bin/env bash
    rm -f {{ project_name }}.zip
    zip -r {{ project_name }}.zip . -x .env .venv/**\* .git/**\*

# Install Python requirements
pipi: check_venv
    python -m pip install -r requirements.txt

# Launch project through Docker
dockup:
    docker compose up

# Check if virtualenv is active
[private]
check_venv:
    #!/usr/bin/env bash
    if [ -z $VIRTUAL_ENV ] && [[ $(pyenv version-name) =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo You must activate a virtualenv!
        exit 1
    fi

# Make a .gitignore file
[private]
mkignore:
    [ -f "{{ gitignore_file }}" ] || echo '{{ gitignore_contents }}' > {{ gitignore_file }}

# Make a requirements.txt file
[private]
mkreq:
    [ -f "{{ req_file }}" ] || echo '{{ req_contents }}' > {{ req_file }}

# Start database server
[private]
database:
    #!/usr/bin/env bash
    if [[ $(grep -i postgres $(find . -name settings.py)) ]]; then
        if   [[ $OSTYPE == "linux-gnu"* ]]; then
            sudo service postgresql status &> /dev/null || sudo service postgresql start
        elif [[ $OSTYPE == "darwin"* ]]; then
            pgrep -x postgres || open /Applications/Postgres.app
        fi
    fi

# Memcached service
[private]
memcached:
    #!/usr/bin/env bash
    if   [[ $OSTYPE == "linux-gnu"* ]]; then
        sudo service memcached status &> /dev/null || sudo service memcached start
    elif [[ $OSTYPE == "darwin"* ]]; then
        pgrep -x memcached || brew services start memcached
    fi

# Start redis server
[private]
redis:
    #!/usr/bin/env bash
    if   [[ $OSTYPE == "linux-gnu"* ]]; then
        sudo service redis status &> /dev/null || sudo service redis start
    elif [[ $OSTYPE == "darwin"* ]]; then
        pgrep -x redis || open /Applications/Redis.app
    fi