import json
import logging
import logging.config


def configure_logger():
    path: str = "03_FastAPI/config.json"
    with open(path, "r") as file:
        dict_config = json.load(file)

    logging.config.dictConfig(dict_config)


logger = logging.getLogger("my_logger")
configure_logger()

