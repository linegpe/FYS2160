from random import randint
from numpy import zeros, histogram, linspace
import matplotlib.pyplot as plt

N = 50
M = 10000
M_values = zeros(M)

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
# Fun loop to check the average value:
sums = 0
for i in range(0,M):
	sums += M_values[i]
print "Avegare value: " + str(sums/M)

# Making a histogram
b = linspace(-29,30,60)-0.5 # Make it beautiful
font = {'size'   : 18}
plt.rc('font', **font)
plt.hist(M_values, bins = b)
plt.xlabel('Energy [$\mu$B]')
plt.ylabel('Counts')
plt.show()