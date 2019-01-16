from matplotlib import pyplot as mpl
import numpy as np

X = []
for i in range(10):
    X.append(i)

mpl.plot(X,X,'-r')
mpl.show()