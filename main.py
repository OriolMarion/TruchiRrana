import tkinter as tk
import pickle as pkl
import numpy as np

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from PIL import ImageTk, Image


def saveMap(map, name):
    with open(f"{name}.pkl", 'wb') as f:
        pkl.dump(map, f)
        
def loadMap(name):
    with open(f"{name}.pkl", 'rb') as f:
        map = pkl.load(f)
    return map

class MapGenerator:
    def __init__(self, image, offset):
        self.image = image
        self.offset = offset
        self.rows = int(image.height / self.offset)
        self.cols = int(image.width / self.offset)
        self.grid = [[0] * self.cols for _ in range(self.rows)]
        self.root = tk.Tk()
        self.root.title("Map generator")
        self.buttons = []
        self.canvas = None

    def toggle_value(self, row, col):
        self.grid[row][col] = (self.grid[row][col] + 1) % 4
        self.update_button_color(row, col)

    def update_button_color(self, row, col):
        button = self.buttons[row][col]
        value = self.grid[row][col]
        if value == 0:
            button.config(bg="white")
        elif value == 1:
            button.config(bg="black")
        elif value == 2:
            button.config(bg="green")
        elif value == 3:
            button.config(bg="red")

    def generate_grid(self):       
        # Create canvas with background image
        background_image = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(self.root, width=self.cols * self.offset, height=self.rows * self.offset)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.pack()

        # Create buttons on top of the canvas
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                button = tk.Button(self.canvas, bg="white", width=2, height=1,
                                   command=lambda r=row, c=col: self.toggle_value(r, c), relief=tk.FLAT)
                button.place(x=self.offset/2 -12 + col * self.offset, y=self.offset/2 -12 + row * self.offset)
                button_row.append(button)
            self.buttons.append(button_row)

        self.root.mainloop()

# Interactive graphical interface
print("Welcome to the Boolean Grid Generator!")

image = Image.open("casa1.png")

map = MapGenerator(image, 40)
map.generate_grid()

# Access the generated grid
map_grid = map.grid

map_grid = loadMap("casa1")

####################################### PATHFINDING ########################################

matrix = [[1] * len(map_grid) for _ in range(len(map_grid[0]))]

for i in range(len(map_grid)):
    for j in range(len(map_grid[i])):
        if map_grid[i][j] == 2: 
            start = [j, i]
            map_grid[i][j] = 0
        elif map_grid[i][j] == 3: 
            end = [j, i]
            map_grid[i][j] = 0

map_grid = np.array(map_grid)
matrix = np.array([[1 if not i else 0 for i in j] for j in map_grid])
print(matrix)

grid = Grid(matrix=matrix)
start = grid.node(start[0], start[1])
end = grid.node(end[0], end[1])

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
print(finder)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))