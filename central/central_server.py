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
    # return status
    print('Saidas:')
    print('L_01: '+status['L_01'])
    print('L_02: '+status['L_02'])
    print('AC: '+status['AC'])
    print('PR: '+status['PR'])
    print('AL_BZ: '+status['AL_BZ'])
    print('Sensores:')
    print('SPres: '+status['SPres'])
    print('SFum: '+status['SFum'])
    print('SJan: '+status['SJan'])
    print('SPor: '+status['SPor'])
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
        room = -1
        while room > len(addresses) or room < 0:
          os.system('clear')
          print('-----SUBMENU-------')
          print('Salas conectadas:')
          for i in range(len(addresses)):
            print(f'Sala {i} - IP:{addresses[i]}')
          room = int(input('Digite o numero da sala desejada'))


        sendCommand(listconn[addresses[room]], f'GET_STATUS{addresses[room]}') #Mandar ip? Sala...?
        get_status(listconn[addresses[room]])
        input('Aperte enter para continuar...')
        

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