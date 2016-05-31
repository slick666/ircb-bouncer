"""This is the configuration that will be used for hte ircb intance that is created with the docker-compose tool"""
SECRET_KEY = 'some key'

DB_URI = 'postgresql://username:password@postgres/ircb'

SUBSCRIBER_ENDPOINTS = {
    'stores': 'tcp://zeromq:4444',
}

LOGGING_CONF = dict(
    version=1,
    formatters=dict(
        bare={
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "format": "[%(asctime)s][%(name)10s %(levelname)7s] %(message)s"
        },
    ),
    handlers=dict(
        console={
            "class": "logging.StreamHandler",
            "formatter": "bare",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    ),
    loggers=dict(
        ircb={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        network={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        bouncer={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        stores={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        dispatcher={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        irc={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        },
        aiohttp={
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["console"],
        }
    ),
)

INTERNAL_HOST = '127.0.0.1'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# A 32 byte string
WEB_SALT = b'c237202ee55411e584f4cc3d8237ff4b'
