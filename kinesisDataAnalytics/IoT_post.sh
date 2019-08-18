#!/bin/bash
curl -D - --tlsv1.2 -X POST --cert ./cert.pem --key ./private.pem --cacert ./RootCA1.pem [自分のAWS-IoTのエンドポイント]:8443/IoT_topic?qos=0 -d $1