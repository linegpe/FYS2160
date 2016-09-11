from random import randint
from numpy import zeros, histogram, linspace, exp
import matplotlib.pyplot as plt

N = 50
M = 10000
M_values = zeros(M)
Omega0 = 1100
Omega = zeros(M)

# Create random integers and make s = +/- 1
# Store final values in array M_values
print "Looping..."
for j in range(0,M):
	i = 0
	s = 0
	while i < N+1:
		rand = randint(0,1)
		i += 1
		if rand == 1:
			s += 1
		elif rand == 0:
			s -= 1
		else:
			print 'Error: random integer not 1 or 0'
	M_values[j] = s
print 'Done!' # It might take some time to run
M_values = - M_values

x = linspace(-30,30,M)
print 'Second loop...'
for n in range(0,M):
	Omega[n] = exp((-2*x[n]**2)/(4*N))*Omega0
#print len(x)
#print len(Omega)
#print Omega


# Histogram and plot
b = linspace(-29,30,60)-0.5 
font = {'size'   : 18}
plt.rc('font', **font)
plt.plot(x,Omega,linewidth=2)
plt.hist(M_values, bins = b)
plt.xlabel('Energy [$\mu$B]')
plt.ylabel('Counts')
plt.show()