import re
import yaml
from netmiko import ConnectHandler as connect


def hostname(text):
    machine_id = re.compile(r"\s+Operating System.*:\s+(?P<OS>.*)")
    
    model_match = machine_id.search(text)
    if model_match:
        return model_match.group("OS")
    return None


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
    result = server.send_command("hostnamectl")
    print(hostname(result))
    print()
    server.disconnect()