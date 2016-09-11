# Testing symbolic python 
from sympy import *

u = symbols('u')
N = symbols('N')
lnP = N*log(N)-((N/2)-u)
series(lnP,u,n=3)