"""Settings that need to be set in order to run the tests."""
import os


PROJECT_ROOT = os.path.dirname(__file__)

DEBUG = True
USE_TZ = True
SITE_ID = 1

FROM_EMAIL = "info@example.com"
DEFAULT_FROM_EMAIL = FROM_EMAIL
SERVER_EMAIL = FROM_EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = 'frequently.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../media/')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'test_app/templates'),
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')
COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_jasmine',
    'django_nose',
]

INTERNAL_APPS = [
    'frequently',
    'frequently.tests.test_app',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
