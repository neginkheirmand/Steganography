import os

for filename in os.listdir("C:\\Users\\venus\\Desktop\\documentation"):
    if filename.endswith(".txt") : 
        #  print(os.path.join(directory, filename))
        print(filename)
        continue
    else:
        print("not a .txt file")
        