#!/usr/bin/env python3
import urllib.request, json, os


BASE_URL = "http://127.0.0.1:8000/s/bkps/"


with urllib.request.urlopen(BASE_URL) as response:
    data = response.read()
    json_data = json.loads(data.decode())
    print(type(json_data))

    for backup in json_data:
        uuid = backup['uuid']

        # os.system(f'wget {BASE_URL}{uuid}/ -O {uuid}.zip')
        cmd = f'curl -O {BASE_URL}{uuid}/'
        print(cmd)
        os.system(cmd)


