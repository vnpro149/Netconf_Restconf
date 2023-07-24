import requests
import json
requests.packages.urllib3.disable_warnings()
url_interfaces='https://10.215.27.111/restconf/data/ietf-interfaces:interfaces'
header={
    'Content-type':'application/yang-data+json',
    'Accept':'application/yang-data+json'
}
basicauth=('vnpro','vnpro#123')
# respon=requests.get(url=url_interfaces,headers=header,auth=basicauth,verify=False)
# print(respon.json())
urlloopback2='https://10.215.27.111/restconf/data/ietf-interfaces:interfaces/interface=Loopback2'
data={
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "Chien's loopback interface",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
resp=requests.put(url=urlloopback2,data=json.dumps(data),\
                  headers=header,auth=basicauth,verify=False)
print(resp.text)

data1={
    "ietf-interfaces:interface": {
        "description":"change description"
    }
}
# resp=requests.patch(url=urlloopback2,data=json.dumps(data1),\
#                     headers=header,auth=basicauth,verify=False)
# respon=requests.get(url=urlloopback2,headers=header,auth=basicauth,verify=False)
# print(respon.json())
print("---------------")
resp=requests.put(url=urlloopback2,data=json.dumps(data1),\
                    headers=header,auth=basicauth,verify=False)
respon=requests.get(url=urlloopback2,headers=header,auth=basicauth,verify=False)
print(respon.json())
