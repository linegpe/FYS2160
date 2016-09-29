import matplotlib.pyplot as plt
import numpy as np

Tmin = 1
Tmax = 100
N = 10
theta = 50
maxj = 10

Tvalues = np.linspace(Tmin,Tmax,N)
Z = np.zeros(N)
Zvalues = np.zeros(N)

def Zfunction():
	z = 0
	for j in range(0,maxj):
		z += (2*j+j)*np.exp(-j*(j+1)*theta/T)
	return z

for i in range(0,N):
	

plt.plot(T,Z)
plt.xlabel(r"Temperatures $T$")
plt.ylabel(r'$Z$')
plt.show()