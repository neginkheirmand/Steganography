import cv2
import binLibrary


def decoder(nameSecundary, namePrimmary):
    image1 = cv2.imread(namePrimmary)
    image2 = cv2.imread(nameSecundary)
    try:
        heigh1, width1, color1 = image1.shape
        heigh2, width2, color2 = image2.shape

        if(width1 != width2 or heigh1 != heigh2 or color1!=color2 ):
            print("the images are not equal")
            return

        fo = open("encryptedMessage.txt", "w")
        codedList = []
        zeroRepeted=0
        for h in range(heigh1):
            for w in range(width1):
                c=2
                while(c>=0):
                    diff = image2[h, w, c] - image1[h, w, c]
                    print(zeroRepeted)
                    if(diff == 0):
                        zeroRepeted+=1
                        # print(0)
                        # if(zeroRepeted==8):
                        #     print("should end?")
                        codedList.append((binLibrary.numtoBin(image2[h,w,c]))[7])                  
                    elif(diff==-1 or diff==255):
                        codedList.append(0)
                        zeroRepeted=0
                        # print(1)
                    elif(diff==1):
                        codedList.append(1)
                        zeroRepeted=0
                        # print(1)
                    if(len(codedList) == 8):
                        fo.flush()
                        if( zeroRepeted == 8):
                            print('\033[91m', zeroRepeted)
                            print("here")
                            fo.close()
                            return
                        fo.write(binLibrary.binToStr(codedList))
                        codedList=[]
                        # print(1)
                        zeroRepeted=0
                    c-=1
    except:
        print('\033[91m',"the files selected are either not images or do not exist", '\033[0m')  
        return   

# print(decoder("codedFile.jpg", "spring.jpg"))
# print(decoder("codedFile.bmp", "AUT_HotChocolate.bmp"))
# print(decoder("springCoded.bmp", "spring.bmp"))
decoder("springCoded.bmp", "spring.bmp")