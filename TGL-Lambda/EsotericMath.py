import math
import random

from shapely.geometry import Point


class EsotericMath:

    @staticmethod
    def pick_next_point(release_point, stdev, rng):
        x = rng.gauss(0, 1) * stdev + release_point.x
        y = rng.gauss(0, 1) * stdev + release_point.y
        return Point(x, y)

    @staticmethod
    def pick_some_points(release_point, diff_coeff, day, number_of_points, rng):
        result = []
        stdev = EsotericMath.calculate_standard_deviation(diff_coeff, day)
        for _ in range(number_of_points):
            result.append(EsotericMath.pick_next_point(release_point, stdev, rng))
        return result

    @staticmethod
    def pick_some_points_mdd(release_point, step_size, steps_per_day, turn_angle_stdev, day, num_points, rng):
        number_of_steps = day * steps_per_day
        mdd = EsotericMath.calculate_mdd(step_size, number_of_steps, turn_angle_stdev)
        return EsotericMath.pick_points_with_radius(release_point, mdd, num_points, rng)

    @staticmethod
    def calculate_standard_deviation(diff_coeff, time):
        return math.sqrt(2 * diff_coeff * time)

    @staticmethod
    def pick_point_in_grid(x_max, y_max):
        return Point(random.randrange(0, int(x_max)), random.randrange(0, int(y_max)))

    @staticmethod
    def calculate_mdd(step_size, number_of_steps, stdev):
        r = math.exp((-math.pow(stdev, number_of_steps)) / 2)
        return step_size * math.sqrt(0.79 * number_of_steps * (1 - r) * (1 + r))

    @staticmethod
    def pick_points_with_radius(center, radius, num_points, rng):
        return [(center[0] + math.cos(angle) * radius, center[1] + math.sin(angle) * radius)
                for angle in (rng.uniform(0, 2 * math.pi) for _ in range(num_points))]
