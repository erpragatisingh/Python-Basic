print ("\n==========================\n")

import zlib, base64
text = b'STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW '
code =  base64.b64encode(zlib.compress(text,9))
print (code)


import zlib, base64
s='eNoLDnF09lbwD3MNcvPxD1cIHhxcAE9UKaU='
data = zlib.decompress(base64.b64decode(s))
print (data)




print ("\n==========================\n")

import tarfile
text = b'STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW STACK OVERFLOW '
code =  tarfile.stn(text)
print (code)




