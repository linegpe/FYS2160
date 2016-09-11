a = 2
b = 3
c = a + b
d = a - b
f = open('writeresulttofile.txt','w')
f.write(str(c) + '\n')
f.write(str(d))
f.close()