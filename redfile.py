import urllib.request
def read_text():
    quats=open("/Users/pragati/Documents/python/openbrowser.py")
    contentof_file=quats.read()
    print(contentof_file)
    check_text_ifexist(contentof_file)
    quats.close()


def check_text_ifexist(textforcheck):

response = urllib.request.urlopen('http://www.wdyl.com/profanity?q='+textforcheck)
html = response.read()
read_text()   

