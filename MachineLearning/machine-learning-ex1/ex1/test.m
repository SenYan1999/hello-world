% Initialize the terminal
clear;close;clc;

% Import the dataset into our model
data = load('ex1data2.txt');
X = data(:,1:2);
y = data(:,3);

m = length(y);                                     %the numbers of the example

% Show the 10 examples of the dataset
fprintf('First 10 examples from the dataset');
fprintf('X = [%.0f , %.0f] , y = %.0f \n' , [X(1:10,:) y(1:10,:)]');

fprintf('program paused, please enter to continue.\n');
pause;

% Scale features and set the to zero mean
[X, mu, sigma] = featureNormalize(X);

% Add intercept term to X
X = [ones(m,1) X];

# Gradient Discent
fprintf('Running Gradient Discent ...\n');

# Choose the alpha and iterations number
alpha = 0.01;
iter = 400;

% Init theta and run Gradient Discent Algorithm
theta = zeros(3,1);
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, iter);

% ----------      Multiple curves       --------------
% Plot the convergence graph
figure;
plot(1:numel(J_history), J_history, '-b', 'LineWidth', 2);
xlabel = ('Numbers of Iterations');
ylabel = ('Cost');
hold on;
# Choose the alpha and iterations number
alpha = 0.1;
iter = 400;
theta = zeros(3,1);
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, iter);
plot(1:numel(J_history), J_history, '-r', 'LineWidth', 2);

alpha = 0.05;
iter = 400;
theta = zeros(3,1);
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, iter);
plot(1:numel(J_history), J_history, '-g', 'LineWidth', 2);

legend()

% Estimate the house price with 1650 sq-ft and 3 br home
x_now = featureNormalize([1650,3]);
price = [1 x_now] * theta;

fprintf('House price using gradient descent with 1650 sq-ft and 3 br homes is:\n $%.0f\n', price);
fprintf('Program paused, please enter to continue.\n');
pause;

% Normal Equation
data = csvread('ex1data2.txt');
X = data(:,1:2);
y = data(:,3);
m = length(y);

X = [ones(m,1) X];

theta = normalEqn(X,y);

fprintf('The theta is: %f \n', theta);
fprintf('\n');

price = [1 1650 3] * theta;

fprintf('House of 1650 sq-ft and 3 br homes using narmal equation is priced as: \n $%.01f', price);

pause