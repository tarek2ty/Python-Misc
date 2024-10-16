from netmiko import ConnectHandler

server1 = ConnectHandler(
    host="192.168.45.66",
    username="eventum",
    password="P@ssw0rd",
    device_type="linux"
)



print(f"Logged into {server1.find_prompt()} successfully")

result = server1.send_command("free -h")
print(result)
server1.disconnect()
