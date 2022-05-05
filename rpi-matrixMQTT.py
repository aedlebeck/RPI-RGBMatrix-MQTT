"""
Filename: rpi-matrixMQTTC.py
Author: Aaron Edlebeck
Description: Accepts messages from an MQTT broker containing 'I:' or 'G:' 
             followed by a link to an image or gif.
"""
import os
import sys
import signal
from ws281xMatrix import WS281xMatrix
import paho.mqtt.client as mqtt
import requests

path = os.path.dirname(__file__)

screen = WS281xMatrix()

#Handles signal iterrupts
def sigint_handler(signal, frame):
    print("KeyboardInterrupt\m")
    screen.kill()
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


def clearScreen():
    screen.reset()
 
def setImg(s):
    clearScreen()
    if s == "I:":
        image = os.path.join(path, 'sample.png')
    else:
        image = os.path.join(path, 'curImg.png')
        url = s[2:]
        data = requests.get(url).content
        with open('curImg.png', 'wb') as handler:
            handler.write(data)

    screen.render_image(image)


def setGif(s):
    clearScreen()
    if s == "G:":
        gif = os.path.join(path, 'gif2.gif')
    else:
        gif = os.path.join(path, 'curGif.gif')
        url = s[2:]
        data = requests.get(url).content
        with open('curGif.gif', 'wb') as handler:
            handler.write(data)

    screen.render_animation(gif, loops = 100)


""" Tuple R,G,B for color """
def setColor(color):
    clearScreen()
    screen.next_frame(screen.blank_frame(color))
   

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}\n")
    userInput = str(msg.payload)
    userInput = userInput[2:]
    userInput = userInput[:-1]
    print(userInput + "\n")
    if userInput[:2] == "I:":
        setImg(userInput)
    elif userInput[:2] == "G:":
        setGif(userInput)
    elif userInput[:2] == "C:":
        clearScreen()
    else:
        print("Incorrect formatting")

     
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection successful")
    else:
        print("Connection failed with code {rc}")

#Setup connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)
client.subscribe("/raspberrypi/matrix/links", qos=0)
client.loop_forever()

