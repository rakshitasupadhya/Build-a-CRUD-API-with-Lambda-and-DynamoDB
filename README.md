# Build-a-CRUD-API-with-Lambda-and-DynamoDB
This is a demonstration on creating a serverless API that creates, reads, updates, and deletes items from a DynamoDB table

# Architecture
<img width="384" alt="image" src="https://github.com/rakshitasupadhya/Build-a-CRUD-API-with-Lambda-and-DynamoDB/assets/107621546/9a85e962-cffd-4dd6-90fb-986f69f05d4f">

# Implementation
1. Create DynamoDB and enter Partition key as ID
2. Create a Lambda function and attach a role to it
3. Create an HTTP API
4. Create routes
   1. GET /items/{id}
   2. GET /items
   3. PUT /items
   4. DELETE /items/{id}
5. Create an integration
6. Attach your integration to routes
7. Test your API using Postman
