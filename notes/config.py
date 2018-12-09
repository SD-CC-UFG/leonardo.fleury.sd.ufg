import os
import yaml
import logging

log = logging.getLogger(__name__)

config = {
    'AMQP_URI': 'pyamqp://guest:guest@$localhost',
    'DATABASE': 'mongodb+srv://guest:guest@localhost',
    'LOGGING': {
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler'
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['console']
        }
    }
}

try:
    # TODO: Get config path from cli argument
    with open("notes/config.yaml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
        log.debug(config)
except IOError as e:
    print(e)
