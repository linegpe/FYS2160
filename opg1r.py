from math import log, factorial

N = 50
Sp = 25
k = 1.38*10**(-23)

S = k*(log(factorial(N)) - log(factorial(Sp)) - log(factorial(N-Sp)))

print "The entropy of the system is " + str(S)