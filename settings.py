import os.path
import sys


# Getting Started
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications'))

# Debug Settings
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Basic Settings
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

# Cache Settings
if DEBUG:
    CACHE_BACKEND = "dummy:///"
else:
    CACHE_BACKEND = "memcached://208.78.98.196:11211/"
    CACHE_MIDDLEWARE_SECONDS = 60 * 60
    CACHE_MIDDLEWARE_KEY_PREFIX = 'aliter'

# Site Settings
SITE_ID = 1
ROOT_URLCONF = 'urls'
USE_I18N = True

# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'complaints.notifications.Notification',
)
USE_ETAGS = True
APPEND_SLASH = True
REMOVE_WWW = True

# Template Settings
MARKUP_FILTER = ('markdown', {})
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'complaints.notifications.notifications',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

# Secret Key Generator
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)
        
    

# Tagging (django-tagging)
FORCE_LOWERCASE_TAGS = True

# Import Local Settings
try:
    from locals import *
except ImportError:
    pass
