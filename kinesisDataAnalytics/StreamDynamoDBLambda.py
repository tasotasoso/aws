from __future__ import print_function
import logging
import base64
import boto3
import json
import decimal

logger = logging.getLogger()
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name=[DynamoDBのリージョン], endpoint_url=[DynamoDBのエンドポイント])
table = dynamodb.Table([テーブル名])

def lambda_handler(event, context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        jpayload = json.loads(payload)
        
        
        TEMPERATURE = str(jpayload['AVGTEMPERATURE'])
        HUMIDITY = str(jpayload['AVGHUMIDITY'])
        AVGTIME = jpayload['AVGTIME']
        sAVGTIME = AVGTIME.split(" ")
        DATE = str(sAVGTIME[0])
        TIME = str(sAVGTIME[1])
        
        response = table.put_item(
        Item={
            'DATE': DATE,
            'TIME' : TIME,
            'TEMPERATURE': TEMPERATURE,
            'HUMIDITY':HUMIDITY
        }
        )