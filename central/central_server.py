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

# Apagar? Desnecessario...
def handle(conn):
  try:
    while True:
      status = conn.recv(2048).decode('ascii')
      status = json.loads(status)
      room_status = status
      # print(status)
  except KeyboardInterrupt:
    print('Error handling connections')
    exit()

def show_output(conn):
  try:
    status = conn.recv(2048).decode('ascii')
    status = json.loads(status)

    print('Saidas:')
    print('1) L_01: '+status['L_01'])
    print('2) L_02: '+status['L_02'])
    print('3) AC: '+status['AC'])
    print('4) PR: '+status['PR'])
  except:
    print('Error getting output')

def get_status(conn):
  try:
    status = conn.recv(2048).decode('ascii')
    status = json.loads(status)

    print('Saidas:')
    print('L_01: '+status['L_01']+' L_02: '+status['L_02'])
    print('AC: '+status['AC'])
    print('PR: '+status['PR'])
    print('AL_BZ: '+status['AL_BZ'])
    print('Sensores:')
    print('SPres: '+status['SPres'])
    print('SFum: '+status['SFum'])
    print('SJan: '+status['SJan']+' SPor: '+status['SPor'])
    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(status['Temperatura'], status['Humidade']))
    print('Total de pessoas nesta sala: '+status['Pessoas'])
  except:
    print('Error getting status')

def get_sucess(conn):
  try:
    response = conn.recv(2048).decode('ascii')
    if response == 'OK':
      print('Dispositivo alternado com sucesso!')
    elif response == 'NOT_OK':
      print('Houve problema em alternar(ON/OFF) dispositivo!!')
  except:
    print('Error getting response')
    

def receive():
  try:
    while True:
      conn, addr = server.accept()
      addresses.append(addr[0])
      listconn[addr[0]] = conn
      print(f"{str(addr)} connected")

  except KeyboardInterrupt:
    return

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
        if len(addresses) == 0:
          print('Nenhuma sala conectada')
          input('Aperte enter para continuar...')
          continue

        room = -1
        while room > len(addresses) or room < 0:
          os.system('clear')
          print('------- Listar Estados -------')
          print('Salas conectadas:')
          for i in range(len(addresses)):
            print(f'Sala {i} - IP:{addresses[i]}')
          room = int(input('Digite o numero da sala desejada'))

        sendCommand(listconn[addresses[room]], f'GET_STATUS') #Mandar ip? Sala...?
        get_status(listconn[addresses[room]])
        input('Aperte enter para continuar...')

      if int(op) == 2:
        if len(addresses) == 0:
          print('Nenhuma sala conectada')
          input('Aperte enter para continuar...')
          continue
        room = -1
        while room > len(addresses) or room < 0:
          os.system('clear')
          print('----- Listar Estados -------')
          print('Salas conectadas:')
          for i in range(len(addresses)):
            print(f'Sala {i} - IP:{addresses[i]}')
          room = int(input('Digite o numero da sala desejada: '))
        
        device = -1
        while device < 1 or device > 6:
          os.system('clear')
          print('-------- Dispositivos --------')
          sendCommand(listconn[addresses[room]], f'GET_STATUS')
          show_output(listconn[addresses[room]])
          print('OBS: Escolha o digito 5 para acionar todos os dispositivos (ON) e 6 para desativar(OFF)')
          device = int(input('Digite o numero do dispositivo que deseja alternar entre ON/OFF: '))
          if device == 1:
            sendCommand(listconn[addresses[room]], f'ON_OFF_L_01')
          elif device == 2:
            sendCommand(listconn[addresses[room]], f'ON_OFF_L_02')
          elif device == 3:
            sendCommand(listconn[addresses[room]], f'ON_OFF_AC')
          elif device == 4:
            sendCommand(listconn[addresses[room]], f'ON_OFF_PR')
          elif device == 5:
            sendCommand(listconn[addresses[room]], f'ON_ALL')
          elif device == 6:
            sendCommand(listconn[addresses[room]], f'OFF_ALL')
          get_sucess(listconn[addresses[room]])
          print('Redirecionando para o menu. Aguarde...')
          time.sleep(2)
        
      if int(op) == 3:
        quit()

  except KeyboardInterrupt:
    quit()


if __name__ == '__main__':
  server = tcpCentral.init() #Configura socket do servidor central
  menuThread = threading.Thread(target=menu, ) #thread pra conversar com user
  menuThread.start()  # inicia a thread
  receive() # Inicia dialogo com distr