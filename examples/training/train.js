const AWS = require('aws-sdk');
const sagemaker = new AWS.SageMaker();

module.exports.startJob = async (event, context) => {
    // Parse the s3 event from the bucket
    const s3Reference = event.Records[0].s3;
    const bucket = s3Reference.bucket.name;
    const key = s3Reference.object.key;

    // Create the path we want to use for training / output
    let path = key;
    let lastIndex = key.lastIndexOf('/');
    if(lastIndex >= 0) {
        path = path.substr(0, lastIndex);
    }

    if(!bucket || !key) {
        console.log('Event not an S3 event');
        throw 'Event not an S3 event type';
    }

    // Create the training job
    await createTrainingJob({
        TrainingJobName: key.replace(/\./g, '-') + '-' + new Date().getTime(),
        RoleArn: process.env.trainingRole,
        HyperParameters: {
            feature_dim: '1'
        },
        AlgorithmSpecification: {
            TrainingInputMode: 'File',
            TrainingImage: process.env.trainingImage,
        },
        InputDataConfig: [{
            ChannelName: 'train',
            DataSource: {
                S3DataSource: {
                    S3DataType: 'S3Prefix',
                    S3Uri: `s3://${bucket}/${path}`,
                    S3DataDistributionType: 'ShardedByS3Key'
                }
            },
            ContentType: 'application/x-recordio-protobuf',
            CompressionType: 'None'
        }],
        OutputDataConfig: {
            S3OutputPath: `s3://${process.env.aiModelBucket}/${path}/model`
        },
        ResourceConfig: {
            InstanceType: 'ml.c5.xlarge',
            InstanceCount: 1,
            VolumeSizeInGB: 1
        },
        StoppingCondition: {
            MaxRuntimeInSeconds: 10 /*minutes*/ * 60 /*seconds*/
        }
    });
}

function createTrainingJob(params) {
    return new Promise((resolve, reject) => {
        sagemaker.createTrainingJob(params, (err, data) => {
            if(err) {
                console.log('An error occured while creating training job', err);
                reject(err);
                return;
            }

            resolve(data);
        });
    });
}