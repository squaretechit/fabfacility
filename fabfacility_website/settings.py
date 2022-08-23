from pathlib import Path
from env import EnvConfig


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6w#j4^)f7qf-=d3npafrlw3-4zt)(#&50^nnj9ybd-0wrxpaxz'

DEBUG = EnvConfig.DEBUG

ALLOWED_HOSTS = EnvConfig.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    # Admin
    'admin_interface',
    'colorfield',
    # Defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Sitemaps
    'django.contrib.sitemaps',
    # My Apps
    'fabfacility_website_theme',
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

ROOT_URLCONF = 'fabfacility_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # My Context
                'fabfacility_website_theme.context_processors.theme_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'fabfacility_website.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = BASE_DIR, 'static'
# STATIC_ROOT = 'here will be the path for production'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
# MEDIA_ROOT = 'here will be the path for production'


# EMAIL Configurations
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = EnvConfig.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EnvConfig.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Admin Layout

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]
