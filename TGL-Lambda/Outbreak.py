from OutbreakLocation import OutbreakLocation
from shapely.geometry import Point
import random


class Outbreak:

    def __init__(self, x, y, n, diff_coeff, step_size, steps_per_day, turn_angle_stdev, use_mdd, seed,
                 location_is_random):
        self.all_outbreak_locations = []
        if location_is_random:
            my_point = Point(random.uniform(0, x), random.uniform(0, y))
        else:
            my_point = Point(x, y)
        rp = OutbreakLocation(my_point, n, diff_coeff, step_size, steps_per_day, turn_angle_stdev, use_mdd, seed)
        self.all_outbreak_locations.append(rp)

    def __str__(self):
        number_of_locations = len(self.all_outbreak_locations)
        if number_of_locations == 1:
            return self.all_outbreak_locations[0].short_string()
        else:
            result = f"Outbreak with {number_of_locations} OutbreakLocation(s): "
            for i in range(number_of_locations - 1):
                result += f"{self.all_outbreak_locations[i].__str__()} ; "
            result += self.all_outbreak_locations[number_of_locations - 1].__str__()
            return result
