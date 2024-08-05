# TGL-Delimiter
TGL-Delimiter creates a .txt TrapGrid file containing grid size, trap coordinates, and trap attractiveness. The user inputs units, a list of different trap densities, a list of lambdas per buffer, and an output file. The units (meters) represents the length of each square in the grid, and the list of different trap densities represents the number of traps per square unit for every buffer. TGL-Delimiter will create a grid of traps with a core area containing the number of traps given by the first trap density. It will then create a buffer layer of 8 square units surrounding this core area with traps, creating a 3x3 grid. The number of traps in each square unit will correspond to the second trap density given. If another trap density is given, another buffer layer will be made around the current grid to make it a 5x5 grid. This process will continue for the entire list of trap densities. TGL-Delimiter will assign the first lambda from the list to the traps in the core area, the second lambda to the first buffer layer, and so on.

This program uses tkinter, random, and numpy packages. Tkinter and random are included by default with Python, but numpy is installed separately. If you do not have this installed or are unsure, open your system's command prompt or terminal, navigate to the directory for TGL-Delimiter, and run "py -m pip install -r requirements.txt" to satisfy this requirement.

## Update 2024-8-1
TGL-Delimiter now takes in ANY size square for each grid. Input and output will both be in meters (REMINDER: 1km is 1000m and 1 mile is approx. 1609m).

## Update 2024-7-16
TGL-Delimiter can now accept either square kilometers or square miles for each grid. Keep in mind that the output will always be in meters.
