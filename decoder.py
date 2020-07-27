import cv2
import binLibrary


def decoder(nameSecundary, namePrimmary):
    image1 = cv2.imread(namePrimmary)
    image2 = cv2.imread(nameSecundary)
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
                # print(binLibrary.numtoBin( image2[h,w,c]) ,binLibrary.numtoBin( image1[h,w,c]))
                diff = image2[h, w, c] - image1[h, w, c]
                # print("the first image ", image1[h,w,c], "   the second image ", image2[h,w,c], "  the difference= " ,diff)
                if(diff == 0):
                    zeroRepeted+=1
                    codedList.append((binLibrary.numtoBin(image2[h,w,c]))[7])  
                    if(zeroRepeted==14):
                        codedList[len(codedList)-8:len(codedList)] = []
                        fo.close()
                        return binLibrary.binToStr(codedList)                  
                elif(diff==-1 or diff==255):
                    codedList.append(0)
                    zeroRepeted=0
                elif(diff==1):
                    codedList.append(1)
                    zeroRepeted=0
                c-=1
    

print(decoder("codedFile.jpg", "spring.jpg"))