"""
Django settings for integrated_side_project project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import json
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

secret_file_path = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file_path) as f:
    SECRETES: dict = json.loads(f.read())

if not SECRETES:
    raise ValueError('참조할 환경변수 파일이 없습니다.')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETES.get('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("there's no available secret key.")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 메인호스트 URL
MAIN_HOST = 'localhost'

# 허용된 호스트 목록
ALLOWED_HOSTS = [
    MAIN_HOST,
    '127.0.0.1',
]

# 디버그툴바용 내부 IP 목록
INTERNAL_IPS = ('127.0.0.1',)

# Application definition

# Django 전용 앱
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# 외부 써드파티 라이브러리
THIRD_PARTY_APPS = [
    'channels',
    'channels_redis',
    'rest_framework',
    'django_json_widget',
    'flat_json_widget',
    'drf_yasg',
    'rangefilter',
    'storages',
]

# 디버그 모드인 경우
# 디버그 툴바 활성화
if DEBUG:
    THIRD_PARTY_APPS += [
        'debug_toolbar',
    ]

LOCAL_APPS = [
    'account',
    'core',
    'chat',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# 관리자 대상 모델
AUTH_USER_MODEL = 'account.AdministrationUser'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 디버그모드일 경우
# 디버그 툴바 미들웨어 추가
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = "integrated_side_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "integrated_side_project.wsgi.application"
ASGI_APPLICATION = "integrated_side_project.asgi.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('localhost', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DB 트리거에 따라
# 참조 환경변수를 바꾸자.
# postgresql이 설치된 컴퓨터에서
# 서버를 구동하는 경우에는 LOCAL_DATABASE로 변경
LOCAL_DATABASE = True
if LOCAL_DATABASE:
    DATABASES = SECRETES['LOCAL_DATABASES']
else:
    DATABASES = SECRETES['EXTERNAL_DATABASES']

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATA_UPLOAD_MAX_MEMORY_SIZE = 20 * 1024 * 1024

LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# swagger 세팅
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic',
        }
    },
}
# SWAGGER_DEFAULTS에 LOGOUT_URL은 라이브러리단에서
# LOGOUT_URL을 제대로 참조하도록 구현하지 않았다.
# 아래처럼 되어있음.
# 'LOGIN_URL': getattr(settings, 'LOGIN_URL', None),
# 'LOGOUT_URL': '/accounts/logout/',
# 때문에 직접 임포트하여 settings에서 LOGOUT_URL을 똑같이 적용시켜줄 필요가있다.
# settings에서 세팅한 값이 최종값이됨.
from drf_yasg.app_settings import swagger_settings

swagger_settings.defaults['LOGIN_URL'] = LOGIN_URL
swagger_settings.defaults['LOGOUT_URL'] = LOGOUT_URL
