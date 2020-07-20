import cv2
import binLibrary


def decoder(nameSecundary, namePrimmary):
    image1 = cv2.imread(namePrimmary)
    image2 = cv2.imread(nameSecundary)
    heigh1, width1, color1 = image1.shape
    heigh2, width2, color2 = image2.shape


    if(width1 != width2 or heigh1 != heigh2 or color1!=color2 ):
        print("the photoes are not equal")
        return

    maxNumber = 100
    codedList = []
    for h in range(heigh1):
        for w in range(width1):
            c=2
            while(c>=0):
                diff = image2[h, w, c] - image1[h, w, c]
                if(diff == 0):
                    codedList.append(binLibrary.numtoBin(image2[h,w,c])[7])                    
                # print("the first image ", image1[h,w,c], "   the second image ", image2[h,w,c], "  the difference= " ,diff)
                elif(diff==-1):
                    codedList.append(0)
                elif(diff==1):
                    codedList.append(1)

                if((h+1)*(w+1)*(3-c)>maxNumber):
                    print(codedList)
                    return binLibrary.binToStr(codedList)
                c-=1
    

print(decoder("codedImage1.bmp", "AUT_HotChocolate.bmp"))
    