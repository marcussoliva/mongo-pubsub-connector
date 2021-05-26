from pymongo import MongoClient
from src.pubsub.publisher import Publisher
from src.environment.environment import MongoEnvironment, GoogleCloudEnvironment
from loguru import logger
from src.mongo.subscriber import Subscriber

mongo_uri = MongoEnvironment.get_mongodb_uri()
topic_name = GoogleCloudEnvironment.get_topic_name()
project_id = GoogleCloudEnvironment.get_project_id()
logger.info('Application configs done.')

mongo_client = MongoClient(mongo_uri)
logger.info('Mongo client created and connected.')

publisher = Publisher(topic_name, project_id)
logger.info('Publisher created with success.')

logger.info('Subscribe attached on mongo stream.')
Subscriber.subscribe(mongo_client, publisher)
