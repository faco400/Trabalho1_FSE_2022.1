import RPi.GPIO as GPIO
import adafruit_dht
import time
from definitions import *
import os
import socket

room = 0
dht_device = adafruit_dht.DHT22(DHT22[room])


"""
Config do socket
"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '164.41.98.26'

def setupPins():
  # rasp pin mode setup
  GPIO.setmode(GPIO.BCM)
  # rasp in setup
  GPIO.setup(L_01[room], GPIO.OUT)
  GPIO.setup(L_02[room], GPIO.OUT)
  GPIO.setup(AC[room], GPIO.OUT)
  GPIO.setup(PR[room], GPIO.OUT)
  GPIO.setup(AL_BZ[room], GPIO.OUT)
  GPIO.setup(SPres[room], GPIO.IN)
  GPIO.setup(SFum[room], GPIO.IN)
  GPIO.setup(SJan[room], GPIO.IN)
  GPIO.setup(SPor[room], GPIO.IN)
  GPIO.setup(SC_IN[room], GPIO.IN)
  GPIO.setup(SC_OUT[room], GPIO.IN)

def getHumidity():
  # humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT22[room])
  temperature = dht_device.temperature
  humidity = dht_device.humidity
  if humidity is not None and temperature is not None:
    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
  else:
    print("Failed to retrieve data from humidity sensor")

if __name__ == '__main__':
  try:
    countP = 0
    setupPins()
    while(1):
      if GPIO.input(L_01[room]):
        print('A lampada 1 ta acesa')
      else:
        print('A lampada 1 ta apagada')
      if GPIO.input(L_02[room]):
        print('A lampada 2 ta acesa')
      else:
        print('A lampada 2 ta apagada')
      if GPIO.input(AC[room]):
        print('O ar condicionado esta ligado')
      else:
        print('O ar condicionado esta desligado')
      if GPIO.input(PR[room]):
        print('O projetor esta ligado')
      else:
        print('O projetor esta desligado')
      if GPIO.input(SC_IN[room]):
        print('Alguem entrou no predio')
        countP = countP + 1
        print(countP)
      else:
        pass
      if GPIO.input(SC_OUT[room]):
        print('Alguem saiu no predio')
        if countP > 0 and countP != 0:
          countP = countP - 1
        print(countP)
      else:
        pass
      if GPIO.input(SFum[room]):
        print('Sensor de fumaça ligado')
      else:
        print('Sensor de fumaça desligado')
      if GPIO.input(SJan[room]):
        print('Janela aberta')
      else:
        print('Janela fechada')
      if GPIO.input(SPor[room]):
        print('Porta aberta')
      else:
        print('Porta fechada')

      print(f'Ha {countP} pessoas na sala')
      getHumidity()
      time.sleep(0.5)
      os.system('clear')
  except KeyboardInterrupt: # if ctrl + c is pressed, exit cleanly
    # GPIO.cleanup()
    pass

# A Fazer...
# conectar com o server central
# instancias conectadas conforme json
# fazer as threads pra distr e central
# Atualizar temp e humidity a cada 2s separadamente
# comunicar com o server pra acionar conforme pedido lampadas, sensores e projetores e retornar sobre sucess
# Informar server central do acionamento do sensor de presença, e janelas e portas
# informar acionamento do sensor de fumaça

# ideias...
# pra comunicar sobre estados enviar sinais pro server central ...
