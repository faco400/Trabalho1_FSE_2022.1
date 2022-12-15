import socket

host = '164.41.98.26'
port = 10191
server_address = (host, port)

def init():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(server_address)
  server.listen(4)

  return server

def accept_connections():
  server = init()
  while True:
    conn, addr = server.accept()
    print(f"{str(addr)} connected")
  
  
def handle(conn):
  try:
    status = conn.recv(2048).decode('ascii')
    status = json.loads(status)
    print(status)
    room_status = status
    return room_status

  except:
    print('Error handling connection')

def receive():
  try:
    # ip_test = addr[0]
    # if ip_test == '164.41.98.16' or ip_test == '164.41.98.28':
    #   print('Usa config 1')
    #   pass
    # elif ip_test == '164.41.98.26' or ip_test == '164.41.98.15':
    #   print('Usa config 2')
    #   pass
    while True:
      conn, addr = server.accept()
      print(f"{str(addr)} connected")
      # cria uma thread que ira tratar o cliente
      thread = threading.Thread(target=handle, args=(conn,))
      thread.start()  # inicia a thread

      # Envia teste para enviar comandos
      # thread = threading.Thread(target=send, args=(conn,))
      # thread.start()  # inicia a thread

  except KeyboardInterrupt:
    conn.close()