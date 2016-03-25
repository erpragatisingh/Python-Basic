"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
import webbrowser
import time

total_break=3
break_count=0

new = 2 # open in a new tab, if possible
print("This program started at "+time.ctime())

while(break_count<total_break):
# open a public URL, in this case, the webbrowser docs
     url = "http://docs.python.org/library/webbrowser.html"
     songURL="https://www.youtube.com/watch?v=jOYR3k1VhUQ"
     webbrowser.open(url,new=new)
     time.sleep(10)
     webbrowser.open(songURL,new=new)
     break_count=break_count+1
# open an HTML file on my own (Windows) computer
#url = "file://X:/MiscDev/language_links.html"
#webbrowser.open(url,new=new)
