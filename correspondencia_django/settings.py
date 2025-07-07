import os
from pathlib import Path

# —————————— Ajusta según tu proyecto ——————————
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'tu-secret-key-aquí'
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'correspondencia_app',
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

# ————— Módulo raíz de tu proyecto —————
ROOT_URLCONF = 'correspondencia_django.urls'
WSGI_APPLICATION = 'correspondencia_django.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 importante: indica la ruta
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

# ————— Base de datos —————
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ————— Validación de contraseñas —————
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    # otros validadores…
]

# ————— Internacionalización —————
LANGUAGE_CODE = 'es-pan'
TIME_ZONE = 'America/Panama'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ————— Archivos estáticos —————
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
STATIC_ROOT = BASE_DIR /'correspondencia_app''staticfiles'


# ————— Media (subida de archivos) —————
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ————— Rutas de autenticación —————
# Redirección después de login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

