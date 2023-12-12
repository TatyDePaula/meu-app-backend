from logging.config import dictConfig
import logging
import os

log_path = "log/"
# Verifica se o diretorio para armexanar os logs não existe
if not os.path.exists(log_path):
   # então cria o diretorio
   os.makedirs(log_path)

dictConfig({
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)-4s %(funcName)s() L%(lineno)-4d %(message)s",
        },
        "detailed": {
            "format": "[%(asctime)s] %(levelname)-4s %(funcName)s() L%(lineno)-4d %(message)s - call_trace=%(pathname)s L%(lineno)-4d",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": "log/error.log",
            "maxBytes": 10000,
            "backupCount": 10,
            "delay": "True",
        },
        "info_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "log/info.log",
            "maxBytes": 10000,
            "backupCount": 10,
            "delay": "True",
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console", "error_file", "info_file"],
            "level": "INFO",
            "propagate": False,
        }
    },
    "root": {
        "handlers": ["console", "error_file", "info_file"],
        "level": "INFO",
    }
})

logger = logging.getLogger("app")