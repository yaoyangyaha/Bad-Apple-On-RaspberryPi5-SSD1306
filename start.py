import time
from board import SCL, SDA
import busio
import adafruit_ssd1306
import os
from PIL import Image
from playsound import playsound
import pygame


# Raspberry Pi pin configuration:
RST = None
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
fps = 30
PATH = 'img/'
i2c = busio.I2C(SCL, SDA)
# 128x64 display with hardware I2C:
disp = adafruit_ssd1306.SSD1306_I2C(84, 48, i2c)
# Initialize library.

# Clear display.
disp.fill(0)
disp.show()

time_sta = time.time()
pygame.mixer.init()
pygame.mixer.music.load("badapple.mp3")
pygame.mixer.music.play()
while True:
    # Current Time
    time_cur = time.time()
    # Calculate the right frame to display
    frame = int((time_cur - time_sta) * fps) + 1
    if frame > 6564:
        timecur=time_cur
        break
    filename = 'ba' + str(frame) + '.bmp'
    
    # Load image and convert to 1 bit color.
    image = Image.open(os.path.join(PATH,filename)).convert('1')
    disp.image(image)
    disp.show()
print(timecur-time_sta)
    
