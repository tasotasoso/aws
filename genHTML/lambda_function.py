import boto3
import os

def lambda_handler(event, context):

    #putトリガーの適用元
    input_bucket = event['Records']['0']['s3']['bucket']['name']
    input_key = event['Records']['0']['s3']['object']['key']
    tmp = '/tmp/' + os.path.basename(input_key)

    #出力先
    output_bucket = 'html_store'
    output_key = 'data.html'

    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(input_bucket)
        bucket.download_file(input_key, tmp)



        with open(tmp, 'r') as input_f:
            lines = [ line for line in input_f ]

            with open('./data.html', 'w') as output_f:
                output_f.write('<html><head></head><body>\n')
                [output_f.write(line + '\n') for line in lines]
                output_f.write('</body></html>')

                s3.Bucket(output_bucket).put_object(Key = output_key ,
                                                    Body = output_f)
    
    except Exception as e:
        raise e