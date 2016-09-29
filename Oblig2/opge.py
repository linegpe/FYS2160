import numpy as np
import matplotlib.pyplot as plt

N = 100 	# Data points
k = 1 		# Boltzmann's constant
theta = 1
Z = np.zeros(N)
epsilon = np.zeros(N)
j = np.linspace(0,20,N)

T_values = 0.1, 10, 100, 1000

for T in T_values:
	for i in range(0,N):
		epsilon[i] = i*(i+1)*theta*k
		Z[i] = (2*j[i] - j[i])*np.exp(-epsilon[i]/(k*T))
	plt.hold = 'on'
	plt.plot(j,Z,'--',label=('T = ' + str(T)))
plt.legend()
plt.xlabel('$j$')
plt.ylabel('$Z_R(T)$')
plt.show()
plt.hold = 'off'