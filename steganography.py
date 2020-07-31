import os
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
        filename, file_extension = os.path.splitext(encodedFile)
        filename1, file_extension1 = os.path.splitext(primmaryFile)
        if((file_extension1 != ".png " and file_extension1!=".bmp") or (file_extension!=file_extension1) ):
            print("the extension of the files or either not equal or not supported")
            return
        print("encrypted message in encryptedMessage.txt")
        decoder.decoder(encodedFile, primmaryFile)
    elif(string == "2" or string == "2)" or string == "encrypt" or string == "2)encrypt"):
        print("enter the name of the file you want to encrypt or its absolute path")
        fileToEncrypt = input()
        filename, file_extension = os.path.splitext(fileToEncrypt)
        if(file_extension != ".png " and file_extension!=".bmp"):
            print("only .png and .bmp types are supported")
            return
        print("enter the name of the output file")
        codeFile = input()
        filename1, file_extension1 = os.path.splitext(codeFile)
        if( file_extension1 != file_extension):
            file_extension1=file_extension
        print("enter the message")
        code = input()
        changePhoto.changePhoto(fileToEncrypt, code, filename1+file_extension1)


steg()