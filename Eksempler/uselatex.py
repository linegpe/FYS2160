import numpy as np 
import matplotlib.pyplot as plt

alpha = np.linspace(0,10)
beta = alpha**2

plt.plot(alpha,beta)
plt.xlabel('Alpha $\alpha$')
plt.ylabel('Beta $\beta$')
plt.show()