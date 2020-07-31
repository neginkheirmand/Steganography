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
        timesRepeted =0
        for h in range(heigh1):
            for w in range(width1):
                c=2
                while(c>=0):
                    diff = image2[h, w, c] - image1[h, w, c]
                    if(diff == 0):
                        zeroRepeted+=1
                        codedList.append((binLibrary.numtoBin(image2[h,w,c]))[7])                  
                    elif(diff==-1 or diff==255):
                        codedList.append(0)
                        zeroRepeted=0
                    elif(diff==1):
                        codedList.append(1)
                        zeroRepeted=0
                    if ( len(codedList) == 8 ):
                        if( zeroRepeted == 8 ):
                            timesRepeted+=1
                            if(timesRepeted==2):
                                fo.flush()
                                fo.close()
                                return
                        fo.write(binLibrary.binToStr(codedList))
                        fo.flush()
                        codedList=[]
                        zeroRepeted=0
                    c-=1
    except:
        print('\033[91m',"the files selected are either not images or do not exist", '\033[0m')  
        return