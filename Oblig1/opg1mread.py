from numpy import zeros, array

f = open('nyfil.txt','r')
lines = f.readlines()
val = []
for line in lines:
	val.append(float(line))

f.close()

M = 10000
val = array(val)
print sum(val)/M


