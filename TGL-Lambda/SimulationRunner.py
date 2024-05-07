from Simulation import Simulation
from Outbreak import Outbreak
import csv
import random


class SimulationRunner:
    def __init__(self, tg, num_days, num_flies, diff_coeff, step_size, steps_per_day, turn_angle_stdev, use_mdd, seed,
                 num_sims=None, outbreak_file=None):
        self.tg = tg
        self.number_of_days = num_days
        self.number_of_flies = num_flies
        self.diff_coeff = diff_coeff
        self.step_size = step_size
        self.steps_per_day = steps_per_day
        self.turn_angle_stdev = turn_angle_stdev
        self.use_mdd = use_mdd
        self.rng = random.Random(seed)
        self.number_of_simulations = num_sims
        self.all_results = []
        self.outbreak_locations_provided = outbreak_file is not None
        self.outbreak_file = outbreak_file
        self.outbreaks = []

    def create_simulation(self, tg, outbreak):
        return Simulation(tg, outbreak, self.number_of_days)

    def create_random_outbreak(self, tg, seed):
        use_random_location = True
        x_max, y_max = tg.x_max, tg.y_max
        return Outbreak(x_max, y_max, self.number_of_flies, self.diff_coeff, self.step_size, self.steps_per_day,
                        self.turn_angle_stdev, self.use_mdd, seed, use_random_location)

    def run_simulations(self):
        count = 1
        if not self.outbreak_locations_provided:
            for i in range(self.number_of_simulations):
                next_seed = self.rng.random()
                outbreak = self.create_random_outbreak(self.tg, next_seed)
                simulation = self.create_simulation(self.tg, outbreak)
                one_result = simulation.run_simulation(count)
                count += 1
                self.all_results.append(one_result)
        else:
            try:
                self.outbreaks = self.create_outbreaks_from_file(self.outbreak_file)
            except IOError as e:
                print(f"Error trying to read outbreak file: {e}")
                raise

            for outbreak in self.outbreaks:
                simulation = self.create_simulation(self.tg, outbreak)
                one_result = simulation.run_simulation(count)
                count += 1
                self.all_results.append(one_result)

    def create_outbreaks_from_file(self, filename):
        my_outbreaks = []
        use_random_location = False
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file, delimiter='\t')
                for row in reader:
                    if len(row) == 2:
                        x, y = map(float, row)
                        next_seed = self.rng.random()
                        outbreak = Outbreak(x, y, self.number_of_flies, self.diff_coeff, self.step_size,
                                            self.steps_per_day, self.turn_angle_stdev, self.use_mdd, next_seed,
                                            use_random_location)
                        my_outbreaks.append(outbreak)
                    else:
                        raise ValueError("Invalid input! Outbreak file must have 2 values per line (x, y).")
        except FileNotFoundError as e:
            print(f"Input file {filename} not found")
            raise e

        return my_outbreaks
