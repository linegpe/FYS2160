import matplotlib.pyplot as plt
import numpy as np

T = 100
theta = 5
maxj = 10
Z = 0
epsilon = 10**(-6)
print epsilon
N = 100000 # Let it go to infinity
z = 1

Z = np.linspace(0,N,N)
jvalues = np.linspace(0,N,N)


# for j in range(1,N):
# 	sumz = epsilon
# 	while sumz > epsilon:		
# 		z = (2*j+j)*np.exp(-j*(j+1)*theta/T)
# 		sumz += z
# 	Z[j] = sumz

j = 1
sumz = 1

while sumz > epsilon:
	for i in range(0,N):
		#print "i = " + str(i)
		sumz = 0
		z = 1
		while z > epsilon:
			#print "j = " + str(j)
			z = (2*j+j)*np.exp(-j*(j+1)*theta/T)
			sumz += z 
			j += 1
		Z[i] = sumz

		

plt.plot(jvalues, Z)
plt.show()