import cv2
import numpy as np
import binLibrary
import re


def changePhoto(stringFileName, stringCode, nameCodedFile):
    image = cv2.imread(stringFileName)
    # if(image==None): 
    #     print("the file does not exist")
    #     sys.exit(0)
    try:
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
    except:
        print('\033[91m',"the files selected are either not images or do not exist", '\033[0m')  
        return 
# changePhoto("AUT_HotChocolate.bmp", "helloThereBaby", "codedFile.bmp")
    #works with bmp -> bmp
# changePhoto("spring.jpg", "helloThereBaby im hereeee but you cant see me", "codedFile.jpg")
    #does not work with jpg -> jpg
# changePhoto("AUT_HotChocolate.png", "hello There Baby", "codedFile.png")
    #works with png -> png

                
def changePhotoFile(stringFileName, fileCodeHolder, nameCodedFile):
    fileCode = open(fileCodeHolder, "rb")
    stringCode = str(fileCode.read(), 'utf-8')
    changePhoto(stringFileName, stringCode, nameCodedFile)
    
# changePhotoFile("spring.jpg", "C:\\Users\\venus\\Desktop\\aut_hotcholocate\\New folder\\allin1.txt", "springCoded.jpg")

def get_char_count(s):
    return len(re.findall(r'\S', s))

# print(get_char_count(""))