try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from time import sleep
import requests
import pyscreenshot as ImageGrab


gameHealthBounds1 = (775,930,818,953)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


# def getHealth():
#     strHealth = ' '
#     if True: #__name__ == "__main__":
        
#         im=ImageGrab.grab(bbox=gameHealthBounds1) # X1,Y1,X2,Y2
#             # im.show()
#         #strhealth = pytesseract.image_to_string(im, config='--psm 8')
        
#         strHealth = pytesseract.image_to_string(Image.open('Screenshot_1.png'), config='--psm 8')
#         print(str)
#         try:
#             return int(float(strHealth))

#         except ValueError:
#             return -1
#     return -2

if __name__ == "__main__":
    # part of the screen

    health = 100


    # im=ImageGrab.grab(bbox=gameHealthBounds1).convert('LA').point(lambda p: p > 200 and 255) # X1,Y1,X2,Y2
    # im.show()
    # strhealth = pytesseract.image_to_string(im)
    # print(strhealth)
    print (pytesseract.image_to_string(Image.open('Screenshot_1.png').convert('LA'), config='--psm 8'))
    print (pytesseract.image_to_string(Image.open('Screenshot_2.png').convert('LA'), config='--psm 8'))
    print (pytesseract.image_to_string(Image.open('Screenshot_3.png').convert('LA'), config='--psm 8'))

    im = pytesseract.image_to_string(Image.open('Screenshot_1.png').convert('LA')
    # print (pytesseract.image_to_string(Image.open('Screenshot_1.png'), config='--psm 8'))
    # try:
    #     tempHealth = float(strHealth)
    #     if(health >tempHealth): #Damage Taken
    #         # bringThePain()
    #         print("Ouch, health went from: "+ health + " to " + tempHealth)

    #         health = tempHealth
    # except ValueError:
    #     print("none detected")

        
#-#