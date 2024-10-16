from netmiko import ConnectHandler, file_transfer

server = ConnectHandler(
    host="192.168.45.66",
    username="eventum",
    password="P@ssw0rd",
    device_type="linux",
)

print(f"logged in {server.find_prompt()}-----")
# print(server.send_command("touch /home/eventum/Training_Lab/tarek_tests/hosts.yaml"))
# quit()
transfer = file_transfer(
    server,
    source_file="/home/eventum/Training_Lab/tarek_tests/process.csv",
    dest_file="process.csv",
    direction="get",
    overwrite_file=False,
    file_system="/",
    disable_md5=False,

)
print(transfer)
server.disconnect()