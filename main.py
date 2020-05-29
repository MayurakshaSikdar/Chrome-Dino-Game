import pyautogui
from PIL import  Image, ImageGrab
import time
#from numpy import asarray

###########################################

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

###########################################

def hit(key):
    pyautogui.press(key)

###########################################

def isCollide(data):
    # cactus detection
    # (please adjust the values depending upon screen size)
    for i in range(490, 520):
        for j in range(250, 270):
            # print(data[i,j])
            if data[i, j] < 20:
                print('cactus')
                hit('up')
                return

    # bird detection
    # (please adjust the values depending upon screen size)
    for i in range(490, 520):
        for j in range(220, 250):
            if data[i, j] < 20:
                print('bird')
                hit('down')
                return

###########################################

if __name__ == "__main__":

    time.sleep(1)
    hit('space')
    while True:
        # time.sleep(0.3)
        image = takeScreenshot()
        data = image.load()
        isCollide(data)

    #########################################
        # This part is used for demo drawing
    #########################################

    # image = takeScreenshot()
    # data = image.load()
    # # cactus detection
    # for i in range(490, 510):
    #     for j in range(260, 270):
    #         data[i, j] = 180

    # # bird detection
    # for i in range(490, 510):
    #     for j in range(220, 250):
    #         data[i, j] = 0
    
    # image.show()