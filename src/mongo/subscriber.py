from bson.json_util import dumps
from loguru import logger
from src.cache.cache import Cache


class Subscriber:

    @staticmethod
    def subscribe(mongo_client=None, publisher=None):
        if not mongo_client or not publisher:
            raise Exception("MongoClient and Publisher must be required.")

        cache = Cache()

        resume_token = cache.get("_id")

        start_after = resume_token if resume_token is not None else None

        try:
            with mongo_client.watch(full_document='updateLookup', start_after=start_after) as stream:
                try:
                    for change in stream:
                        cache.set('_id', change['_id'])
                        publisher.publish(dumps(change))
                except Exception as err:
                    logger.error('Error when listen mongodb stream. {}', err)
        except Exception as halt_error:
            logger.error(f"Error iniatilizing stream: {type(halt_error)} > {halt_error} ")
