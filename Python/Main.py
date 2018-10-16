from HealthOCR import getHealth
from time import sleep
import requests

print("Starting")


currentHealth = 100


while(True):
    tempHealth = getHealth()
    print (tempHealth)
    if(tempHealth>-1):
        print( tempHealth)
