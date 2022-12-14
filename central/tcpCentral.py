import socket

host = '164.41.98.26'
port = 10191
server_address = (host, port)

def init():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(server_address)
  server.listen(4)

  return server
