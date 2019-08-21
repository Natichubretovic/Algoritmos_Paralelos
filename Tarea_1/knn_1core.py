import numpy as np
from collections import defaultdict

class Point:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y
    def euc_distance(self, point):
        distance =
            np.sqrt(
                (self.x - point.x)**2
                +(self.y - point.y)**2
                )
        return distance

def KNN(point, k, data, metric = "Euclidean"):
    tuple_dist_label=[(l.label, point.distance(l)) for l in data)]
    sorted_by_second = sorted(tuple_dist_label, key=lambda tup: tup[1])
    k_nearest = sorted_by_second[:k]
    label_times = defaultdict(int)
    for elem in k_nearest:
        label_times[elem[0]] += 1
    label = [
        item[0] for item in sorted(label_times.items(), key = lambda tup:tup[1]
        ][-1]
