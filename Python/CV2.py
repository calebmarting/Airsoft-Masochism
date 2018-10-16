import numpy as np
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from time import sleep
import requests
import pyscreenshot as ImageGrab



def damageTaken():
    print ("You don screwed up")
    url = 'http://192.168.1.28'
    payload = {'key1': 'value1', 'key2': 'value2'}

    # GET
    r = requests.get(url+'/ledOn')

    sleep(0.15)

    r = requests.get(url+'/ledOff')

def main():
    currentHealth = 100
    while(True):
        # Load an color image in grayscale
        #img = cv2.imread('Screenshot_1.png',0)
        img2 = ImageGrab.grab(bbox=gameHealthBounds1)
        img = np.array(img2)
        _, img = cv2.threshold(img,250,255,cv2.THRESH_BINARY)
        img =cv2.bitwise_not(img)
        # cv2.imshow('image',img)
        # img = np.array(img)
        strRead = pytesseract.image_to_string(img, config='--psm 6')
        try:
            health = float(strRead)
            if(health != currentHealth):
                delta = (health-currentHealth)
                print("Health Delta "+ str(delta))
            if(health < currentHealth):
                damageTaken()
            currentHealth = health
        except ValueError:
            if(strRead.find("a")!=-1):
                health = 0
            else:
                print ("could not convert " + strRead)



if __name__ == "__main__":
    print("Start")

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    gameHealthBounds1 = (775,930,818,953)
    main()

        # print(pytesseract.image_to_string(img, config='--psm 6'))


    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
