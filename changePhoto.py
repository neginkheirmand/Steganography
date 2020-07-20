import cv2
import numpy as np
import binLibrary

def changePhoto(stringFileName, stringCode):
    image = cv2.imread(stringFileName)
    heigh, width, color = image.shape
    codeList = binLibrary.stringToBin(stringCode)
    index = 0 
    for i in range(heigh):
        for j in range(width):
            for c in range(color):
                
                

