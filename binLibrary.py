def numtoBin ( number ):
    list = []
    i=0
    while(number!=0):
        list.append(number%2)
        number = int(number/2)
        i+=1
   
    j=len(list)-1
    newList = []
    numZeroAtStart = 8-len(list)
    if(numZeroAtStart>0):
        for x in range(numZeroAtStart):
            newList.append(0)
    
    while(j>=0):
        newList.append(list[j])
        j-=1
    return newList

def binToNum(binList):
    number =0
    i = 0
    while(i<len(binList)):
        number+=binList[i]*(pow(2, len(binList)-1-i))
        i+=1
    return number



def stringToBin(string):
    textList=[]
    i=0
    # for char in string:
    while(i<len(string)):
        textNum=ord(string[i])
        textList+=numtoBin(textNum)
        i+=1
    return textList


def binToStr(binList):
    i = 8
    string = ""
    while(i<=len(binList)):
        string+=chr(binToNum(binList[i-8:i]))
        i+=8
    return string