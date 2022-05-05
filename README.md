
# RPI RGB Matrix MQTT Controller

This project incorporates the ws281x Raspberry Pi matrix controller.  
 The example.py file is used to test if the matrix is rendering correctly and to give an example on its usage.   
The rpi-matrixMQTT.py incorporates an MQTT client to controll the matrix.    

Collaborated with https://github.com/justinfederico he created a flask website to send MQTT messages containing an image or a link to be displayed by the Raspberry Pi.  
The repository: https://github.com/justinfederico/RGB-Matrix-Control-Website


## Installation
Install Pillow
"pip3 install Pillow"

Install ws281x Driver
"pip3 install rpi-ws281x"

Clone the Repo
"git clone https://github.com/aedlebeck/RPI-RGBMatrix-MQTT"
## Usage/Examples

Adjust the variables for different matrixes 

```
ws281xMatrix.py
```
```python
def __init__(
        self,
        width = 32,          # Number of pixels in width
        height = 8,         # Number of pixels in height
        led_pin = 18,        # PWM pin
        freq = 800000,       # 800khz
        dma_channel = 10,
        invert = False,      # Invert Shifter, should not be needed
        brightness = 0.1,    # 1: 100%, 0: 0% everything in between.
        led_channel = 0,     # set to '1' for GPIOs 13, 19, 41, 45 or 53
        led_type = None,     # Read the documentation to get your strip type.
        fps = 10             # frames per second.
    ):
```  
Run example.py:
```
sudo python3 example.py
```
*sudo is required as the PWM0 channel has to be accessed by the RGB matrix driver
## Libraries Used
Pillow 
https://github.com/python-pillow/Pillow

rpi_ws281x
https://github.com/jgarff/rpi_ws281x

rpi_ws281x python wrapper
https://github.com/whizzzkid/rpi-ws281x-matrix-python

