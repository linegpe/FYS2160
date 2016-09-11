from sympy import *

q = symbols('q')
N = symbols('N')

#lnOmega = (q+N-1)*log(q+N-1) - q*log(q) - (N-1)*log(N-1)
#lnOmega = (q+N-1)*log(q+N) - q*log(q) - (N-1)*log(N)
#lnOmega = (q+N)*log(q+N-1) - q*log(q) - N*log(N-1)
lnOmega = (q+N)*log(q+N) - q*log(q) - N*log(N)

expansion = series(lnOmega,q,n=2)
print expansion