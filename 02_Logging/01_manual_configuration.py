import logging
import os

logger = logging.getLogger("my_app")  # Common is to use __name__ here

os.makedirs("logs", exist_ok=True)


# Basic logger configuration this goes usually in a separate file config/logging.py
def logger_config():
    logger.setLevel(logging.DEBUG)
    # Create a handler to stdout
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    # Create a handler to a file
    file_handler = logging.FileHandler("logs/manual.log")
    file_handler.setLevel(logging.DEBUG)
    # Create a formatter
    formatter = logging.Formatter(
        "[%(asctime)s|%(name)s|%(levelname)s] - %(message)s"
    )  # Uses weird variables for the formatter
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


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

    # Esto sigue sin ser recomendado, pero es una forma de hacerlo


if __name__ == "__main__":
    main()
