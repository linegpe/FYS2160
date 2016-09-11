from numpy import zeros
from math import factorial
import matplotlib.pyplot as plt 

NA = 50
NB = 50
qTot = 100
OmegaTot = zeros(qTot+1)
qAvec = zeros(qTot+1)
micro = 0

# Calculate the probability for each macrostate qA
for qA in range(0,qTot+1):
	qB = qTot - qA # Total energy in subsystem B
	OmegaA = factorial(qA + NA - 1)/(factorial(qA)*factorial(NA-1))
	OmegaB = factorial(qB + NB - 1)/(factorial(qB)*factorial(NB-1))
	OmegaTot[qA] = OmegaA * OmegaB
	qAvec[qA] = qA
	micro += OmegaTot[qA]
print 'The total number of microstates is ' + str(micro)

# Make sure the sum of all probabilities is 1:
check = 0
p = zeros(qTot+1)
for qA in range(0,qTot+1):
	p[qA] = float(OmegaTot[qA])/float(micro)
	check += p[qA]
eps = 0.1 
if 1-eps < check < 1+eps:
	print 'The sum of all probabilities is ' + str(check)
else:
	print 'Something went wrong. The sum of all probabilities is ' + str(check)

# Most probable macrostate:
print 'The most probable macrostate is qA = ' + str(qAvec[p.argmax()]) + ', with probability ' + str(max(p))

# Plotting the probability P(qA)
font = {'size'   : 18}
plt.rc('font', **font)
plt.plot(qAvec,p,linewidth=2.0)
plt.xlabel('qA')
plt.ylabel('P(qA)')
plt.show()