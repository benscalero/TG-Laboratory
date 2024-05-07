import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
import time
from TrapGrid import TrapGrid
from SimulationRunner import SimulationRunner
from SimulationResultsHolderAggregator import SimulationResultsHolderAggregator
from Sampling import Sampling
from Trap import Trap
from SortingResults import SortingResults
from MoreInfoGUI import MoreInfoGUI
import sys


class DriverGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.trap_grid_file = None
        self.outbreak_file = None
        self.random_seed = 0
        self.release_point_file = None
        self.num_days = 0
        self.num_simulations = 0
        self.num_flies = 0
        self.diff_coeff = 0.0
        self.step_size = 0.0
        self.steps_per_day = 0.0
        self.turn_angle_stdev = 0.0
        self.use_mdd = False
        self.outbreak_locations_provided = False
        self.tg = None
        self.desired_escape_prob = None
        self.tolerance = None
        self.lower_bounds = []
        self.upper_bounds = []
        self.num_samples = 0
        self.sim_runner = None
        self.output_file = None
        self.lhs_list = None
        self.agg = None
        self.final_day_results = {}

        self.title("TrapModel GUI")
        self.geometry("500x700")

        # Create labels, entries, and buttons
        self.button_exp_info = tk.Button(self, text="More Info", command=MoreInfoGUI.experiment_info)

        self.label_tg = tk.Label(self, text="TrapGrid file:")
        self.entry_tg = tk.Entry(self)
        self.button_tg = tk.Button(self, text="Browse", command=self.browse_trapgrid)

        self.label_ob = tk.Label(self, text="Outbreak file:")
        self.entry_ob = tk.Entry(self)
        self.button_ob = tk.Button(self, text="Browse", command=self.browse_outbreak)

        self.label_nd = tk.Label(self, text="Number of days:")
        self.entry_nd = tk.Entry(self)

        self.label_ns = tk.Label(self, text="Number of simulations:")
        self.entry_ns = tk.Entry(self)

        self.label_nf = tk.Label(self, text="Number of flies per outbreak:")
        self.entry_nf = tk.Entry(self)

        self.button_insect_info = tk.Button(self, text="More Info", command=MoreInfoGUI.insect_info)

        self.label_dc = tk.Label(self, text="Diffusion coefficient:")
        self.entry_dc = tk.Entry(self)

        self.label_s = tk.Label(self, text="Random seed:")
        self.entry_s = tk.Entry(self)

        self.label_step_size = tk.Label(self, text="Step size:")
        self.entry_step_size = tk.Entry(self)

        self.label_steps_per_day = tk.Label(self, text="Steps per day:")
        self.entry_steps_per_day = tk.Entry(self)

        self.label_turn_angle_stdev = tk.Label(self, text="Turn angle stdev:")
        self.entry_turn_angle_stdev = tk.Entry(self)

        self.button_res_info = tk.Button(self, text="More Info", command=MoreInfoGUI.results_info)

        self.label_desired_escape_prob = tk.Label(self, text="Desired escape probability:")
        self.entry_desired_escape_prob = tk.Entry(self)

        self.label_tolerance = tk.Label(self, text="Tolerance:")
        self.entry_tolerance = tk.Entry(self)

        self.label_lower_bounds = tk.Label(self, text="Lambda lower bounds:")
        self.entry_lower_bounds = tk.Entry(self)

        self.label_upper_bounds = tk.Label(self, text="Lambda upper bounds:")
        self.entry_upper_bounds = tk.Entry(self)

        self.label_num_samples = tk.Label(self, text="Number of lambda sets:")
        self.entry_num_samples = tk.Entry(self)

        self.label_output_file = tk.Label(self, text="Output File:")
        self.entry_output_file = tk.Entry(self)
        self.button_output_file = tk.Button(self, text="Browse", command=self.browse_output_file)

        # Create and pack submit button
        self.button_submit = tk.Button(self, text="Run Simulation", command=self.main)

        # Pack widgets
        title1 = tk.Label(text="Experiment Info", font=Font(weight="bold"))
        title1.grid(row=0, column=1, padx=2, pady=2)

        self.button_exp_info.grid(row=0, column=2, padx=2, pady=2)

        self.label_tg.grid(row=1, column=0, sticky="e")
        self.entry_tg.grid(row=1, column=1, padx=5, pady=5)
        self.button_tg.grid(row=1, column=2)

        self.label_ob.grid(row=2, column=0, sticky="e")
        self.entry_ob.grid(row=2, column=1, padx=5, pady=5)
        self.button_ob.grid(row=2, column=2)

        self.label_nd.grid(row=3, column=0, sticky="e")
        self.entry_nd.grid(row=3, column=1, padx=5, pady=5)

        self.label_ns.grid(row=4, column=0, sticky="e")
        self.entry_ns.grid(row=4, column=1, padx=5, pady=5)

        self.label_nf.grid(row=5, column=0, sticky="e")
        self.entry_nf.grid(row=5, column=1, padx=5, pady=5)

        self.label_s.grid(row=6, column=0, sticky="e")
        self.entry_s.grid(row=6, column=1, padx=5, pady=5)

        spacer1 = tk.Label(text="Insect Info", font=Font(weight="bold"))
        spacer1.grid(row=7, column=1, padx=2, pady=2)

        self.button_insect_info.grid(row=7, column=2, padx=2, pady=2)

        self.label_dc.grid(row=8, column=0, sticky="e")
        self.entry_dc.grid(row=8, column=1, padx=5, pady=5)

        spacer2 = tk.Label(text="OR")
        spacer2.grid(row=9, column=1, padx=2, pady=2)

        self.label_step_size.grid(row=10, column=0, sticky="e")
        self.entry_step_size.grid(row=10, column=1, padx=5, pady=5)

        self.label_steps_per_day.grid(row=11, column=0, sticky="e")
        self.entry_steps_per_day.grid(row=11, column=1, padx=5, pady=5)

        self.label_turn_angle_stdev.grid(row=12, column=0, sticky="e")
        self.entry_turn_angle_stdev.grid(row=12, column=1, padx=5, pady=5)

        spacer3 = tk.Label(text="Results Info", font=Font(weight="bold"))
        spacer3.grid(row=13, column=1, padx=2, pady=2)

        self.button_res_info.grid(row=13, column=2, padx=2, pady=2)

        self.label_desired_escape_prob.grid(row=14, column=0, sticky="e")
        self.entry_desired_escape_prob.grid(row=14, column=1, padx=5, pady=5)

        self.label_tolerance.grid(row=15, column=0, sticky="e")
        self.entry_tolerance.grid(row=15, column=1, padx=5, pady=5)

        self.label_lower_bounds.grid(row=16, column=0, sticky="e")
        self.entry_lower_bounds.grid(row=16, column=1, padx=5, pady=5)

        self.label_upper_bounds.grid(row=17, column=0, sticky="e")
        self.entry_upper_bounds.grid(row=17, column=1, padx=5, pady=5)

        self.label_num_samples.grid(row=18, column=0, sticky="e")
        self.entry_num_samples.grid(row=18, column=1, padx=5, pady=5)

        self.label_output_file.grid(row=19, column=0, sticky="e")
        self.entry_output_file.grid(row=19, column=1, padx=5, pady=5)
        self.button_output_file.grid(row=19, column=2)

        spacer4 = tk.Label(text="")
        spacer4.grid(row=20, column=1, padx=2, pady=2)

        self.button_submit.grid(row=21, column=1, pady=10)

    def browse_trapgrid(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.entry_tg.delete(0, tk.END)
        self.entry_tg.insert(0, filename)

    def browse_outbreak(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.entry_ob.delete(0, tk.END)
        self.entry_ob.insert(0, filename)

    def browse_output_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.entry_output_file.delete(0, tk.END)
        self.entry_output_file.insert(0, filename)

    def main(self):
        # Processes inputs
        # initializes entries if filled
        if len(self.entry_tg.get()):
            self.trap_grid_file = self.entry_tg.get()

        if len(self.entry_ob.get()):
            self.outbreak_file = self.entry_ob.get()
            self.outbreak_locations_provided = True

        if len(self.entry_nd.get()):
            self.num_days = int(self.entry_nd.get())

        if len(self.entry_ns.get()):
            self.num_simulations = int(self.entry_ns.get())

        if len(self.entry_nf.get()):
            self.num_flies = int(self.entry_nf.get())

        if len(self.entry_dc.get()):
            self.diff_coeff = float(self.entry_dc.get())

        if len(self.entry_s.get()):
            self.random_seed = int(self.entry_s.get())

        if len(self.entry_step_size.get()):
            self.step_size = float(self.entry_step_size.get())

        if len(self.entry_steps_per_day.get()):
            self.steps_per_day = int(self.entry_steps_per_day.get())

        if len(self.entry_turn_angle_stdev.get()):
            self.turn_angle_stdev = float(self.entry_turn_angle_stdev.get())

        if len(self.entry_desired_escape_prob.get()):
            self.desired_escape_prob = float(self.entry_desired_escape_prob.get())
            if self.desired_escape_prob <= 0 or self.desired_escape_prob >= 1:
                print("Sorry, the argument 'Desired Escape Probability' must"
                      " be greater than 0.0 and below 1.0")
                exit()
        else:
            print("Please provide a desired escape probability.")
            exit()

        if len(self.entry_tolerance.get()):
            self.tolerance = float(self.entry_tolerance.get())
            if self.tolerance <= 0 or self.tolerance >= 1:
                print("Sorry, the argument 'Tolerance' must"
                      " be greater than 0.0 and below 1.0")
                exit()
            if not len(self.entry_desired_escape_prob.get()):
                print("Sorry, the argument 'Tolerance' cannot be given"
                      " without the argument 'Desired Escape Probability'")
                exit()

        if len(self.entry_lower_bounds.get()):
            self.lower_bounds = [float(x.strip()) for x in self.entry_lower_bounds.get().strip('[]').split(', ')]

        if len(self.entry_upper_bounds.get()):
            self.upper_bounds = [float(x.strip()) for x in self.entry_upper_bounds.get().strip('[]').split(', ')]

        if len(self.entry_num_samples.get()):
            self.num_samples = int(self.entry_num_samples.get())

        self.output_file = self.entry_output_file.get()

        # sets defaults for any entries left empty (exits if no TrapGrid file)
        if self.trap_grid_file is None:
            print("Sorry, the argument '-tg <TrapGrid file>' is required.")
            exit()

        if self.random_seed == 0:
            self.random_seed = round(time.time() * 1000)
            print("No seed provided for random number generator; using " + str(self.random_seed))

        if self.num_days == 0:
            self.num_days = 10
            print("No value specified for number of days; will run simulation for 10 days. \n")

        if self.num_simulations == 0:
            self.num_simulations = 1
            print("No value specified for number of simulations; will run 1 simulation. \n")

        if self.num_flies == 0:
            self.num_flies = 50
            print("No value specified for number of flies; will use 500 flies per release. \n")

        if self.diff_coeff == 0.0:
            self.diff_coeff = 30.0
            print("No value specified for diffusion coefficient; will use 30.0\n")

        # If step_size, steps_per_day, and turn_angle_stdev supplied, use MDD model. Otherwise, it's diffusion
        if self.step_size != 0 and self.steps_per_day != 0 and self.turn_angle_stdev != 0:
            self.use_mdd = True

        if self.num_samples == 0:
            self.num_samples = 20
            print("No value specified for number of lambda sets; will use 20. \n")

        # Create TrapGrid
        try:
            self.tg = TrapGrid(self.trap_grid_file)
        except ValueError:
            print("ValueError with TrapGrid file")
            sys.exit(-1)
        except IOError:
            print("IOError with TrapGrid")
            sys.exit(-1)

        # Calculate and print TrapGrid info...
        if self.output_file:
            sys.stdout = open(self.output_file, 'w')
        print("######################## TrapGrid information ####################")
        print("#" + str(self.tg))
        print("#Number of different lambdas: " + str(len(self.tg.list_of_lambdas)))
        print("######################## Parameters ##############################")
        print("#Number of days: " + str(self.num_days))
        print("#Number of simulations: " + str(self.num_simulations))
        print("#Number of flies per outbreak: " + str(self.num_flies))
        if self.use_mdd:
            print("#Step size: " + str(self.step_size))
            print("#Steps per day: " + str(self.steps_per_day))
            print("#Turn angle stdev: " + str(self.turn_angle_stdev))
        else:
            print("#Diffusion coefficient: " + str(self.diff_coeff))
        print("#Random seed: " + str(self.random_seed))
        print(f"#Desired Escape Probability after {str(self.num_days)} day(s): {str(self.desired_escape_prob)}")
        print(f"#Tolerance: " + str(self.tolerance))
        print(f"#Lambda Lower Bounds: " + str(self.lower_bounds))
        print(f"#Lambda Upper Bounds: " + str(self.upper_bounds))
        print(f"#Number of lambda sets: " + str(self.num_samples))
        print("##################################################################\n")
        self.out_file()

        ### NOW RUN SIMULATIONS ###
        num_lambda_params = len(self.tg.list_of_lambdas)
        if not self.lower_bounds:
            self.lower_bounds = [0 for _ in range(num_lambda_params)]
        elif not len(self.lower_bounds) == len(self.tg.list_of_lambdas):
            print("Length of lower bounds does not match number of lambdas. Please fix.")
            exit()
        if not self.upper_bounds:
            self.upper_bounds = [1 for _ in range(num_lambda_params)]
        elif not len(self.upper_bounds) == len(self.tg.list_of_lambdas):
            print("Length of upper bounds does not match number of lambdas. Please fix.")
            exit()
        self.lhs_list = Sampling.get_LHS_samples(num_lambda_params, self.num_samples, self.lower_bounds,
                                            self.upper_bounds)
        print(f"{len(self.tg.list_of_lambdas)} different type(s) of traps given. "
              f"Program will solve for sets of {len(self.tg.list_of_lambdas)} lambda(s).")

        # run SimulationRunner for each individual combination of lambdas given to us through LHS
        combination_count = 0
        for combination in self.lhs_list:
            new_trap_list = []
            for old_trap in self.tg.original_trap_list:
                new_trap = old_trap
                for lambda_param in range(len(self.tg.list_of_lambdas)):
                    if old_trap.get_lambda() == self.tg.list_of_lambdas[lambda_param]:
                        new_trap = Trap(old_trap.get_location().x, old_trap.get_location().y, combination[lambda_param])
                        break
                new_trap_list.append(new_trap)
            self.tg.trap_list = new_trap_list
            combination_count += 1
            print(
                f"Now running {self.num_simulations} simulations for lambdas {combination} ({combination_count}"
                f" of {len(self.lhs_list)})")
            if not self.outbreak_locations_provided:
                self.sim_runner = SimulationRunner(self.tg, self.num_days, self.num_flies, self.diff_coeff,
                                                   self.step_size, self.steps_per_day, self.turn_angle_stdev,
                                                   self.use_mdd, self.random_seed, self.num_simulations)
                self.sim_runner.run_simulations()
            else:
                self.sim_runner = SimulationRunner(self.tg, self.num_days, self.num_flies,
                                                   self.diff_coeff, self.step_size, self.steps_per_day,
                                                   self.turn_angle_stdev, self.use_mdd, self.random_seed,
                                                   outbreak_file=self.outbreak_file)
                self.sim_runner.run_simulations()
            self.in_file(self.output_file)

            ### PRINT RESULTS ###
            # first the average cumulative probabilities for each set of lambdas
            print("#Averaged Simulation Results\n")
            self.agg = SimulationResultsHolderAggregator(self.sim_runner.all_results, combination)
            print(self.agg.aggregate_simulation_results_holders(self.final_day_results))
            print("##################################################################\n")
            self.out_file()

        # then at the end print list of lambdas sorted by those resulting in escape probability closest to target
        if self.desired_escape_prob:
            self.in_file(self.output_file)
            final_results = SortingResults.sorting(self.final_day_results, self.desired_escape_prob)
            print("######################### FINAL RESULTS ##########################\n")
            print("#Results show each set of lambda(s) used and their corresponding\n"
                  f"average cumulative escape probability of day {self.num_days}.\n"
                  "#These results are sorted by their escape probability's distance\n"
                  f"to the given desired escape probability {self.desired_escape_prob}\n")
            # if tolerance is given the closest result's distance from desired probability is greater than tolerance,
            # give recommendation of what to set lower_bounds and upper_bounds to
            if self.tolerance and SortingResults.distance_from_target(list(final_results.keys())[0],
                                                                      self.desired_escape_prob) > self.tolerance:
                print("######################## RECOMMENDATION ##########################\n")
                print("#The closest result seems to be too far (greater than the\n"
                      f"given tolerance {self.tolerance})\n"
                      "It is recommended to run this program again with the\n"
                      "following lower and upper bounds.\n")
                print("#NOTE: This will improve accuracy towards a specific set of \n"
                      "lambda(s), but keep in mind that this set of lambdas won't\n"
                      "necessarily be the only possible answer.\n")
                recommendation = SortingResults.recommended_bounds(final_results, self.desired_escape_prob)
                print(f"Recommended Lower bounds:\n{recommendation[0]}\n")
                print(f"Recommended Upper Bounds:\n{recommendation[1]}\n")
            print("##################################################################\n")
            print(f"Order of Lambdas: {self.tg.list_of_lambdas}\n")
            print("__________________________________________________________________")
            for key, value in final_results.items():
                print(f"Lambda(s): {value}\nEscape Probability: {key}\n")
                print("__________________________________________________________________")

        if self.output_file:
            self.out_file()
            print("All simulations complete. Results are in specified file. Now exiting.")
        sys.exit()

    @staticmethod
    def in_file(output_file):  # outputs will be within file until out_file is called
        if output_file:
            sys.stdout = open(output_file, 'a')

    @staticmethod
    def out_file():  # outputs will be in terminal until in_file is called
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    my_gui = DriverGUI()
    my_gui.mainloop()
