from google.cloud import pubsub_v1
import json
from google.api_core.exceptions import AlreadyExists


class Publisher:
    __publisher = ''
    __topic = None
    __topic_path = None

    def __init__(self, topic_name=None, project_id=None):
        if not topic_name or not project_id:
            raise Exception("topic_name and project_id are required")
        self.__topic_name = "projects/{}/topics/{}".format(project_id, topic_name)
        self.__publisher = pubsub_v1.PublisherClient()
        try:
            self.__topic = self.__publisher.create_topic(name=self.__topic_name)
        except AlreadyExists as alerr:
            pass

    def publish(self, dict):
        json_message = json.dumps(dict, ensure_ascii=False)
        try:
            self.__publisher.publish(self.__topic_name, json_message.encode())
        except Exception as e:
            raise
