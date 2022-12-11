import socket

host = '164.41.98.26'
port = 10000
server_address = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, SO_REUSEADDR, 1)

server.bind(server_address)
server.listen(4)

def receive():
  while True:
    conn, addr = server.accept()
    print(f"{str(addr)} connected")
    



if __name__ == '__main__':
  # print('pi')
  receive()