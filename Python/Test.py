try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from time import sleep
import requests
import pyscreenshot as ImageGrab


gameHealthBounds1 = (775,930,818,953)
testHealthBounds1 = ()
print("Started")


# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
#print(pytesseract.image_to_string(Image.open('Screenshot_1.png'), config='--psm 8'))


#-- include('examples/showgrabbox.py')--#

def bringThePain():

    print ("SHOTS FIRED")
    # url = 'http://192.168.1.28'
    # payload = {'key1': 'value1', 'key2': 'value2'}

    # # GET
    # r = requests.get(url+'/ledOn')

    # sleep(0.15)

    # r = requests.get(url+'/ledOff')



if __name__ == "__main__":
    # part of the screen

    health = 100
    strHealth = ''

    while(True):
        im=ImageGrab.grab(bbox=gameHealthBounds1) # X1,Y1,X2,Y2
        # im.show()
        strhealth = pytesseract.image_to_string(im, config='--psm 8')
        
        #strHealth = pytesseract.image_to_string(Image.open('Screenshot_1.png'), config='--psm 8')
        try:
            tempHealth = int(float(strHealth))
            if(health >tempHealth): #Damage Taken
                bringThePain()
                print("Ouch, health went from: "+ health + " to " + tempHealth)

            health = tempHealth
        except ValueError:
            print("none detected")
            sleep(.1)
        
#-#