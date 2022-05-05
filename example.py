import signal
import os
import time
from ws281xMatrix import WS281xMatrix

path = os.path.dirname(__file__)
im = os.path.join(path, 'curImg.png')
gif = os.path.join(path, 'curGif.gif')

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
    screen.render_image(s)


def setGif(s):
    clearScreen()
    screen.render_animation(s, loops = 100)


#Tuple R,G,B for color
def setColor(color):
    clearScreen()
    screen.next_frame(screen.blank_frame(color))
  
#Test matrix
print('Blue')
setColor((0,0,255))
time.sleep(3)
screen.render_image(im)
time.sleep(10)
screen.render_animation(gif)
time.sleep(20)

