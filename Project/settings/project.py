import os
from pathlib import Path

import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = "+j407t_$m*$hgr)yd5t&^fae3cot!*^+9@hwh+t9i^sw2$rlo0"

DEBUG = True

ALLOWED_HOSTS = ["tjg.herokuapp.com/", "127.0.0.1", "localhost"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Ecommerce_Store",
    "cart",
    "django_countries",
    "account",
    "payment",
    "orders",
    "mptt",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "Ecommerce_Store.context_processors.categories",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "Project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Cart session ID
CART_SESSION_ID = "cart"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Customized user model
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

# activation email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe Payment
os.environ.setdefault(
    "STRIPE_PUBLISHABLE_KEY",
    "",
)
STRIPE_SECRET_KEY = ""
STRIPE_ENDPOINT_SECRET = ""

# Stripe listen --forward-to localhost:8000/payment/webhook/
# Activate Django-Heroku.
django_heroku.settings(locals())
