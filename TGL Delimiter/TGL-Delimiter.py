import sys
import tkinter as tk
from tkinter import filedialog
import random

import numpy as np


class TGDelimiter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.length = 0
        self.density_list = []
        self.lambdas = []
        self.output_file = None
        self.units = 1000

        self.title("TG Delimiter")
        self.geometry("400x200")

        self.label_units = tk.Label(self, text="Units (km or miles)")
        self.entry_units = tk.Entry(self)

        self.label_density_list = tk.Label(self, text="List of Different Trap Densities:")
        self.entry_density_list = tk.Entry(self)

        self.label_lambdas = tk.Label(self, text="List of Lambdas per Buffer:")
        self.entry_lambdas = tk.Entry(self)

        self.label_output_file = tk.Label(self, text="Output File:")
        self.entry_output_file = tk.Entry(self)
        self.button_output_file = tk.Button(self, text="Browse", command=self.browse_output_file)

        self.button_submit = tk.Button(self, text="Create Grid", command=self.main)

        self.label_units.grid(row=1, column=0, sticky="e")
        self.entry_units.grid(row=1, column=1, padx=5, pady=5)

        self.label_density_list.grid(row=2, column=0, sticky="e")
        self.entry_density_list.grid(row=2, column=1, padx=5, pady=5)

        self.label_lambdas.grid(row=3, column=0, sticky="e")
        self.entry_lambdas.grid(row=3, column=1, padx=5, pady=5)

        self.label_output_file.grid(row=4, column=0, sticky="e")
        self.entry_output_file.grid(row=4, column=1, padx=5, pady=5)
        self.button_output_file.grid(row=4, column=2)

        self.button_submit.grid(row=5, column=1, pady=10)

    def browse_output_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        self.entry_output_file.delete(0, tk.END)
        self.entry_output_file.insert(0, filename)

    @staticmethod
    def generate_traps_in_square(num_traps, lambdas, units):
        grid_density = int(np.sqrt(num_traps))  # Density of points in each axis
        traps_per_axis = (num_traps + grid_density - 1) // grid_density

        # Generate evenly spaced x and y coordinates, excluding edges
        x_coordinates = np.linspace(0, units, traps_per_axis, endpoint=False)
        y_coordinates = np.linspace(0, units, traps_per_axis, endpoint=False)

        # Create a list to store trap coordinates
        trap_coordinates = [(x, y, lambdas) for x in x_coordinates for y in y_coordinates]

        # Return the requested number of traps
        while len(trap_coordinates) > num_traps:
            trap_coordinates.remove(random.choice(trap_coordinates))

        return trap_coordinates

    @staticmethod
    def generate_squares_by_densities(trap_densities, lambdas, units):
        density_squares = []

        for density in range(len(trap_densities)):
            num_traps = int(trap_densities[density])  # Convert trap density to number of traps
            trap_coordinates = TGDelimiter.generate_traps_in_square(num_traps, lambdas[density], units)
            density_squares.append(trap_coordinates)

        return density_squares

    @staticmethod
    def go_through_ring(start_, length_, list_, units):
        new_traps = []
        # Finds spacing based off of difference between two lowest x values
        sorted_traps = sorted(list_, key=lambda trap: trap[0])
        lowest_x_value = sorted_traps[0][0]
        for next_lowest in sorted_traps[1:]:
            next_lowest_x_value = next_lowest[0]
            if next_lowest[0] > lowest_x_value:
                break
        spacing = (next_lowest_x_value - lowest_x_value) / 2

        for sides in range(4):
            if sides == 0:
                for squares in range(1, length_ + 1):
                    for i in range(len(list_)):
                        x, y, lambdas = list_[i]
                        x += (start_ + squares - 1) * units + spacing
                        y += start_ * units + spacing
                        if (x, y, lambdas) not in new_traps:
                            new_traps.append((x, y, lambdas))
            if sides == 1:
                for squares in range(1, length_ + 1):
                    for i in range(len(list_)):
                        x, y, lambdas = list_[i]
                        x += (start_ + length_ - 1) * units + spacing
                        y += (start_ + squares - 1) * units + spacing
                        if (x, y, lambdas) not in new_traps:
                            new_traps.append((x, y, lambdas))
            if sides == 2:
                for squares in range(1, length_ + 1):
                    for i in range(len(list_)):
                        x, y, lambdas = list_[i]
                        x += (start_ + squares - 1) * units + spacing
                        y += (start_ + length_ - 1) * units + spacing
                        if (x, y, lambdas) not in new_traps:
                            new_traps.append((x, y, lambdas))
            else:
                for squares in range(1, length_ + 1):
                    for i in range(len(list_)):
                        x, y, lambdas = list_[i]
                        x += start_ * units + spacing
                        y += (start_ + squares - 1) * units + spacing
                        if (x, y, lambdas) not in new_traps:
                            new_traps.append((x, y, lambdas))
        return new_traps

    @staticmethod
    def add_core_area(length_, list_, units):
        new_traps = []
        sorted_traps = sorted(list_, key=lambda trap: trap[0])
        lowest_x_value = sorted_traps[0][0]
        for next_lowest in sorted_traps[1:]:
            next_lowest_x_value = next_lowest[0]
            if next_lowest[0] > lowest_x_value:
                break
        spacing = (next_lowest_x_value - lowest_x_value) / 2
        for i in list_:
            x, y, lam = i
            x += (length_ - 1) * units + spacing
            y += (length_ - 1) * units + spacing
            new_traps.append((x, y, lam))
        return new_traps

    def main(self):
        if len(self.entry_units.get()):
            if self.entry_units.get() == "km":
                self.units = 1000
            elif self.entry_units.get() == "miles":
                self.units = 1609
            else:
                print("Sorry, please input an acceptable unit (km or miles).")
                exit()

        if len(self.entry_density_list.get()):
            self.density_list = [float(x.strip()) for x in self.entry_density_list.get().strip('[]').split(', ')]

        if len(self.entry_lambdas.get()):
            try:
                self.lambdas = [float(x.strip()) for x in self.entry_lambdas.get().strip('[]').split(', ')]
            except ValueError:
                self.lambdas = [str(x.strip()) for x in self.entry_lambdas.get().strip('[]').split(', ')]

        if len(self.entry_output_file.get()):
            self.output_file = self.entry_output_file.get()

        squares_list = TGDelimiter.generate_squares_by_densities(self.density_list, self.lambdas, self.units)
        grid = []
        self.length = len(self.density_list) * 2 - 1

        for buffers in range(len(self.density_list)):
            # if this is the core area, it is only one square
            if buffers == 0:
                grid.extend(TGDelimiter.add_core_area(len(self.density_list), squares_list[0], self.units))
            else:
                grid.extend(TGDelimiter.go_through_ring(len(self.density_list) - buffers - 1, buffers * 2 + 1,
                                                        squares_list[buffers], self.units))

        ### Now we output onto the TrapGrid file ###
        sys.stdout = open(self.output_file, 'w')
        print(f"{self.length * self.units}\t{self.length * self.units}")
        for trap in grid:
            x, y, lam = trap
            print(f"{x}\t{y}\t{lam}")

        sys.stdout = sys.__stdout__
        print("TrapGrid file has been created. Now exiting.")
        sys.exit()


if __name__ == "__main__":
    my_gui = TGDelimiter()
    my_gui.mainloop()
