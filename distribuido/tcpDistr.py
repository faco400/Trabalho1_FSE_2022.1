import socket

IP_address = '164.41.98.26'
port  = 10191
server_address = (IP_address, port)

"""
Config do socket
"""
def init():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.connect(server_address)

  return server
  