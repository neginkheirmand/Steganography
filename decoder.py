import cv2

def decoder(nameSecundary, namePrimmary):
    image1 = cv2.imread(namePrimmary)
    image1 = cv2.imread(nameSecundary)
    heigh1, width2, width1, color1 = image1.shape
    heigh2, width2, color2 = image2.shape

    if(width1 != width2 or heigh1 != heigh2 or color1!=color2 ):
        print("the photoes are not equal")
        return
    for h in range(heigh1):
        for w in range(width1):
            c=2
            while(c>=0):
                diff = image1[h, w, c] - image2[h, w, c]
                print("%d" % diff)
                c-=1
    