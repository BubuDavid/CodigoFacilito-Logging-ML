import logging

logger = logging.getLogger("my_app")  # Common is to use __name__ here


def main():
    logging.basicConfig(level=logging.DEBUG)  # Set the logging level
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    try:
        a = 1 / 0
        logger.debug(a)
    except ZeroDivisionError:
        logger.exception("You can't divide by zero")

    # Esto sigue siendo feo y no es recomendable porque no es robusto


if __name__ == "__main__":
    main()
