import socket
import threading
import time

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MSG='!disconnect'


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[SERVER] {addr} connected.")

    while True:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            
            
            msg = msg.decode(FORMAT)
            print(f"\n[{time.ctime()}] {addr} \n[SERVER] MSG: {msg}\n")
            
            if msg==DISCONNECT_MSG:
                print("[SERVER] Closing: ",addr)
                break
            try:
                file=open(msg)
                msg=f"File Content:\n\n {file.read()}".encode(FORMAT)
            except FileNotFoundError:
                msg=f"[SERVER] File Not Found".encode(FORMAT)
            finally:
                msg+=b' '*(HEADER-len(msg))
                conn.send(msg)
    conn.close()

def start():
    server.listen()
    print(f"[SERVER] listening to {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[SERVER] Active connection - {threading.active_count()-1}.")

print("[SERVER] Starting...")
start()