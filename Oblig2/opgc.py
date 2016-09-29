import numpy as np
import matplotlib.pyplot as plt

Tmax = 20 		# Highest temperature
N = 100 		# Number of data points
epsilon = 1 	# Energy unit
k = 1 			# Boltzmann's constant
T = np.linspace(1,Tmax,N)

def c_v(T):
	return(3*epsilon*np.exp(-epsilon/(k*T)))/(k*T**2*(1+3*np.exp(-epsilon/(k*T)))**2)

plt.plot(T,c_v(T))
plt.xlabel('Temperature')
plt.ylabel('Heat capacity')
plt.show()