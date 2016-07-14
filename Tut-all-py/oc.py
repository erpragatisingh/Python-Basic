http://www.openbookproject.net/py4fun/
Python for Fun - Open Book Project
www.openbookproject.net
Purpose of this Collection. This collection is a presentation of several small Python programs. They are aimed at intermediate programmers; people who have studied ...
 
1.       Find current working dir:
import os
os.getcwd()
 
2.       Change current working dir:
Import os
os.chdir(‘path’)
os.getcwd()
 
 
Path format:
C://Users//gur32384//Desktop
 
 
3.       Create a new file
file=open(“name.txt”,”w+”)

4.       Word count
 
#!/usr/bin/python
##file=open("D:\\zzzz\\names2.txt","r+")
##file=open("E:\ALU\NETAP00051145\patch\fullscenario\5SwitchAndProfit_sep.128.tra","r+")
file=open("ol.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();
 
 
import file name
