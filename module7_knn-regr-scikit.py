import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

N = read_positive_integer("Enter the number of data points (N): ")
k = read_positive_integer("Enter the value of k for k-NN Regression (k): ")

x_values = np.zeros(N)
y_values = np.zeros(N)

print("Enter the (x, y) points:")
for i in range(N):
    x_values[i] = float(input(f"Enter x value for point {i+1}: "))
    y_values[i] = float(input(f"Enter y value for point {i+1}: "))

X = float(input("Enter the value of X for prediction: "))

if k > N:
    print("Error: k should be less than or equal to N.")
else:
    X_train = x_values.reshape(-1, 1)
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X_train, y_values)
    Y = knn_regressor.predict(np.array(X).reshape(1, -1))
    print("Predicted Y value:", Y[0])
    if k <= N:
        y_predicted = knn_regressor.predict(X_train)
        r2 = r2_score(y_values, y_predicted)
        print("Coefficient of determination (R^2):", r2)