# This program is a simple model to study how atoms move in a box when they all start out at the same side

from pylab import *
N = 210 # Number of particles
nstep = 4000 # Number of timesteps
n = zeros(nstep)
n[0] = 210 # Initial number of particles to the left
for i in range(1,nstep):
	r = rand(1)
	if (r<n[i-1]/N):
		n[i] = n[i-1] - 1 # Move atom from left to right
	else:
		n[i] = n[i-1] + 1 # Move atom from right to left
plot(range(0,nstep),n/N)
xlabel('t'),ylabel('n/N')
show()