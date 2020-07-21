import cv2
import numpy as np
import binLibrary



def changePhoto(stringFileName, stringCode, nameCodedFile):
    image = cv2.imread(stringFileName)
    # if(image==None):
    #     print("the file does not exist")
    #     sys.exit(0)
    heigh, width, color = image.shape
    if(heigh*width*3<len(stringCode)*8):
        print("the image is too small")
        return
    codeList = binLibrary.stringToBin(stringCode)
    index = 0 
    # in this type of iterating the index 0 is blue 
    # 1 is green and 2 is red thats why the last for is 
    # reverse 
    for i in range(heigh):
        for j in range(width):
            c = 2
            while(c>=0):
                # print(image[i,j,c])
                binaryColor = binLibrary.numtoBin(image[i,j,c])
                # binaryColor is a list with 8 elements(the color in binary mode)
                if(binaryColor[7]!=codeList[index]):
                    # print(i,j,c,"  ", binaryColor[7],"!=" , codeList[index])
                    binaryColor[7]=codeList[index]
                    image[i,j,c]= binLibrary.binToNum(binaryColor)
                index+=1
                c-=1
                if(index==len(codeList)):
                    cv2.imwrite(nameCodedFile, image)
                    return
# changePhoto("AUT_HotChocolate.bmp", "helloThereBaby", "codedFile.jpg")

                

