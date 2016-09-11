from pylab import*
N = 10 # Number of elements
k = 100000
kx = 1000000 # Spring constant
d = 0.1 # Size in m
m = 0.1 # Mass in kg
t = 20.0 # Simulation time
g = 9.81 # m/s 
z0 = 0.1 # Initial hight
dt = 0.00001 # Timesteps
nstep = ceil(t/dt)
z = zeros((N,nstep),float)
vz = zeros((N,nstep),float)
z[:,0] = d*(array(range(N)))/N + z0 # Initail position
l = d/N # Distance between nodes
for i in range(nstep): # Calculate motion
	dz = diff(z[:,i])-1
	F = -k*append(0.0,dz) + k*append(dz,0.0) - m*g # Internode
	F[0] = F[0] - kw*z[0,i]*(z[0,i]<0) # Bottom wall
	a = F/m
	vz[:,i+1] = vz[:,i] + a*dt 
	z[:,i+1] = z[:,i] + vz[:,i+1]*dt 