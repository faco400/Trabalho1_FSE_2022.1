import RPi.GPIO as GPIO
import adafruit_dht
import time
import os
import json
from definitions import *

room = 0
dht_device = adafruit_dht.DHT22(DHT22[room], False)

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
  try:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    if humidity is not None and temperature is not None:
      print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
      print("Failed to retrieve data from humidity sensor")
  except:
    getHumidity()

def states(server):
  try:
    # Leitura de arquivos
    msg = {
      'L_01': 'OFF',
      'L_02': 'OFF',
      'AC': 'OFF',
      'PR': 'OFF',
      'AL_BZ': 'OFF',
      'SPres': 'OFF',
      'SFum': 'OFF',
      'SJan': 'OFF',
      'SPor': 'OFF',
      'Temperatura': '0',
      'Humidade': ''
    }
    countP = 0
    setupPins()
    while(1):
      if GPIO.input(L_01[room]):
        msg['L_01'] = 'ON'
      else:
        msg['L_01'] = 'OFF'

      if GPIO.input(L_02[room]):
         msg['L_02'] = 'ON'
        # print('lampada 2 ligada')
      else:
        msg['L_02'] = 'OFF'
        # print('lampada 2 desligada')

      if GPIO.input(AC[room]):
        msg['AC'] = 'ON'
        # print('ar condicionado ligado')
      else:
        msg['AC'] = 'OFF'
        # print('ar condicionado desligado')

      if GPIO.input(PR[room]):
        msg['PR'] = 'ON'
        # print('projetor ligado')
      else:
        msg['PR'] = 'OFF'

      if GPIO.input(AL_BZ[room]):
        msg['AL_BZ'] = 'ON'
        # print('alarme ligado')
      else:
        msg['AL_BZ'] = 'OFF'
        # print('alarme desligado')

      if GPIO.input(SC_IN[room]):
        print('Alguem entrou no predio')
        countP = countP + 1
      if GPIO.input(SC_OUT[room]):
        print('Alguem saiu no predio')
        if countP > 0 and countP != 0:
          countP = countP - 1

      if GPIO.input(SPres[room]):
        # print('Sensor de fumaça ligado')
        msg['SPres'] = 'ON'
      else:
        msg['SPres'] = 'OFF'

      if GPIO.input(SFum[room]):
        msg['SFum'] = 'ON'
      else:
        msg['SFum'] = 'OFF'
      
      if GPIO.input(SJan[room]):
        msg['SJan'] = 'ON'
      else:
        msg['SJan'] = 'OFF'
      
      if GPIO.input(SPor[room]):
        msg['SPor'] = 'ON'
      else:
        msg['SPor'] = 'OFF'

      getHumidity()
      print(f'Ha {countP} pessoas na sala')

      # Armazenando dados em um json de estados
      with open('./states.json', 'w') as outfile:
        json.dump(msg,outfile)
      # msg_to_send = json.dumps(msg).encode('ascii')
      # server.send(msg_to_send)
      time.sleep(0.2)
      # os.system('clear')
  except KeyboardInterrupt: # if ctrl + c is pressed, exit cleanly
    # GPIO.cleanup()
    pass