from Trap import Trap


class TrapGrid:
    def __init__(self, filename=None):
        self.x_max = None
        self.y_max = None
        self.list_of_lambdas = []
        self.trap_list = []
        self.original_trap_list = []
        if filename:
            self.read_traps_from_file(filename)

    def __str__(self):
        return f"TrapGrid from x=0 to x={self.x_max}, y=0 to y={self.y_max} containing {len(self.trap_list)} traps.\n"

    def read_traps_from_file(self, filename):
        my_traps = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            first_line = lines[0].split('\t')
            if len(first_line) != 2:
                print(
                    "Error -- first line of TrapGrid file should contain two entries"
                    " representing the coordinates of the upper-right corner of the grid.")
                raise ValueError()
            self.x_max = float(first_line[0])
            self.y_max = float(first_line[1])

            for line in lines[1:]:
                trap_data = line.split()
                if len(trap_data) == 3:
                    x = float(trap_data[0])
                    y = float(trap_data[1])
                    lam = trap_data[2]
                    if lam not in self.list_of_lambdas:
                        self.list_of_lambdas.append(lam)
                    new_trap = Trap(x, y, lam)
                    my_traps.append(new_trap)
                else:
                    print("Invalid input! TrapGrid file must have 3 values per line (x, y, lambda).")
                    raise ValueError()

        self.trap_list = my_traps
        self.original_trap_list = my_traps

    def get_total_escape_probability(self, current_location):
        escape_probability = 1.0
        for trap in self.trap_list:
            escape_probability *= trap.get_escape_probability(current_location)
        return escape_probability
