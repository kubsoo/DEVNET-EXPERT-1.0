import requests
import json

username = 'cisco'
password = 'cisco'
device_ip = '192.168.54.131'

period = 500
receiver_ip = '192.168.54.1'
receiver_port = 57500

xpaths = {
    1:'/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds',
    2: '/memory-ios-xe-oper:memory-statistics/memory-statistic'
}

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}   

url = f'https://{device_ip}/restconf/data/Cisco-IOS-XE-mdt-cfg:mdt-config-data/'

for key,value in xpaths.items():
    body = {
      "mdt-subscription": [{
        "subscription-id": key,
        "base": {
          "stream": "yang-push",
          "encoding": "encode-kvgpb",
          "period": period,
          "xpath": value
        },
        "mdt-receivers": {
          "address": receiver_ip,
          "port": receiver_port,
          "protocol": "grpc-tcp"
        }
      }]
    }

    response = requests.post(url,auth=(username, password),headers=headers,data=json.dumps(body),verify=False)
    if response.ok:
        print(f"Subscription {key} created succesfully!")
    else:
        print(response.json())