import os
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY', default='dev-secret')
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
    'employees',
    'attendance',
]

DATABASES = {
    'default': env.db('DATABASE_URL')
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}
