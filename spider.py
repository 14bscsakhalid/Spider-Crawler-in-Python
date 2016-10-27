import os
from os import walk

myPath = "F:/work"

myFiles = {}
myDirs = {}
keyWords = {}

for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):
            filepath = os.path.join(root, file)
            filename = os.path.basename(filepath)
	    myFiles[filename] = []
            myFiles[filename].append(filepath)
#print(myFiles)
#print(myDirs)

for subdir, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):
            f=open(subdir+'/'+ file,'r')
	    for line in f:
		for word in line.split():	    
		    filepath = os.path.join(root, file)
		    filename = os.path.basename(filepath)	    
		    keyWords[word] = []
		    keyWords[word].append(filepath)
#print keyWords

var = raw_input("Enter a keyword: ")
if var not in keyWords.keys():
	print("No keyword in any text file")

else:
	for paths in keyWords[var]:
		print(paths)
	for files in myFiles[var]:
	    print files
