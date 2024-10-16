#using cmd $hosnamectl, we extract the hostname, OS and kernel
import re
from netmiko import ConnectHandler


def hostname(text):
    machine_id = re.compile(r"\s+Operating System.*:\s+(?P<OS>.*)")
    
    model_match = machine_id.search(text)
    if model_match:
        return model_match.group("OS")
    return None

server = ConnectHandler(
    host = "192.168.45.66",
    username = "eventum",
    password = "P@ssw0rd",
    device_type = 'linux',
)

# print(server.find_prompt())

result = server.send_command("hostnamectl")
print(result)
print()
print(hostname(result))


