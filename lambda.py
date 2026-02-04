Here's the code of lambda function

import json
import boto3

s3 = boto3.client('s3')

BUCKET_NAME = "ali-file-sharing-project"

def lambda_handler(event, context):

    # ---------- DOWNLOAD ----------
    if event.get('queryStringParameters'):

        file_name = event['queryStringParameters'].get('file')

        if not file_name:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps("Missing filename")
            }

        url = s3.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name
            },
            ExpiresIn=300
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(url)
        }

    # ---------- LIST FILES ----------
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)

    files = []

    if 'Contents' in objects:
        for obj in objects['Contents']:
            files.append(obj['Key'])

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps(files)
    }

    
