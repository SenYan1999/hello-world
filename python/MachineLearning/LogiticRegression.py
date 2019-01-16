from matplotlib import pyplot as plt
import numpy as np
import scipy.optimize as opt
import os


def plotData(X, y):
    
    for i in range(0, np.size(y)):
        if y[i] == 1:
            plt.scatter(X[i, 0], X[i, 1], c='r', marker='x')
        
        else:
            plt.scatter(X[i, 0], X[i, 1], c='g', marker='o')


def sigmoid(X):

    return 1 / (1 + np.exp(-X))


def costFunction(theta, X, y):

    m = np.size(y)

    cost = -(1/m) * np.sum(y * np.log(sigmoid(X@theta)) + (1 - y) * np.log(1 - sigmoid(X@theta)))

    return cost


def gradient(theta, X, y):

    m = np.size(y)

    grad = (1/m) * np.sum((sigmoid(X@theta) - y) * X, 0)

    return np.array([grad])


def predict(X, theta):

    X = np.insert(X, 0, 1, axis=1)

    p = 1 if sigmoid(X@theta) >= 0.5 else 0

    return p


if __name__ == '__main__':
    
    # Load the data
    os.chdir('/home/mike/python/MachineLearning/')

    data = np.loadtxt('ex2data1.txt', dtype=float, delimiter=',')
    X, y = data[:, 0:2], np.array([data[:, 2]]).T

    # Visualize the data
    plt.figure()
    plotData(X, y)
    plt.xlabel = 'Exam 1 score'
    plt.ylabel = 'Exam 2 score'
    plt.legend('Admitted', 'Not admitted')
    plt.show()

    # Initialize the theta and predo the X
    X = np.insert(X, 0, 1, axis=1)
    init_theta = np.zeros((X.shape[1], 1))

    # Test cost function
    cost = costFunction(init_theta, X, y)
    grad = gradient(init_theta, X, y)

    print('Cost at initial theta(zeros) is: %.3f' % cost)
    print('Expected cost(approx) is: 0.693')
    print('Gradint at initial theta(zeros) is:')
    print(grad)
    print('Expected gradients (approx):\n-0.1000\n -12.0092\n -11.2628\n')

    # Use the scipy built in function to find the optimized theta
    theta = opt.minimize(costFunction, init_theta, (X,y), jac=gradient)
    print('theta is:')
    print(theta)
    
    # Predict some values
    my_X = np.array([45, 80])
    p = predict(my_X, theta)
    print('Predic score with 45 in exam 1 and 80 in exam 2 is:')
    print('Admitted!' if p == 1 else 'Not admitted!')