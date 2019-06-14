# csv-protobuf-pipeline

This project provides a serverless approach for turning CSV files into training material for AWS Sagemaker. The solution is designed to be a data transformation pipeline for numerical based data, leveraging buckets for both input and output.

This project was created by Inspired Futures AI, LLC to support machine learning for its mytaptrack® device and platform.

## Dependencies

This project has most of its dependencies checked into source control; modifications needed to be made to some of the dependencies to fit the contraints of AWS Lambda. This project requires the following dependencies:

- NodeJS
- Serverless Framework (including setup and configuration)

## Deploying

### Deploy the pipeline
1. navigate to the pipeline directory
2. run "npm install" to install serverless dependencies
```
npm install
```
3. run "serverless deploy"
```
serverless deploy --stage dev --service <your service name>
```

### Deploy the example
1. navigate to "examples/training"
2. run "npm install" to install serverless components
```
npm install
```
3. run "serverless deploy"
```
serverless deploy --stage dev --training-bucket <your service name>-dev-output
```

## Parameters

**--input** *The input bucket name*
This parameter sets the bucket name, which will be the input bucket. This bucket **must be** a new bucket, which will be created by the serverless deployment - the Lambda function must create a subscription to the bucket.

**--output** *The output bucket name*
This parameter sets the bucket name, which will be the output bucket. This bucket **will not** be created by the serverless deployment, and must be created either by another deployment or manually.

**--output-prefix** *The output key prefix for objects being output*
This parameter sets the prefix to attach to the objects being output by the pipeline.

**--stage** *The name of the stage*
Stage is used to specify different environments to deploy to.

**--region** *The AWS region*
Region is used to specify the region to be deployed to.

## License
This library is licensed under the MIT License