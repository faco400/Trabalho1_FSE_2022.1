import time
import os
import json
import threading
import tcpDistr
import control

def receive(server):
  try:
    message = server.recv(2048).decode('ascii')
    print (message)
    # str(msg)
    # print('---'+msg+'-----')
    if str(message) == 'ON':
      print('Tentei')
      GPIO.output(L_01[room], GPIO.LOW)
  except:
    # return 0
    print('nao')
    pass

if __name__ == '__main__':
  try:
    server = tcpDistr.init()
    control.states(server)
  except KeyboardInterrupt: # if ctrl + c is pressed, exit cleanly
    pass

# A Fazer...
# conectar com o server central [OK]
# instancias conectadas conforme json
# fazer as threads pra distr e central
# Atualizar temp e humidity a cada 2s separadamente
# comunicar com o server pra acionar conforme pedido lampadas, sensores e projetores e retornar sobre sucess
# Informar server central do acionamento do sensor de presença, e janelas e portas
# informar acionamento do sensor de fumaça

# ideias...
# pra comunicar sobre estados enviar sinais pro server central ...
