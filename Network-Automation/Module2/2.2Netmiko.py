#this will ssh to multiple devices in the yaml file
import yaml
from netmiko import ConnectHandler as connect


with open('hosts.yaml','r') as f:
    data=yaml.safe_load(f)

for device in list(data.values()):
    server = connect(
        host= device['add'],
        username=device['username'],
        password=device['password'],
        device_type=device['platform']
    )

    print(f"logged into {server.find_prompt()}   ")
    result = server.send_command(device['cmd'])
    print(result)
    server.disconnect()
    print()