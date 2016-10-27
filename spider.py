import os
from os import walk

myPath = "F:/work"

myFiles = []
myDirs = []
keyWords = []

for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):
            filepath = os.path.join(root, file)
            filename = os.path.basename(filepath)
            myDirs.append(os.path.dirname(filepath))
            myFiles.append(filename)
print(myFiles)
print(myDirs)

for subdir, dirs, files in os.walk(myPath):
    for file in files:
            f=open(subdir+'/'+ file,'r')
            lines = f.readlines()
            keyWords.append(lines)
            f.close()
print keyWords

