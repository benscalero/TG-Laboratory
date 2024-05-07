import tkinter as tk


class MoreInfoGUI:
    @staticmethod
    def experiment_info():
        new_window = tk.Toplevel()
        new_window.title("Experiment Info")
        new_window.geometry("800x200")
        label1 = tk.Label(new_window, text="This section of parameters pertains to the details of the experiment.\n")
        label2 = tk.Label(new_window, text="TrapGrid file: This is a tab-separated file and is a REQUIRED parameter. "
                                           "The first line should give x and y values representing the upper-right\n"
                                           "corner of a rectangle (whose lower-left corner is (0,0)). Each subsequent "
                                           "line should have three entries -- x and y (used to mark the location of\n"
                                           "the trap) and a lambda parameter, which is a placeholder name representing"
                                           " a specific lure used for that trap. For example, if the first three\n"
                                           " traps all used the same lure, the lambda parameter for each of them could"
                                           " be 'lam1'. Then, if the next six traps in the file all had the same lure\n"
                                           " but were different from the first three, their lambda parameter could "
                                           "each be named 'lam2'.")
        label3 = tk.Label(new_window, text="Outbreak file: This is a two-column tab-delimited file and is optional. "
                                           "This file contains the x and y locations of outbreaks to be simulated.\n"
                                           "If you provide this file, the program will run one simulation "
                                           "per location.")
        label4 = tk.Label(new_window, text="If values are not provided for 'number of days', 'number of simulations',"
                                           "nor 'number of flies', the defaults will be 10, 1, and 50, respectively.")
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        new_window.protocol("WM_DELETE_WINDOW", lambda: new_window.destroy())

    @staticmethod
    def insect_info():
        new_window = tk.Toplevel()
        new_window.title("Insect Info")
        new_window.geometry("800x100")
        label1 = tk.Label(new_window, text="This section of parameters pertains to the details of the insects "
                                           "involved.")
        label2 = tk.Label(new_window, text="The default mode of this program uses a diffusion model for insect "
                                           "dispersal. This diffusion coefficient is given in square meters per day\n"
                                           "(default is 30.0). However, if you provide the step size, amount of steps"
                                           " per day, and the turn angle standard deviation of the insects, then the\n"
                                           " program will use a Mean Dispersal Distance model instead.")
        label1.pack()
        label2.pack()
        new_window.protocol("WM_DELETE_WINDOW", lambda: new_window.destroy())

    @staticmethod
    def results_info():
        new_window = tk.Toplevel()
        new_window.title("Results Info")
        new_window.geometry("800x350")
        label1 = tk.Label(new_window, text="This section of parameters pertains to the output desired by the user.")
        label2 = tk.Label(new_window, text="Desired Escape Probability: This value is what the user wants the average"
                                           " cumulative escape probability to be after the final day of simulations.\n"
                                           "After running, the program will print results of all sets of lambdas and "
                                           "their corresponding final day result, sorted by their result's distance\n"
                                           "to this value. (This value must be greater than 0 but less than 1)")
        label3 = tk.Label(new_window, text="Tolerance: This value is the maximum distance that the user wants between"
                                           " their desired escape probability and the closest result that the program\n"
                                           "returns. If that distance is greater than the tolerance, the program will "
                                           "give a 'recommended' lower and upper bounds for the lambda values for the\n"
                                           "user to apply in another run of the program, which should result in more"
                                           "accurate results. (This value must be greater than 0 but less than 1)")
        label4 = tk.Label(new_window, text="Lower Bounds and Upper Bounds: These represent the lowest and highest, "
                                           "respectively, values of lambda that the program will test. Both of these\n"
                                           "bounds must be inputted as lists, starting and ending with [] brackets, "
                                           "containing the lambda values inside, separated by ', '. For example,\n"
                                           "if you were running the program with 2 different lambdas amongst the traps,"
                                           " and you wanted the first lambda to be no less than 0.4 and the second\n"
                                           "lambda to be no less than 0.6, then you would input '[0.4, 0.6]'. The same"
                                           " would be done for upper bounds if the user wants the lambdas to be no\n"
                                           "greater than these values, instead. By default, lower bounds is set to a"
                                           "list consisting of 0s for all lambdas, and upper bound is a list\n"
                                           "consisting of all 1s. (Remember that the values within the "
                                           "list represent lambdas, so they must be greater than 0 but less than 1)")
        label5 = tk.Label(new_window, text="Number of lambda sets: This value is how many different sets of lambda "
                                           "the program will come up with for testing using Latin Hypercube Sampling.\n"
                                           "Keep in mind that the greater this value, the longer the runtime but the"
                                           " greater the accuracy as well. By default, this value is set to 20.")
        label6 = tk.Label(new_window, text="Output file: The user has the option to provide a file for the program to"
                                           " put its results. By default, the results are shown in the terminal.")
        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        new_window.protocol("WM_DELETE_WINDOW", lambda: new_window.destroy())
