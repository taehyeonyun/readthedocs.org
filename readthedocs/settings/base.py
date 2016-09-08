# encoding: utf-8
# pylint: disable=missing-docstring

import os

import djcelery

from readthedocs.core.settings import Settings


djcelery.setup_loader()

_ = gettext = lambda s: s


class CommunityBaseSettings(Settings):

    """Community base settings, don't use this directly"""

    # Django settings
    SITE_ID = 1
    ROOT_URLCONF = 'readthedocs.urls'
    SUBDOMAIN_URLCONF = 'readthedocs.core.urls.subdomain'
    LOGIN_REDIRECT_URL = '/dashboard/'
    FORCE_WWW = False
    SECRET_KEY = 'replace-this-please'  # noqa
    ATOMIC_REQUESTS = True

    # Debug settings
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    TASTYPIE_FULL_DEBUG = True
    LOG_DEBUG = False

    # Domains and URLs
    PRODUCTION_DOMAIN = 'readthedocs.org'
    PUBLIC_DOMAIN = None
    USE_SUBDOMAIN = False
    PUBLIC_API_URL = 'https://{0}'.format(PRODUCTION_DOMAIN)

    ADMINS = (
        ('Eric Holscher', 'eric@readthedocs.org'),
        ('Anthony Johnson', 'anthony@readthedocs.org'),
    )
    MANAGERS = ADMINS

    # Email
    DEFAULT_FROM_EMAIL = "no-reply@readthedocs.org"
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

    # Cookies
    SESSION_COOKIE_DOMAIN = 'readthedocs.org'
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True

    # Application classes
    @property
    def INSTALLED_APPS(self):  # noqa
        apps = [
            'django.contrib.auth',
            'django.contrib.admin',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.staticfiles',
            'django.contrib.messages',
            'django.contrib.humanize',

            # third party apps
            'pagination',
            'taggit',
            'djangosecure',
            'guardian',
            'django_gravatar',
            'rest_framework',
            'corsheaders',
            'copyright',
            'textclassifier',
            'annoying',
            'django_countries',
            'django_extensions',
            'messages_extends',

            # Celery bits
            'djcelery',

            # daniellindsleyrocksdahouse
            'haystack',
            'tastypie',

            # our apps
            'readthedocs.bookmarks',
            'readthedocs.projects',
            'readthedocs.builds',
            'readthedocs.comments',
            'readthedocs.core',
            'readthedocs.doc_builder',
            'readthedocs.oauth',
            'readthedocs.redirects',
            'readthedocs.rtd_tests',
            'readthedocs.restapi',
            'readthedocs.privacy',
            'readthedocs.gold',
            'readthedocs.donate',
            'readthedocs.payments',
            'readthedocs.notifications',

            # allauth
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'allauth.socialaccount.providers.github',
            'allauth.socialaccount.providers.bitbucket',
            'allauth.socialaccount.providers.bitbucket_oauth2',
        ]
        return apps

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    MIDDLEWARE_CLASSES = (
        'readthedocs.core.middleware.ProxyMiddleware',
        'readthedocs.core.middleware.FooterNoSessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
        'djangosecure.middleware.SecurityMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'pagination.middleware.PaginationMiddleware',
        'readthedocs.core.middleware.SubdomainMiddleware',
        'readthedocs.core.middleware.SingleVersionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
    )

    AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of `allauth`
        "django.contrib.auth.backends.ModelBackend",
        # `allauth` specific authentication methods, such as login by e-mail
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        # Read the Docs processor
        "readthedocs.core.context_processors.readthedocs_processor",
    )

    MESSAGE_STORAGE = 'readthedocs.notifications.storages.FallbackUniqueStorage'

    # Paths
    SITE_ROOT = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    TEMPLATE_ROOT = os.path.join(SITE_ROOT, 'readthedocs', 'templates')
    DOCROOT = os.path.join(SITE_ROOT, 'user_builds')
    UPLOAD_ROOT = os.path.join(SITE_ROOT, 'user_uploads')
    CNAME_ROOT = os.path.join(SITE_ROOT, 'cnames')
    LOGS_ROOT = os.path.join(SITE_ROOT, 'logs')
    PRODUCTION_ROOT = os.path.join(SITE_ROOT, 'prod_artifacts')
    PRODUCTION_MEDIA_ARTIFACTS = os.path.join(PRODUCTION_ROOT, 'media')

    # Assets and media
    STATIC_ROOT = os.path.join(SITE_ROOT, 'media/static/')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
    MEDIA_URL = '/media/'
    ADMIN_MEDIA_PREFIX = '/media/admin/'
    STATICFILES_DIRS = [os.path.join(SITE_ROOT, 'readthedocs', 'static')]
    TEMPLATE_DIRS = (
        TEMPLATE_ROOT,
    )

    # Cache
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'PREFIX': 'docs',
        }
    }
    CACHE_MIDDLEWARE_SECONDS = 60

    # I18n
    TIME_ZONE = 'America/Chicago'
    LANGUAGE_CODE = 'en-us'
    LANGUAGES = (
        ('en', gettext('English')),
        ('es', gettext('Spanish')),
        ('nb', gettext('Norwegian Bokmål')),
        ('fr', gettext('French')),
        ('ru', gettext('Russian')),
        ('de', gettext('German')),
        ('gl', gettext('Galician')),
        ('vi', gettext('Vietnamese')),
        ('zh-cn', gettext('Chinese')),
        ('zh-tw', gettext('Taiwanese')),
        ('ja', gettext('Japanese')),
        ('uk', gettext('Ukrainian')),
        ('it', gettext('Italian')),
    )
    LOCALE_PATHS = [
        os.path.join(SITE_ROOT, 'readthedocs', 'locale'),
    ]
    USE_I18N = True
    USE_L10N = True

    # Celery
    CELERY_ALWAYS_EAGER = True
    CELERYD_TASK_TIME_LIMIT = 60 * 60  # 60 minutes
    CELERY_SEND_TASK_ERROR_EMAILS = False
    CELERYD_HIJACK_ROOT_LOGGER = False
    # Don't queue a bunch of tasks in the workers
    CELERYD_PREFETCH_MULTIPLIER = 1
    CELERY_CREATE_MISSING_QUEUES = True

    CELERY_DEFAULT_QUEUE = 'celery'
    # Wildcards not supported: https://github.com/celery/celery/issues/150
    CELERY_ROUTES = {
        'readthedocs.oauth.tasks.SyncBitBucketRepositories': {
            'queue': 'web',
        },
        'readthedocs.oauth.tasks.SyncGitHubRepositories': {
            'queue': 'web',
        },
    }

    # Docker
    DOCKER_ENABLE = False
    DOCKER_IMAGE = 'readthedocs/build:14.04'

    # All auth
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ACCOUNT_AUTHENTICATION_METHOD = "username_email"
    ACCOUNT_ACTIVATION_DAYS = 7
    SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
    SOCIALACCOUNT_AUTO_SIGNUP = False
    SOCIALACCOUNT_PROVIDERS = {
        'github': {
            'SCOPE': ['user:email', 'read:org', 'admin:repo_hook', 'repo:status']
        }
    }

    # CORS
    CORS_ORIGIN_REGEX_WHITELIST = (
        '^http://(.+)\.readthedocs\.io$',
        '^https://(.+)\.readthedocs\.io$'
    )
    # So people can post to their accounts
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = (
        'x-requested-with',
        'content-type',
        'accept',
        'origin',
        'authorization',
        'x-csrftoken'
    )

    # RTD Settings
    REPO_LOCK_SECONDS = 30
    ALLOW_PRIVATE_REPOS = False
    GROK_API_HOST = 'https://api.grokthedocs.com'
    SERVE_DOCS = ['public']

    # Haystack
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        },
    }

    # Elasticsearch settings.
    ES_HOSTS = ['127.0.0.1:9200']
    ES_DEFAULT_NUM_REPLICAS = 0
    ES_DEFAULT_NUM_SHARDS = 5

    ALLOWED_HOSTS = ['*']

    ABSOLUTE_URL_OVERRIDES = {
        'auth.user': lambda o: "/profiles/%s/" % o.username
    }

    INTERNAL_IPS = ('127.0.0.1',)

    # Guardian Settings
    GUARDIAN_RAISE_403 = True
    ANONYMOUS_USER_ID = -1

    # Stripe
    STRIPE_SECRET = None
    STRIPE_PUBLISHABLE = None

    # Misc application settings
    GLOBAL_ANALYTICS_CODE = 'UA-17997319-1'
    GRAVATAR_DEFAULT_IMAGE = 'http://media.readthedocs.org/images/silhouette.png'
    COPY_START_YEAR = 2010
    RESTRICTEDSESSIONS_AUTHED_ONLY = True
    RESTRUCTUREDTEXT_FILTER_SETTINGS = {
        'cloak_email_addresses': True,
        'file_insertion_enabled': False,
        'raw_enabled': False,
        'strip_comments': True,
        'doctitle_xform': True,
        'sectsubtitle_xform': True,
        'initial_header_level': 2,
        'report_level': 5,
        'syntax_highlight': 'none',
        'math_output': 'latex',
        'field_name_limit': 50,
    }
    REST_FRAMEWORK = {
        'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
        'PAGINATE_BY': 10
    }
    SILENCED_SYSTEM_CHECKS = ['fields.W342']

    # Logging
    LOG_FORMAT = "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s"
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': LOG_FORMAT,
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'exceptionlog': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "exceptions.log"),
                'formatter': 'standard',
            },
            'errorlog': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "rtd.log"),
                'formatter': 'standard',
            },
            'postcommit': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "postcommit.log"),
                'formatter': 'standard',
            },
            'middleware': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "middleware.log"),
                'formatter': 'standard',
            },
            'restapi': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "api.log"),
                'formatter': 'standard',
            },
            'db': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "db.log"),
                'formatter': 'standard',
            },
            'search': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGS_ROOT, "search.log"),
                'formatter': 'standard',
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler',
            },
            'console': {
                'level': ('INFO', 'DEBUG')[DEBUG],
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'errorlog'],
                'propagate': True,
                'level': 'WARN',
            },
            'django.db.backends': {
                'handlers': ['db'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'readthedocs.core.views.post_commit': {
                'handlers': ['postcommit'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'core.middleware': {
                'handlers': ['middleware'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'restapi': {
                'handlers': ['restapi'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['exceptionlog'],
                'level': 'ERROR',
                'propagate': False,
            },
            'readthedocs.projects.views.public.search': {
                'handlers': ['search'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'search': {
                'handlers': ['search'],
                'level': 'DEBUG',
                'propagate': False,
            },
            # Uncomment if you want to see Elasticsearch queries in the console.
            # 'elasticsearch.trace': {
            #     'level': 'DEBUG',
            #     'handlers': ['console'],
            # },

            # Default handler for everything that we're doing. Hopefully this
            # doesn't double-print the Django things as well. Not 100% sure how
            # logging works :)
            '': {
                'handlers': ['console', 'errorlog'],
                'level': 'INFO',
            },
        }
    }
