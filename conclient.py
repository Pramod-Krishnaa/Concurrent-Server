import socket
HEADER=64
PORT=5050
FORMAT='utf-8'
DISCONNECT_MSG='!disconnect'
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    try:
        message=msg.encode(FORMAT)
    except:
        message=msg
    
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+= b' ' *(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))
msg=''
while(msg!=DISCONNECT_MSG):
    msg=input('\n\n>')
    send(msg)