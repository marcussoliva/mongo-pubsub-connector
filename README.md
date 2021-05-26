# Mongo Pub/Sub Connector
Sync data from MongoDB to Google Cloud Pub Sub 

<img src="https://raw.githubusercontent.com/marcussoliva/mongo-pubsub-connector/master/logo.png" alt="Mongo PubSub Connector Logo" width="600" height="200"/>


## What is it?

Mongo Pub/Sub Connector is an connector to sync data from MongoDB to Google Cloud Pub/Sub. 
Mongo Pub/Sub Connector uses MongoDB Streams API and then, your mongodb server needs supports this API.

## Why Sync data to Google Cloud Pub/Sub?

The objective is sync data easy and safe way from MongoDB to GCP services and Google Pub/Sub has compatibility with many
others Google Cloud Services (GS, Composer, Dataproc, Dataflow and others).



## How to use this image
### Running the daemon
One of the important things to note about Mongo Pub/Sub Connector is that you need set ENVs variables: 
```docker
docker run  -e MONGO_URI='your-mongodb-uri'  -e GOOGLE_PROJECT_ID='google-project-id'  -e  GOOGLE_PUBSUB_TOPIC_NAME='your-google-pubsub-topic-name' -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/credentials.json -v your-credentials-path-json-file:/tmp/keys/credentials.json  --name mongo-pubsub-connector solivavinicius/mongo-pubsub-connector:latest
```


