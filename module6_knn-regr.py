import numpy as np


class KNNRegression:
    def __init__(self, k):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        distances = np.sqrt(np.sum((X_test - self.X_train) ** 2, axis=1))
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = self.y_train[nearest_indices]
        return np.mean(nearest_labels)


def main():
    N = int(input("Enter the number of points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k should be less than or equal to N.")
        return

    points = []
    for i in range(N):
        x = float(input(f"Enter x coordinate for point {i + 1}: "))
        y = float(input(f"Enter y coordinate for point {i + 1}: "))
        points.append([x, y])

    X = np.array(points)[:, 0]
    y = np.array(points)[:, 1]

    knn = KNNRegression(k)
    knn.fit(X, y)

    test_point = float(input("Enter the test point (X): "))
    prediction = knn.predict(np.array([test_point]))
    print(f"The predicted value (Y) for X = {test_point} is: {prediction}")


if __name__ == "__main__":
    main()