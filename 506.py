def getunicode(key):
    return hex(ord(key))

dict = {}

carstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

for key in carstring:
    unival = getunicode(key) 
    dict[key] = unival

print dict.values()
