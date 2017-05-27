"""Common settings and globals."""
from __future__ import absolute_import

from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import normpath
from os import environ

from sys import path

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(key):
    """
    Get the environment setting or return exception,
    if default is not set

    :param key:
    """
    try:
        return environ[key]
    except KeyError:
        error_msg = 'Set the {0} env variable'.format(key)
        raise ImproperlyConfigured(error_msg)


# ######### PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(abspath(__file__))

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site sub-module name:
SITE_MODULE = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
# ######### END PATH CONFIGURATION


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# ######### END DEBUG CONFIGURATION


# ######### TEST RUNNER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/releases/dev/#new-test-runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
# ######### END TEST RUNNER CONFIGURATION


# ######### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = (
)
# ######### END MANAGER CONFIGURATION


# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# ######### END DATABASE CONFIGURATION


# ######### ATOMICITY CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-DATABASE-ATOMIC_REQUESTS
ATOMIC_REQUESTS = True
# ######### END ATOMICITY CONFIGURATION


# ######### GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#datetime-format
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#date-format
DATE_FORMAT = 'N j, Y'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-format
TIME_FORMAT = 'P'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

LOCALE_PATHS = (
    join(SITE_ROOT, 'locale'),
)
# ######### END GENERAL CONFIGURATION


# ######### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# ######### END MEDIA CONFIGURATION


# ######### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
# ######### END STATIC FILE CONFIGURATION


# ######### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = r"ugdn_k*$*g3b_g3x$hf4mxm#l$h*si9&u-@5aokaumjz=#x5g7"
# ######### END SECRET CONFIGURATION


# ######### SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
# ######### END SITE CONFIGURATION


# ######### FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)
# ######### END FIXTURE CONFIGURATION


# ######### TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
            ]
        }
    }
]
# ######### END TEMPLATE CONFIGURATION


# ######### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-MIDDLEWARE
MIDDLEWARE = [
    # Default Django middleware.
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'reversion.middleware.RevisionMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware'
]
# ######### END MIDDLEWARE CONFIGURATION


# ######### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '{0}.urls'.format(SITE_MODULE)
# ######### END URL CONFIGURATION


# ######### APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin'
    # Useful template tags:
    # 'django.contrib.humanize'
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework_swagger',
)

# Apps specific for this project go here.
LOCAL_APPS = (

)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# ######### END APP CONFIGURATION


# ######### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '{0}.wsgi.application'.format(SITE_MODULE)
# ######### END WSGI CONFIGURATION


# ######### PASSWORD VALIDATION CONFIGURATION
# See: https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#password-validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,
        }
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
# ######### END PASSWORD VALIDATION CONFIGURATION


# ######### PASSWORD HASHER CONFIGURATION
# See: https://docs.djangoproject.com/en/1.10/topics/auth/passwords/#password-validation
# Argon2 is the winner of the 2015 Password Hashing Competition,
# a community organized open competition to select a next generation hashing algorithm.
# It's designed not to be easier to compute on custom hardware than it is to compute on an ordinary CPU.
# Argon2 is not the default for Django because it requires a third-party library.
# The Password Hashing Competition panel, however, recommends immediate use of Argon2 rather
# than the other algorithms supported by Django.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher'
]
# ######### END PASSWORD HASHER CONFIGURATION


# ######### DJANGO REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.CoreJSONRenderer',

        'rest_framework_swagger.renderers.OpenAPIRenderer',
        'rest_framework_swagger.renderers.SwaggerUIRenderer',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}
# ######### END DJANGO REST FRAMEWORK CONFIGURATION
