import cv2
import numpy as np
import binLibrary

def changePhoto(stringFileName, stringCode):
    image = cv2.imread(stringFileName)
    heigh, width, color = image.shape
    codeList = binLibrary.stringToBin(stringCode)
    index = 0 
    # in this type of iterating the index 0 is blue 
    # 1 is green and 2 is red thats why the last for is 
    # reverse 
    for i in range(heigh):
        for j in range(width):
            c= 2
            while(c>=0):
                binaryColor = binLibrary.letterCounter(image[i,j,c])
                if(binaryColor[7]==codeList)

                

