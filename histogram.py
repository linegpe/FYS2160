import numpy as np
import matplotlib.pyplot as plt
b = np.linspace(1,10,10)-0.5
print b

a = [1,4,2,6,3,6,3,5,5,3,5,2,5,3,5,6,7,8,9,9,7,6,7,4,6,3]

plt.hist(a, bins = b, width = 1)
plt.xlabel('Value')
plt.ylabel('Counts')
plt.show()