import cv2
import changePhoto
import decoder

def steg():
    print("do you want to \n1)decode or 2)encrypt ?")
    string = input()
    if(string == "1" or string == "1)" or string == "decode" or string == "1)decode"):
        print("enter the name of the file encrypted")
        encodedFile = input()
        print("enter the name of the primmary file")
        primmaryFile = input()
        print("how much of the image you want to search in?")
        amount=input("1)all 2)1/2 3)1/3 4)1/4")
        print(decoder.decoder(encodedFile, primmaryFile))
    elif(string == "2" or string == "2)" or string == "encrypt" or string == "2)encrypt"):
        print("enter the name of the file you want to encrypt")
        fileToEncrypt = input()
        print("enter the name of the output file")
        codeFile = input()
        print("enter the message")
        code = input()
        changePhoto.changePhoto(fileToEncrypt, code, codeFile)


steg()