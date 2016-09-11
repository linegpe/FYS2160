# Task 1c, Oblig 1
# Calculate the number of microstates as a function of qA, NA and NB 

from math import factorial
from numpy import zeros

qTot = 6 # Total enery in the whole system
NA = 2 # Number of oscillators in subsystem A
NB = 2 # Number of oscillators in subsystem B
micro = 0 # Total number of microstates
OmegaTot = zeros(qTot+1)

# Pint number of microstates for each macrostate qA:
print 'Number of microstates for each macrostate qA:'
for qA in range(0,qTot+1):
	qB = qTot - qA # Total energy in subsystem B
	OmegaA = factorial(qA + NA - 1)/(factorial(qA)*factorial(NA-1))
	OmegaB = factorial(qB + NB - 1)/(factorial(qB)*factorial(NB-1))
	OmegaTot[qA] = OmegaA * OmegaB
	print ('qA = '+ str(qA) + ': ' +str(OmegaTot[qA]))
	micro += OmegaTot[qA]
print 'The complete number of microstates is ' + str(micro)
print 'If we assume each microstate is equally probable, then the probability for each macrostate is'

# Make sure the sum of all probabilities is 1:
check = 0
for qA in range(0,qTot+1):
	p = OmegaTot[qA]/float(micro)
	check += p
	print ('qA = '+ str(qA) + ': P(qA) = ' + str(p))
print 'The sum of all the probabilities should be 1. We have:'
print check
