#this will scp the /etc/hosts file to us 
import yaml
from netmiko import ConnectHandler as connect
from netmiko import file_transfer

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
    tansfer_hosts= file_transfer(
        server,
        source_file=device['file_location'],
        dest_file="kpis.txt",
        direction="get",
        overwrite_file=False,
    )
    
    print(tansfer_hosts)

    server.disconnect()
    print()
