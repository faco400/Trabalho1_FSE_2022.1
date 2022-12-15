import os
import threading
import json
import time
import tcpCentral
import sys

room_status = []
listconn = {}
addresses = []

def sendCommand(conn, COMMAND):
  conn.send(COMMAND.encode('ascii'))
  # print("oi")

# Apagar? Desnecessario...
def handle(conn):
  try:
    while True:
      status = conn.recv(2048).decode('ascii')
      status = json.loads(status)
      room_status = status
      print(status)
  except KeyboardInterrupt:
    print('Error handling connections')
    exit()

def get_status(conn):
  try:
    status = conn.recv(2048).decode('ascii')
    status = json.loads(status)
    # print(status)
    return status
  except:
    print('Error getting status')

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
      addresses.append(addr[0])
      listconn[addr[0]] = conn
      print(f"{str(addr)} connected")

  except KeyboardInterrupt:
    # conn.close()
    pass

    
def menu():
  try:
    op = 0
    while op != 3:
      os.system('clear')
      print('-----MENU------')
      print('1) Listar estados dos dispositivos das salas') # Por enquanto funciona voltado para uma sala 1
      print('2) Ative um dispositivo') # Em construção...
      print('3) Sair do programa')
      op = input('Digite uma opcao: ')
      if int(op)<1 or int(op)> 3:
        menu()
      
      if int(op) == 1:
        sendCommand(listconn[addresses[0]], 'GET_STATUS')
        print(get_status(listconn[addresses[0]]))
        time.sleep(3)

      if int(op) == 2:
        pass
      if int(op) == 3:
        quit()

  except KeyboardInterrupt:
    quit()


if __name__ == '__main__':
  server = tcpCentral.init() #Configura socket do servidor central
  menuThread = threading.Thread(target=menu, ) #thread pra conversar com user
  menuThread.start()  # inicia a thread
  receive() # Inicia dialogo com distr