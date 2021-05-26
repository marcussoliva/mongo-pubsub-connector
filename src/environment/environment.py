import os


class MongoEnvironment:
    """
     Returns mongodb uri
    """

    @staticmethod
    def get_mongodb_uri() -> str:
        if "MONGO_URI" not in os.environ:
            raise Exception('MONGO_URI must be declared in your environment.')

        return os.environ['MONGO_URI']


class GoogleCloudEnvironment:

    @staticmethod
    def get_credentials() -> str:
        if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
            raise Exception('GOOGLE_APPLICATION_CREDENTIALS must be declared in your environment.')
        return os.environ['GOOGLE_APPLICATION_CREDENTIALS']

    @staticmethod
    def get_project_id() -> str:
        if "GOOGLE_PROJECT_ID" not in os.environ:
            raise Exception('GOOGLE_PROJECT_ID must be declared in your environment.')
        return os.environ['GOOGLE_PROJECT_ID']

    @staticmethod
    def get_topic_name() -> str:
        if "GOOGLE_PUBSUB_TOPIC_NAME" not in os.environ:
            raise Exception('GOOGLE_PUBSUB_TOPIC_NAME must be declared in your environment.')
        return os.environ['GOOGLE_PUBSUB_TOPIC_NAME']
