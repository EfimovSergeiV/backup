#!/usr/bin/env python3
import urllib.request, json, os


BASE_URL = "http://192.168.60.203/s/bkps/"


with urllib.request.urlopen(BASE_URL) as response:
    data = response.read()
    json_data = json.loads(data.decode())
    print(type(json_data))

    for backup in json_data:
        uuid = backup['uuid']

        cmd = f'wget --content-disposition { BASE_URL }{ uuid }/'
        
        print(cmd)
        os.system(cmd)


