from collections import OrderedDict


class SimulationResultsHolder:
    def __init__(self):
        self.raw_data = []
        self.avg_escape_probability_by_day = OrderedDict()
        self.cum_escape_probability_by_day = OrderedDict()
        self.fly_release_info = ""

    def add_raw_data(self, one_line_of_data):
        self.raw_data.append(one_line_of_data)

    def add_avg_escape_probability(self, day, prob):
        self.avg_escape_probability_by_day[day] = prob

    def calculate_cumulative_probabilities(self):
        current_cumulative_probability = 1.0
        for day, daily_avg in self.avg_escape_probability_by_day.items():
            current_cumulative_probability *= daily_avg
            self.cum_escape_probability_by_day[day] = current_cumulative_probability

    def raw_data_to_string(self):
        result = "[Day\tReleasePoint\tFlyLocation\tP(escape)]\n"
        for line in self.raw_data:
            result += f"{', '.join(line)}\n"
        return result

    def add_fly_release_info(self, info):
        self.fly_release_info = info
