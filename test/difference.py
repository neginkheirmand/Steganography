#this scrypt should see if there are is difference between the images "AUT_HotChocolate.bmp" and "HotChocolateWithTasteOfCode.bmp" 
#and color them red in the output file, if there was no difference in a pixel should leave it as it is

import cv2

def difference(primmary, secundary):
    image1 =cv2.imread(primmary)
    image2 =cv2.imread(secundary)
    heigh, width, color = image1.shape
    equal=0
    for h in range(heigh):
        for w in range(width):
            if(image1[h,w,0]==image2[h,w,0] and image1[h,w,1]==image2[h,w,1] and image1[h,w,2]==image2[h,w,2]):
                image2[h,w]=[0,0,255]
                equal+=1
                if(equal==14):
                    cv2.imwrite("difference.bmp", image2)
                    return
            else:
                equal=0
    cv2.imwrite( "difference.bmp",image2)
    return

difference("AUT_HotChocolate.bmp", "HotChocolateWithTasteOfCode.bmp")

