## netmiko could specify what type of devices we have (cisco, linux,...)
## and it will handle the low level connectivity to them
## napalm takes this a step further and defines a higher level (API)
## so we do not need to define low level type, it will get facts for us from all devices
## it is built on top of netmiko to handle 

from napalm import get_network_driver
from yaml import safe_load

with open('hosts.yaml','r') as f:
    data=safe_load(f)

for device in list(data.values()):
    driver = get_network_driver(device['platform'])  #this will return a driver that can mange this type
    conn = driver(
        device['add'],device['username'],device['password']
        )
    ##this conn works as the conn of netmiko

    conn.open() 
    facts=conn.get_facts() #instead of passing cli commands, napalm has getters
    # getters get the values in json
    print(facts)




