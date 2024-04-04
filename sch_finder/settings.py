"""
Django settings for sch_finder project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# JWT secret for token signing
JWT_SECRET = os.environ.get('JWT_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# List of allowed hostnames for the production environment
ALLOWED_HOSTS = ["uniguide-7lk7.onrender.com", "127.0.0.1", "localhost"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin
    'django.contrib.auth',  # Authentication system
    'django.contrib.contenttypes',  # Content types
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Messages framework
    'django.contrib.staticfiles',  # Static file serving
    'rest_framework',  # Django Rest Framework
    'sch_finder_api',  # Your app
    'django_rest_passwordreset',  # Password reset functionality
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Messages middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

ROOT_URLCONF = 'sch_finder.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sch_finder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Define the database URL for the production environment
DATABASE_URL = "postgres://godwin:4D0XTvwA00Ch7vYaRr06fMU7WVUk24yq@dpg-co2n7e8l6cac73br5g5g-a.oregon-postgres.render.com/unifinder"

# Parse the database URL and configure the database settings
DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL)
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Static root directory for serving static files in production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Static file storage using Whitenoise for compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model for authentication
AUTH_USER_MODEL = "sch_finder_api.User"

# Allow CORS for all origins
CORS_ORIGIN_ALLOW_ALL = True

# Allow credentials to be included in CORS requests
CORS_ALLOW_CREDENTIALS = True

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'okpegodwinfather@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # This should be stored securely and not hardcoded
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'okpegodwinfather@gmail.com'

