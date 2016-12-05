from configparser import ConfigParser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CONFIG ---------------

config = ConfigParser()

DB_CONFIG_NAME = os.getenv("DB_CONFIG_NAME", "config.conf")

config_path = os.path.join(BASE_DIR + '/conf/', DB_CONFIG_NAME)

config.read(config_path)

# database params --------------------------

DB_ENGINE = config.get('database', 'engine')
DB_NAME = config.get('database', 'name')
DB_USERNAME = config.get('database', 'user')
DB_PASSWORD = config.get('database', 'password')
DB_HOST = config.get('database', 'host')
DB_PORT = config.get('database', 'port')

# END CONFIG -------
