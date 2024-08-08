import logging
import logging.config  # Por alguna razon esto esta en otro modulo...
import os

logger = logging.getLogger("my_app")  # Common is to use __name__ here

os.makedirs("logs", exist_ok=True)

# siiii un diccionario
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # This is important
    "formatters": {
        "simple": {
            "format": "[%(levelname)s|%(module)s|%(lineno)d] %(asctime)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S%z",  # Use iso8601 and include timezone
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",  # Si usas los handlers por defecto tienes que usar "class"
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stdout",  # This is the default value for stream to stdout
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",  # Handler para un archivo que rota. (Por alguna razon esta escondido tambien)
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "logs/dict.log",
            "maxBytes": 2048,  # Escribe 2KB y el backup (Rota)
            "backupCount": 3,  # Guarda 3 archivos de backup
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        }
    },
}


# Basic logger configuration this goes usually in a separate file config/logging.py
def logger_config():
    logging.config.dictConfig(LOGGING_CONFIG)


def main():
    logger_config()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    try:
        a = 1 / 0
        logger.debug(a)
    except ZeroDivisionError:
        logger.exception("You can't divide by zero")  # ERROR LEVEL

    # Ya casi llegamos a lo optimo.


if __name__ == "__main__":
    main()
