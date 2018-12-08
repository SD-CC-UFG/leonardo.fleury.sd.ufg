import yaml
import logging

from auth.auth import Auth

config = {
    'SECRET_KEY': 'secret_key',
    'DATABASE': 'mongodb+srv://guest:guest@localhost'
}

try:
    with open("config.yaml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
except IOError as e:
    logging.info("Configuration file not found. Using default settings.")
    logging.error(e)

logging.config.dictConfig(config.LOGGING)
log = logging.getLogger(__name__)

log.debug("{}".format(config))
