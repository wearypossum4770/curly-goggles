import os
from pathlib import Path

#--------------------------------------------------------------------------------
# DJANGO BASE  SETTINGS
#--------------------------------------------------------------------------------
BASE_DIR = Path.cwd()
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
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

#--------------------------------------------------------------------------------
# SECURITY SETTINGS
#--------------------------------------------------------------------------------
SECRET_KEY = 'cxy(3qhp_)bop!h3g3qe+5*&wox&(&kft687yz-@rzyp(dzu+t'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

#--------------------------------------------------------------------------------
# APPS
#--------------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#--------------------------------------------------------------------------------
# POSTMAN SETTINGS
#--------------------------------------------------------------------------------
# ~ INSTALLED_APPS += ['pagination', 'postman',]
# POSTMAN_I18N_URLS = True  # default is False
POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
# POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
# POSTMAN_DISABLE_USER_EMAILING = True  # default is False
# POSTMAN_FROM_EMAIL = 'from@host.tld'  # default is DEFAULT_FROM_EMAIL
# POSTMAN_PARAMS_EMAIL = get_params_email  # default is None
# POSTMAN_AUTO_MODERATE_AS = True  # default is None
POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
# POSTMAN_NAME_USER_AS = 'last_name'  # default is None
# POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
# POSTMAN_NOTIFIER_APP = None  # default is 'notification'
# POSTMAN_MAILER_APP = None  # default is 'mailer'
# POSTMAN_AUTOCOMPLETER_APP = {
    # 'name': '',  # default is 'ajax_select'
    # 'field': '',  # default is 'AutoCompleteField'
    # 'arg_name': '',  # default is 'channel'
    # 'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
# }  # default is {}

#--------------------------------------------------------------------------------
# DATABASE / CACHE SETTINGS
#--------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f'{BASE_DIR}/data/db.sqlite3',
    }
}

#--------------------------------------------------------------------------------
#  TEMPLATES / FRONTEND
#--------------------------------------------------------------------------------
ROOT_URLCONF = 'my_project.urls'
WSGI_APPLICATION = 'my_project.wsgi.application'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'{BASE_DIR}/templates',],
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

#--------------------------------------------------------------------------------
# INTERNATIONALIZATION SETTINGS
#--------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#--------------------------------------------------------------------------------
# STATIC SETTINGS
#--------------------------------------------------------------------------------
STATIC_URL = '/static/'

#--------------------------------------------------------------------------------
# RESTFRAMEWORK SETTINGS
#--------------------------------------------------------------------------------


#--------------------------------------------------------------------------------
# 
#--------------------------------------------------------------------------------


