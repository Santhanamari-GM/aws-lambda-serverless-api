# AWS Lambda & Serverless API

A simple serverless REST API built using **AWS Lambda, Amazon API Gateway, and Python**. This project demonstrates how to create, deploy, integrate, and test serverless applications on AWS without managing servers.

## Project Overview

The objective of this project is to understand serverless computing and build a working API using AWS services.

The API accepts HTTP GET and POST requests through Amazon API Gateway, invokes an AWS Lambda function, and returns JSON responses.

## Key Objectives

- Understand serverless computing.
- Learn AWS Lambda fundamentals.
- Create and test a Lambda function using Python.
- Understand Amazon API Gateway.
- Integrate API Gateway with Lambda.
- Build and test a serverless REST API.
- Monitor Lambda execution using Amazon CloudWatch.

## Technologies Used

| Technology | Purpose |
|---|---|
| AWS Lambda | Executes Python code without managing servers |
| Amazon API Gateway | Creates and manages HTTP API endpoints |
| Python 3.15 | Backend programming language |
| Amazon CloudWatch | Monitors execution logs |
| Postman | Tests GET and POST API requests |

## Architecture

The application follows this serverless architecture:

```text
       Client / User
             |
             v
      Amazon API Gateway
             |
             v
        AWS Lambda
       (Python 3.15)
             |
             v
       JSON Response
             |
             v
        Client/User

    Amazon CloudWatch
    (Execution Logs)
```

## Project Implementation

### 1. Create AWS Lambda Function

- Open AWS Lambda Console.
- Create a new function.
- Function name: `ws-serverless-api`
- Runtime: Python 3.15.
- Create an execution role with basic Lambda permissions.

### 2. Implement Python Code

The Lambda function supports GET and POST requests.

**GET Request:**

Returns a welcome message.

Example response:

```json
{
  "message": "Welcome to AWS Serverless API!",
  "status": "Success",
  "technology": "AWS Lambda",
  "method": "GET"
}
```

**POST Request:**

Accepts a user's name and returns a personalized response.

Example request:

```json
{
  "name": "EIMLISNU"
}
```

Example response:

```json
{
  "message": "Hello EIMLISNU!",
  "status": "Success",
  "method": "POST"
}
```

### 3. Create Amazon API Gateway

- Create an HTTP API.
- Integrate it with the Lambda function.
- Configure the following routes:

| HTTP Method | Resource Path |
|---|---|
| GET | `/hello` |
| POST | `/hello` |

Both routes connect to the same Lambda function.

### 4. API Endpoint

The API is deployed in the AWS Mumbai region (`ap-south-1`).

**Base URL:**

```text
https://23m96x1o07.execute-api.ap-south-1.amazonaws.com
```

**GET Endpoint:**

```text
GET /hello
```

**POST Endpoint:**

```text
POST /hello
```

### 5. Test Using Postman

**GET Request**

- Method: GET
- Endpoint: `/hello`
- Expected status: `200 OK`

**POST Request**

- Method: POST
- Endpoint: `/hello`
- Body type: Raw JSON
- Content-Type: `application/json`

Request body:

```json
{
  "name": "EIMLISNU"
}
```

Both GET and POST requests were successfully tested using Postman.

### 6. Monitor Using Amazon CloudWatch

CloudWatch was used to monitor Lambda function execution.

Log group:

```text
/aws/lambda/ws-serverless-api
```

CloudWatch provides information about:

- Lambda execution.

## Key Learnings

- Understanding serverless architecture.
- Creating and deploying AWS Lambda functions.
- Writing Python code for serverless applications.
- Configuring HTTP APIs using API Gateway.
- Integrating API Gateway with Lambda.
- Testing APIs using Postman.
- Monitoring application execution using CloudWatch.

## Project Result

Successfully developed and deployed a serverless REST API using AWS Lambda and Amazon API Gateway.

The API supports GET and POST methods, returns JSON responses, and successfully executes requests through Postman. Lambda execution logs were also verified using Amazon CloudWatch.
