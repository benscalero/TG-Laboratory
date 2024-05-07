from shapely.geometry import Point
from SimulationResultsHolder import SimulationResultsHolder


class Simulation:
    def __init__(self, t, f, num_days):
        self.tg = t
        self.fr = f
        self.number_of_days = num_days
        self.cumulative_prob = 1
        self.results_holder = None

    # Main method for simulation; also writes results to output files
    def run_simulation(self, count):
        self.results_holder = SimulationResultsHolder()
        self.results_holder.add_fly_release_info(str(self.fr))

        for i in range(1, self.number_of_days + 1):
            print(f"Running simulation for day {i}...")
            total_prob_for_day = 0
            number_of_flies = 0

            for current_release_point in self.fr.all_outbreak_locations:
                fly_locations = current_release_point.locate_flies(i)

                for current_location in fly_locations:
                    if current_location.x > 3 * self.tg.x_max or current_location.y > 3 * self.tg.y_max:
                        current_escape_prob = 1.0
                    else:
                        current_escape_prob = self.tg.get_total_escape_probability(Point(current_location))
                    results = [str(i), current_release_point.short_string(), self.location_to_string(current_location),
                               str(current_escape_prob)]
                    self.results_holder.add_raw_data(results)
                    total_prob_for_day += current_escape_prob
                    number_of_flies += 1

            avg_for_day = total_prob_for_day / number_of_flies
            self.cumulative_prob *= avg_for_day
            self.results_holder.add_avg_escape_probability(i, avg_for_day)

        print(f"Simulation #{count} complete!")
        return self.results_holder

    @staticmethod
    def location_to_string(p):
        return f"({p.x}, {p.y})"
