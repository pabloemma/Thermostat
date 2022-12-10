
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np






t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^',t,t**3.2,'b+')
plt.show()


