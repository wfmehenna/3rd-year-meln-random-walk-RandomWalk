import random # This line imports the 'random' module, which is used to make random choices (like rolling a dice or choosing a direction).
import os     # This line imports the 'os' module, which is used to interact with the operating system (specifically, to clear the screen).
import time   # This line imports the 'time' module, which is used to pause the program for a short duration.

# --- Global Variables and Functions ---

# This list holds the possible outcomes when rolling a standard six-sided dice.
dice_poosibilities = [1, 2, 3, 4, 5, 6]

# This is a simple function to simulate a single dice rolll.
def roll():
    # 'random.choice()' picks one item at random from the provided list.
    return random.choice(dice_poosibilities)

# These are the possible changes in position (delta) for a Point:
# 1: move one step in the positive direction
# 0: stay in the same position
# -1: move one step in the negative direction
possibilities = [1, 0, -1]


# --- Point Class ---

# A 'class' is a blueprint for creating objects. The 'Point' class represents a single moving entity on the grid.
class Point:
    # This is the constructor method. It's called automatically when you create a new Point object.
    def __init__(self, x, y):
        # 'self.x' and 'self.y' store the Point's current coordinates.
        self.x = x
        self.y = y

    # This method changes the Point's coordinates (its position).
    def move(self):
        # The Point randomly moves in the x-direction by adding one of the 'possibilities' (1, 0, or -1).
        self.x += random.choice(possibilities)
        # The Point also randomly moves in the y-direction.
        self.y += random.choice(possibilities)

    # This method simply prints the Point's current coordinates to the console.
    def display(self):
        # The 'f-string' (f"...") allows easy embedding of variables inside the string.
        print(f"The points coordinates are {self.x}, {self.y}")


# --- Grid Class ---

# The 'Grid' class represents the 2D area where the Points move.
class Grid:
    # Constructor for the Grid. It sets up the grid size and an empty list to hold Point objects.
    def __init__(self, width=0, height=0, points=[]):
        # 'self.width' and 'self.height' define the dimensions of the grid.
        self.width = width
        self.height = height
        # 'self.points' is a list that will store all the 'Point' objects currently on the grid.
        self.points = points

    # This method adds a Point object to the Grid's list of points.
    def add_point(self, point):
        self.points.append(point)

    # This is the core method for visualizing the grid.
    def display_grid(self):
        # We use a nested loop to iterate through every cell (i, j) of the grid.
        # 'i' represents the row (x-coordinate).
        for i in range(self.width):
            # 'j' represents the column (y-coordinate).
            for j in range(self.height):
                marker = " "  # Start by assuming the cell is empty (marked by a space).

                # Now, check every Point in the 'self.points' list.
                for p in self.points:
                    # Check if the current cell coordinates (i, j) match a Point's coordinates (p.x, p.y).
                    if (i == p.x) and (j == p.y):
                        # If a match is found, place a '*' marker on the grid.
                        marker = "*"
                        # NOTE: This simple version assumes only one Point can be in a cell.
                        # If multiple Points are on the same spot, it just shows one '*'.

                # Print the determined 'marker' (either " " or "*").
                # 'end=""' prevents the 'print' function from starting a new line,
                # so the markers appear side-by-side to form a row.
                print(marker, end="")

            # After the inner loop finishes (a full row 'j' is printed),
            # this 'print()' with no arguments starts a new line for the next row 'i'.
            print()

# --- Program Execution ---

# 1. Create a Grid object named G1 with dimensions 10x10.
G1 = Grid(10, 10)
# 2. Create the first Point object named p1 at coordinates (2, 3).
p1 = Point(2, 3)
# 3. Create the second Point object named p2 at coordinates (4, 4).
p2 = Point(4, 4)
# 4. Add the points to the grid.
G1.add_point(p1)
G1.add_point(p2)


# --- Simulation Loop ---

# This 'while True' loop runs the simulation forever (until the user manually stops it, e.g., with Ctrl+C).
while True:
    # 1. Display the current state of the grid.
    G1.display_grid()

    # 2. Move the points to a new, random location.
    p1.move()
    p2.move()

    # 3. Pause the program for 0.5 seconds so the user can see the movement.
    time.sleep(0.5)

    # 4. Clear the terminal screen using the 'os' module.
    # On Linux/macOS, you might use 'os.system("clear")' instead of "cls".
    # This makes the new grid display appear in the same spot, creating an animation effect.
    os.system("cls")
