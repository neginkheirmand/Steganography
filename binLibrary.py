
'''
this scrypt should take in a number and give a list of that number in binary mode
'''
def letterCounter ( number ):
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

# print(ord('h'))
# print(letterCounter(104))

def stringToBin(string):
    textList=[]
    i=0
    # for char in string:
    while(i<len(string)):
        if(string[i] == ' '):
            textList.append("*")
        else:
            textNum=ord(string[i])
            textList+=letterCounter(textNum)
        i+=1
    
    strin=""

    for j in range(len(textList)):
        # print("---", textList[j])
        if(textList[j]=="*"):
            # print(strin)
            strin= ""
        else:
            strin+=str(textList[j])

    # print(strin)
    return textList


# stringToBin("U_R0CK")
stringToBin("_B3_zuD_3HS4S_behtarE_KH4hEd_kard")