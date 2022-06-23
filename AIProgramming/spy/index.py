from asyncore import read, write


originFile=None
encryption=None

originFile=open('origin.txt','r',encoding="UTF-8")
encryption=open('encryption.txt','w',encoding="UTF-8")
origin_str = originFile.readline()

for i in origin_str:
    aa = ord(i) + 100
    bb = chr(aa) 
    encryption.write(bb)

originFile.close()
encryption.close()
