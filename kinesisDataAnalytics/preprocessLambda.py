from __future__ import print_function

import base64
import json
import re

print('Loading function')

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        
        #decode csv from IoT
        payload = base64.b64decode(record['data'])
        parsedPayloads = re.split('[:,]', payload)

        temperature = parsedPayloads[1]
        humidity = parsedPayloads[3]
        jrpayload = {}
        jrpayload["TEMPERATURE"] = temperature 
        jrpayload["HUMIDITY"] = humidity
        
        #encode json payload for return
        rpayload = json.dumps(jrpayload)

        # Do custom processing on the record payload here
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(rpayload)
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}