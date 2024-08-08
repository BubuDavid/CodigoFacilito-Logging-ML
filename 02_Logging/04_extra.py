# La verdad es que los logs en el json son muy poco legibles y no podemos analizarlos bien con alguna herramienta externa.
# Vamos a usar formato json en nuestros mismos logs!
# Para esto necesitamos un formatter que transforme el log record en un json.
# Pero esto es super tricky
import json
import logging
import logging.config
import os

logger = logging.getLogger("my_app")  # Common is to use __name__ here

os.makedirs("logs", exist_ok=True)


# Basic logger configuration this goes usually in a separate file config/logging.py
def logger_config():
    config_path = "02_Logging/extra_config.json"
    with open(config_path, "r") as file:
        logging_config = json.load(file)
    logging.config.dictConfig(logging_config)


def main():
    logger_config()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.info("Testing extra", extra={"key": "extra"})
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    try:
        a = 1 / 0
        logger.debug(a)
    except ZeroDivisionError:
        logger.exception("You can't divide by zero")  # ERROR LEVEL

    # Esto ya es lo mejor!


if __name__ == "__main__":
    main()
