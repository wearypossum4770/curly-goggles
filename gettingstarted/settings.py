from os import getenv
from pathlib import Path, PurePath
import django_heroku
from dotenv import load_dotenv
# ~ from config import settings
# ~ BASE_DIR = Path(__file__).resolve('..')
BASE_DIR = Path('/home/gatorcollege2006/web_dev/curly-goggles')
# ~ BASE_DIR = PurePath.parent(PurePath.parent(Path.resolve(__file__)))
load_dotenv(dotenv_path=BASE_DIR / ".env")

# ~ #-----------------------------------------------------------------------
# ~ ## SECURITY SETTINGS
# ~ #-----------------------------------------------------------------------
SECRET_KEY = getenv('DJANGO_SECRET_KEY','abcd1234$#@!') 
DEBUG = getenv('DEBUG',False)
ALLOWED_HOSTS = [
	'127.0.0.1',
	'frozen-beyond-38164.herokuapp',

]
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
PASSWORD_VALIDATOR_PREFIX = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{PASSWORD_VALIDATOR_PREFIX}.UserAttributeSimilarityValidator',},
    {'NAME': f'{PASSWORD_VALIDATOR_PREFIX}.MinimumLengthValidator',    },
    {'NAME': f'{PASSWORD_VALIDATOR_PREFIX}.CommonPasswordValidator',},
    {'NAME': f'{PASSWORD_VALIDATOR_PREFIX}.NumericPasswordValidator',},
]

#-----------------------------------------------------------------------------------------------------------------
# ADMIN SETTINGS
#-----------------------------------------------------------------------------------------------------------------
ADMINS = [
    ('DJANGO DEBUG', 'debug.django@localhost'),
    ]

# ~ #-----------------------------------------------------------------------
# ~ ## APP SETTINGS
# ~ #-----------------------------------------------------------------------
INSTALLED_APPS = [
		"django.contrib.admin",
		"django.contrib.auth",
		"django.contrib.contenttypes",
		"django.contrib.sessions",
		"django.contrib.messages",
		"django.contrib.staticfiles",
		"django.contrib.sites",

	]+[
	'django_extensions',
	'users.apps.UsersConfig',
	'core.apps.CoreConfig',
		# ~ "hello",
		# ~ "cloud.apps.CloudConfig",
		# ~ "chat.apps.ChatConfig",
	]

# ~ #-----------------------------------------------------------------------
# ~ ## SERVER / WEB CONFIG SETTINGS
# ~ #-----------------------------------------------------------------------
ROOT_URLCONF = "gettingstarted.urls"
# FIXTURE_DIRS = []
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'src'],
		"APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
WSGI_APPLICATION = "gettingstarted.wsgi.application"
# ~ ASGI_APPLICATION = "gettingstarted.asgi.application"

# ~ #-----------------------------------------------------------------------
# ~ ## DATABASE / CACHE / STORAGE SETTINGS
# ~ #-----------------------------------------------------------------------
USPS_SHIPPING_API_PASSWORD = getenv('USPS_SHIPPING_API_PASSWORD')
USPS_SHIPPING_API_USERNAME= getenv('USPS_SHIPPING_API_USERNAME')
USPS_SHIPPING_API_COMPANY = getenv('USPS_SHIPPING_API_COMPANY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f"{BASE_DIR}/data/db.sqlite3",
        # ~ 'TEST':{'NAME':f"{BASE_DIR}/data/test_db.sqlite3"},
    }
}
CACHES = {
    'default':{
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1;11211',
    }
}
# ~ #-----------------------------------------------------------------------
# ~ ## INTERNATIONALIZAION SETTINGS
# ~ #-----------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ~ #-----------------------------------------------------------------------
# ~ ## PUSH && EMAIL  NOTIFICATION / DJANGO CHANNELS  SETTINGS
# ~ #-----------------------------------------------------------------------
DEFAULT_FROM_EMAIL:'webmaster@localhost'

# ~ #-----------------------------------------------------------------------
# ~ ## RESTFRAMEWORK  SETTINGS
# ~ #-----------------------------------------------------------------------
SITE_ID = 1
INSTALLED_APPS+=[
		'corsheaders',
	]

# ~ #-----------------------------------------------------------------------
# ~ ## STATIC / CSS / JS / IMG FILE SETTINGS
# ~ #-----------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",]
MEDIA_ROOT=   BASE_DIR / "static" / "media"
MEDIA_URL = '/media/'
# ------ SPECIAL VARIABLES ------ 

# ~ #-----------------------------------------------------------------------
# ~ ## MISC SETTINGS
# ~ #-----------------------------------------------------------------------
DROPBOX_SECRET_API_TOKEN = getenv('DROPBOX_SECRET_API_TOKEN')
DROPBOX_APP_KEY= getenv('DROPBOX_APP_KEY')

# ~ #-----------------------------------------------------------------------
# ~ ## DEPLOY SETTINGS
# ~ #-----------------------------------------------------------------------
HOST_URL = 'http://127.0.0.1:8000' if getenv('DEBUG') else  'https://hudson-sorry-07505.herokuapp.com/'

django_heroku.settings(locals())


