from pathlib import Path
from datetime import timedelta
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-s#ohlpe%^gzey+qj=2(3h1mkf-xh!f&05w2_8(8r7#zilv3+c5'

DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Add the following apps:
    'users',        # User management
    'auction_items',# Auction items
    'bids',         # Bidding system
    'payments',     # Payment integration
    'notifications',# Notification system
    'logs',         # Activity logging
    'files',        # File uploads
    'categories',   # Auction item categories
    'admins',
    'transactions',        
    'rest_framework',  # Django REST framework
    'rest_framework_simplejwt',  # SimpleJWT for authentication
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'django_celery_results',  # To store results of Celery tasks
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AuctionPlatform.urls'

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

WSGI_APPLICATION = 'AuctionPlatform.wsgi.application'

# Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'onlineauctiondb',
        'USER': 'onlineauctionuser',
        'PASSWORD': 'securepassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



AUTH_USER_MODEL = 'users.User'

# settings.py for REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # Use JWT as primary authentication
        'rest_framework.authentication.SessionAuthentication',         # Fallback to session-based authentication
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Token expires in 5 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Refresh token expires in 1 day
    'ROTATE_REFRESH_TOKENS': True,                    # Rotate refresh tokens on every refresh request
    'BLACKLIST_AFTER_ROTATION': True,                  # Blacklist old refresh tokens
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'TOKEN_OBTAIN_SERIALIZER' : 'user.serializers.CustomClaimTokenObtainSerializer',
}

# Email Settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config('EMAIL_HOST', default='localhost')
# EMAIL_PORT = config('EMAIL_PORT', cast=int, default=25)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
# EMAIL_USE_SSL = config('EMAIL_USE_SSL', cast=bool, default=False)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'onlineauctionp@gmail.com'
EMAIL_HOST_PASSWORD = 'brfuntzxcusexdyg'  # App-specific password

#reis cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Redis server URL
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'books',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  
SESSION_CACHE_ALIAS = 'default'


# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as broker
CELERY_RESULT_BACKEND = 'django-db'  # Store results in Django database
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Password validation
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add other configurations if necessary
#Mahabub
# bossking1888f@gmail.com
# incorrect2

