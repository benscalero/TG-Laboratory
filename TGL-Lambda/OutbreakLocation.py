from EsotericMath import EsotericMath
import random

"""OutbreakLocation class abstracts a release at a given location on the grid
of a given number of flies having a given diffusion coefficient"""


class OutbreakLocation:
    def __init__(self, rp, num_flies, dc, step_size, steps_per_day, turn_angle_stdev, use_mdd, seed):
        self.location = rp
        self.number_of_flies = num_flies
        self.diffusion_coefficient = dc
        self.step_size = step_size
        self.steps_per_day = steps_per_day
        self.turn_angle_stdev = turn_angle_stdev
        self.use_mdd = use_mdd
        self.rng = random.Random(seed)
        self.esoteric_math = EsotericMath()

    def __str__(self):
        return f"{self.number_of_flies} flies released at {self.location} with Diffusion Coefficient" \
               f" {self.diffusion_coefficient}"

    # Returns the location of the OutbreakLocation in "(x, y)" format
    def short_string(self):
        return f"({self.location.x}, {self.location.y})"

    # Randomly places flies using a Gaussian distribution according to their diffusion coefficient
    # and the number of days elapsed since their release
    # @param day
    # @param An array of points representing the locations of the flies
    def locate_flies(self, day):
        if not self.use_mdd:
            return self.esoteric_math.pick_some_points(self.location, self.diffusion_coefficient,
                                                       day, self.number_of_flies, self.rng)
        return self.esoteric_math.pick_some_points_mdd(self.location, self.step_size, self.steps_per_day,
                                                       self.turn_angle_stdev, day, self.number_of_flies, self.rng)
