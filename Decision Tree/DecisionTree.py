import numpy as np
import matplotlib.pyplot as plt


class DecisionTree:
    def __init__(self, x):
        self.x = x


if __name__ == '__main__':
    data = np.array([
        [1, 1], [0, 0], [4, 4], [2, 2],
        [10, 10], [15, 15], [13, 13], [12, 12],
        [50, 50], [55, 55], [40, 40], [45, 45],
        [48, 48]])
    dt = DecisionTree(data)
    print('moein')
