import matplotlib.pyplot as plt
import numpy as np
import os

def CostFunction(X, y, theta):

    # To compute the cost of the given theta in linear regression

    predictions = X @ theta

    m = y.size

    cost = (0.5/m) * ((predictions - y)**2).sum()
    
    return cost

def FeatureNormalized(X):

    # To mean normalize the features of X

    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    X = (X - mean) / std 

    return X


def GradientDescent(X, y, theta, alpha, iter):

    # Linear regression using gradient descent

    m = X.shape[0]
    J_history = np.zeros((iter, 1))

    for i in range(0, iter):
        
        J_history[i] = int(CostFunction(X, y, theta))

        theta = theta - (1/m) * alpha * np.array([(((X @ theta - np.array([y]).T) * X).sum(axis=0))]).T
    
    return [theta, J_history]

def NormalEquation(X, y):

    # Linear regression using normal equation

    m = X.shape(X)
    theta = np.zeros(m,1)

    theta = np.linalg.pinv(X.T @ X) @ X.T @ np.array([y]).T

    return theta

if __name__ == '__main__':

    # Test the Linear Regression

    # Load the data set

    os.chdir('/home/mike/python/MachineLearning')
    X = np.loadtxt('ex1data2.txt', delimiter=',', usecols=(0, 1))
    y = np.loadtxt('ex1data2.txt', delimiter=',', usecols=2)
    y.reshape(np.size(y), 1)

    # Data normalize

    # X = FeatureNormalized(X)
    X = np.insert(X, 0, np.ones(np.size(X, axis=0)), axis=1)

    # Set the alpha and iteration number

    alpha, iter_num = 0.01, 400
    theta = np.zeros((X.shape[1], 1))

    # Run Gradient Descent
    [theta, J_history] = GradientDescent(X, y, theta, alpha, iter_num)

    # Vector Visualization
    J_x = np.arange(iter_num)

    plt.plot(J_x, J_history, '-r')
    plt.xlabel('Iteration numbers')
    plt.ylabel('Cost')
    plt.title('Relationship when Iteration goes with cost')
    plt.show()

    # Prediction
    
    X_1 = np.array([[1650,3]])
    X_1 = FeatureNormalized(X_1)
    X_1 = np.insert(X_1, 0, 1, axis=1)

    price1 = X_1 @ theta

    print('Here is a example with the linear regression using gradient descent:\n')
    print('Predict the price of a 1650 sq-ft and 3 br house:')
    print('Price is: %.3f'%price1)