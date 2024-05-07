from typing import List
from SimulationResultsHolder import SimulationResultsHolder


class SimulationResultsHolderAggregator:
    def __init__(self, holders: List[SimulationResultsHolder], current_lambda):
        self.results_holders = holders
        self.current_lambda = current_lambda
        for sim_res_hol in self.results_holders:
            sim_res_hol.calculate_cumulative_probabilities()

    def aggregate_simulation_results_holders(self, final_day_results):
        result = f"Lambda: {self.current_lambda}\n"
        result += "Day\tAv Cumulative Escape Probability\n"
        num_days = len(self.results_holders[0].avg_escape_probability_by_day)

        for day in range(1, num_days + 1):
            avg_prob = self.calculate_avg_cum_prob(day)
            result += f"{day}\t{avg_prob}\n"
            if day == num_days:
                final_day_results[avg_prob] = self.current_lambda

        return result

    def calculate_avg_cum_prob(self, day):
        total_prob, num_probs = 0.0, 0

        for sim_res_hol in self.results_holders:
            daily_prob = sim_res_hol.cum_escape_probability_by_day.get(day, 0.0)
            total_prob += daily_prob
            num_probs += 1

        avg_prob = total_prob / num_probs if num_probs > 0 else 0.0
        return avg_prob
