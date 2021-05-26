from pupdb.core import PupDB
from loguru import logger


class Cache:

    def __init__(self):
        self.db = PupDB('db.json')
        logger.debug("database key/value created with success.")

    def set(self, key, value):
        self.db.set(key, value)

    def get(self, key):
        return self.db.get(key)
