import numpy as np
from shapely.geometry import Point


class Trap:
    def __init__(self, x, y, lam):
        self.location = Point(x, y)
        self.lambda_ = lam

    def get_location(self):
        return self.location

    def get_lambda(self):
        return self.lambda_

    def __str__(self):
        return f"Position: ({self.location.x},{self.location.y}); Lambda: {self.lambda_}"

    def get_escape_probability(self, point):
        distance = Point.distance(self.location, point)
        exp_lam = np.exp(self.lambda_ * distance)
        numerator = 2 * exp_lam
        denominator = 1 + exp_lam ** 2
        escape_prob = 1 - (numerator / denominator)

        if not np.isnan(escape_prob):
            return escape_prob
        return 1.0
