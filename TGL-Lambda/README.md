# TGL-Lambda
TGL-Lambda takes a desired escape probability and runs a large number of TrapGrid instances, testing many levels of lure attractiveness (notated as lambda) to determine what value(s) of lambda would result in this escape probability. TGL-Lambda was made to ease the process of estimating lure attrractive from completed MMR experiments.

In your Command Line Interface, go to the TGL-Lambda's directory and run "py TGL-Lambda.py". This will open the GUI for you to input your parameters. The parameters are split into three sections:

The first section is Experiment Info. “TrapGrid file” is a required parameter that provides TGL-Lambda with the details of the experiment’s grid layout and trap details. This should be a tab-separated values (.tsv) file. The first row should give the grid dimension as x meters by y meters. Every following row after this represents a trap and should consist of 3 values: the x-coordinate, the y-coordinate, and the λ parameter for the trap. “Outbreak file” is an optional .tsv file that consists of the (x, y) locations of outbreaks.  If this file is not provided, the program will run simulations with randomized outbreak locations. “Number of days” indicates how many days pass in each simulation of the experiment, “number of simulations” indicates how many simulations will occur for each set of λs, “number of flies” indicates how many flies are to be released for each simulation, and “random seed” is just an arbitrary value that the user can provide for the randomization processes within the software.
          	
The second section is Insect Info, and this provides detail on the insects themselves. “Diffusion coefficient” indicates the distance that the flies move in square meters per day. If this value is provided, ignore the rest of the parameters in this section. Otherwise, the user can provide the step size, number of steps per day, and the turn angle standard deviation of the insects. If these are provided, then the program will use a Mean Dispersal Distance model instead. However, if none of the “Insect Info” parameters are given, TGL-Lambda will use the diffusion model with a diffusion coefficient of 30.0 by default.

The third section is Results Info. “Desired Escape Probability” is what the user wants the average cumulative escape probability to be after the final day of simulations. After the program runs every simulation, it will print every set of λ combinations and their corresponding final day result, sorted by their result’s distance to this value. "Tolerance"  represents the maximum distance that the user wants between their desired escape probability and the closest result that the program returns. This is a way for the program to understand whether its results end up being satisfactory, and a "recommendation" will be given if it's not. “Lower bounds” and “upper bounds” are the next two parameters, and they represent the lowest and highest values of λ, respectively, that the program will obtain in its sampling. These should be inputted as lists, starting and ending with [] brackets, and they should contain the λ values inside, separated by a comma. "Number of lambda sets” is the value of how many different sets of λ for TGLambdas to create, using Latin Hypercube Sampling, for testing. By default, this value is 20, meaning that it uses LHS where the parameter space (0, 1) is split into 20 intervals that span 0.05 each. Keep in mind that the greater this value, the more accurate the program, but the longer the runtime as well. Lastly, "output file" is an optional .txt file for the program to put its results.