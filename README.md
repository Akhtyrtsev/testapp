This project uses sqlite backend, so no need in additional configuration
In order to run the project extract it, create virtual environment and install requirements.
After these operations move to app directory and run command: ./manage.py runserver
In order to run project with real db, you should create the last and configure it in settings.py
Here is postgres example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': postgres,
        'USER': postgres,
        'PASSWORD': postgres,
    }
}
