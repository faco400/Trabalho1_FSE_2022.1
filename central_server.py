import socket
import os
import threading
import json
import time

host = '164.41.98.26'
port = 10191
server_address = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET, SO_REUSEADDR, 1)

server.bind(server_address)
server.listen(4)

def handle(conn):
  try:
    print('Estados das Saidas:')
    while True:
      # os.system('clear')
      # conn.send('L_01'.decode('ascii'))
      status = conn.recv(2048).decode('ascii')
      if not status:
        print('oi')
      status = json.loads(status)
      print(status)
      # if status == 'L_01_ON':
      #   print('Lampada 1 ligada')
      # elif status == 'L_01_OFF':
      #   print('Lampada 1 desligada')
      # if status == 'L_02_ON':
      #   print('Lampada 2 ligada')
      # elif status == 'L_02_OFF':
      #   print('Lampada 2 desligada')
      # if status_AC == 'AC_ON':
      #   print('Ar condicionado ligado')
      # elif status_AC == 'AC_OFF':
      #   print('Ar condicionado desligado')
      # if status_PR == 'PR_ON':
      #   print('Projetor ligado\n')
      # elif status_PR == 'PR_OFF':
      #   print('Projetor desligado\n')
      # if status_AL_BZ == 'AL_BZ_ON':
      #   print('Alarme ligado')
      # elif status_AL_BZ == 'AL_BZ_OFF':
      #   print('Alarme desligado')
      # print('Estados das Sensores:')
  except:
    return

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

  except KeyboardInterrupt:
    conn.close()

    
def menu():
  try:
    op = 0
    while op != 1 or op !=2:
      op = input('Digite 1 para monitorar os sensores\nDigite 2 para sair do programa\n')
      op = int(op)
      if op == 1:
        room = 0
        while room < 1 or room > 4:
          os.system('clear')
          room = input('Digite o numero da sala que deseja monitorar (1-4)\n')
          room = int(room)
          # receive()
      elif op == 2:
        return 0
  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  os.system('clear')
  receive()
  # Fazer thread pro menu() e desenvolve-lo