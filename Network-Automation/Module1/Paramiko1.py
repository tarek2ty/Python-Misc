"""
Paramiko is a low-level dirty library.
it does not have a control mechanism
it will show every bit of the output even the prompt 

-Define Host
-Define SSH Client
-Invoke Shell
-Send Command
-Receive Output
"""
import time
import paramiko

def send_cmd(conn, command):
    conn.send(command+"\n")
    time.sleep(1)

def get_output(conn):
    return conn.recv(65535).decode("utf-8")

def main():
    hosts = {"192.168.45.66":"free -h"}

    for hostname, command in hosts.items():
        conn_paramiko = paramiko.SSHClient()        #define the connection
        
        conn_paramiko.set_missing_host_key_policy(paramiko.AutoAddPolicy())     #tell it to ignore unkown ssh kex and choose automatically
        
        conn_paramiko.connect(          #those are the parameters of the client
            hostname=hostname,
            port=22,
            username="eventum",
            password="P@ssw0rd",
            look_for_keys = False,
            allow_agent = False,
        )

        conn = conn_paramiko.invoke_shell()     #open a shell and write the command
        time.sleep(1)
        print("logged in" + get_output(conn).strip() +" successfully")     #this is just to make sure we are logged in

        commands = [        #the commands to send the client>> maybe a priv escalation or control length before the actual command
            command,
        ]

        for cmd in commands:
            send_cmd(conn,cmd)
            print(get_output(conn))

        conn.close()

if __name__ == "__main__":      #this part will call the main function when called from the shell directly but does not invoke it in another python file
    main()
