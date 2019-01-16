import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt


def sigmoid(X):
    return (1/(1+np.exp(X)))


if __name__ == '__main__':

    A = np.arange(10)

    plt.plot(A,sigmoid(A))