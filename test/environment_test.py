import unittest
import os
from src.environment.environment import MongoEnvironment, GoogleCloudEnvironment


class MongoEnvironmentTest(unittest.TestCase):

    def tearDown(self) -> None:
        if "MONGO_URI" in os.environ:
            del os.environ["MONGO_URI"]

    def test_if_mongo_uri_exists_in_env(self):
        os.environ["MONGO_URI"] = "mongodb+srv://root:root@localhost"
        mongodb_uri = MongoEnvironment.get_mongodb_uri()
        self.assertIsNotNone(mongodb_uri, msg="mongodb_uri exists in environment")

    def test_raise_exception_if_mongo_uri_not_exists_in_env(self):
        self.assertRaises(Exception, MongoEnvironment.get_mongodb_uri)


class GoogleCloudEnvironmentTest(unittest.TestCase):
    def tearDown(self) -> None:
        if "GOOGLE_APPLICATION_CREDENTIALS" in os.environ:
            del os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        if "GOOGLE_PROJECT_ID" in os.environ:
            del os.environ["GOOGLE_PROJECT_ID"]
        if "GOOGLE_PUBSUB_TOPIC_NAME" in os.environ:
            del os.environ["GOOGLE_PUBSUB_TOPIC_NAME"]

    def test_if_google_cloud_application_credentials_exists_in_env(self) -> None:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/credentials.json"
        gac = GoogleCloudEnvironment.get_credentials()
        self.assertIsNotNone(gac)

    def test_if_google_cloud_project_id_exists_in_env(self) -> None:
        os.environ["GOOGLE_PROJECT_ID"] = "my-project-id"
        gp = GoogleCloudEnvironment.get_project_id()
        self.assertIsNotNone(gp)

    def test_if_google_cloud_pubsub_name_exists_in_env(self) -> None:
        os.environ["GOOGLE_PUBSUB_TOPIC_NAME"] = "my-pubsub-topic"
        topic = GoogleCloudEnvironment.get_topic_name()
        self.assertIsNotNone(topic)

    def test_if_google_cloud_application_credentials_not_exists_in_env(self):
        self.assertRaises(Exception, GoogleCloudEnvironment.get_credentials)

    def test_if_google_cloud_project_id_not_exists_in_env(self) -> None:
        self.assertRaises(Exception, GoogleCloudEnvironment.get_project_id)

    def test_if_google_cloud_pubsub_name_not_exists_in_env(self) -> None:
        self.assertRaises(Exception, GoogleCloudEnvironment.get_topic_name)
