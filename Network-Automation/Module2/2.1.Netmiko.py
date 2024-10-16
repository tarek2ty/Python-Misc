#this will use ini config files instead of yaml or in-line

from netmiko import ConnectHandler
import configparser

config = configparser.ConfigParser()
config.read('props.ini')


server1 = ConnectHandler(
    host=config['SFTPconfiguration']['address'],
    username=config['SFTPconfiguration']['username'],
    password=config['SFTPconfiguration']['password'],
    device_type="linux"
)

output=server1.send_command("free -h;")
print(output)
server1.disconnect()