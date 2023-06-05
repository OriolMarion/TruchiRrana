import tkinter as tk
from tkinter import simpledialog
import pickle as pkl
import numpy as np
import time as time

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from PIL import ImageTk, Image
        
def findPath(map_grid, start, end, debug=False):
                
    # matrix = [[1] * len(map_grid) for _ in range(len(map_grid[0]))]
    matrix = np.array([[1 if not i else 0 for i in j] for j in map_grid])
    print(matrix)
    
    grid = Grid(matrix=matrix)
    node_start = grid.node(start[1], start[0])
    node_end = grid.node(end[1], end[0])

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(node_start, node_end, grid)

    if debug:
        print('operations:', runs, 'path length:', len(path))
        print(path)
        print(grid.grid_str(path=path, start=node_start, end=node_end))
        
    return path

def calculateDir(path):
    if path[0][0] < path[1][0] and path[0][1] == path[1][1]:
        return 90
    elif path[0][0] == path[1][0] and path[0][1] < path[1][1]:
        return 180
    elif path[0][0] > path[1][0] and path[0][1] == path[1][1]:
        return 270
    elif path[0][0] == path[1][0] and path[0][1] > path[1][1]:
        return 0

class MapGenerator:
    def __init__(self, method, image, squareSize, offset=40, loadPath=None, northOffset=0):
        self.squareSize = squareSize
        self.image = image
        self.offset = offset
        self.root = tk.Tk()
        self.root.title("Map visualizer")
        self.buttons = []
        self.canvas = None
        self.northOffset = northOffset
        
        if method == "new":
            self.rows = int(image.height / self.offset)
            self.cols = int(image.width / self.offset)
            self.grid = [[0] * self.cols for _ in range(self.rows)]
            
        elif method == "load": 
            assert loadPath != None, "No path for method load"
            map = self.load(loadPath)
            print(map)
            self.rows = len(map)
            self.cols = len(map[0])
            self.grid = map

    def toggle_value(self, row, col):
        self.grid[row][col] = (self.grid[row][col] + 1) % 4
        self.update_button_color(row, col)

    def color(self, value):
        assert value in [0, 1, 2, 3], f"Value {value} has no color"
        if value == 0:
            return "white"
        elif value == 1:
            return "black"
        elif value == 2:
            return "green"
        elif value == 3:
            return "red"

    def update_button_color(self, row, col):
        button = self.buttons[row][col]
        value = self.grid[row][col]
        button.config(bg=self.color(value))

    def generate_grid(self):       
        # Create canvas with background image
        background_image = ImageTk.PhotoImage(self.image)
        self.canvas = tk.Canvas(self.root, width=self.cols * self.offset, height=(self.rows + 2) * self.offset)
        self.canvas.create_image(0, 0, anchor="nw", image=background_image)
        self.canvas.pack()

        # Create buttons on top of the canvas
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                button = tk.Button(self.canvas, bg=self.color(self.grid[row][col]), width=2, height=1,
                                   command=lambda r=row, c=col: self.toggle_value(r, c), relief=tk.FLAT)
                button.place(x=self.offset/2 -12 + col * self.offset, y=self.offset/2 -12 + row * self.offset)
                button_row.append(button)
            self.buttons.append(button_row)
        
        startButton = tk.Button(self.canvas, bg="white", width=5, height=1,
                                command=lambda : self.start(), text= "Start")
        startButton.place(x=self.offset/2 -12 + 0 * self.offset, y=self.offset/2 -12 + (self.rows + 1) * self.offset)
        stopButton = tk.Button(self.canvas, bg="white", width=5, height=1,
                                command=lambda : self.stop(), text = "Stop")
        stopButton.place(x=self.offset/2 + 12 + 1 * self.offset, y=self.offset/2 -12 + (self.rows + 1) * self.offset)
        saveButton = tk.Button(self.canvas, bg="white", width=5, height=1,
                                command=lambda : self.askSaveMap(), text = "Save")
        saveButton.place(x=self.offset/2 + 36 + 2 * self.offset, y=self.offset/2 -12 + (self.rows + 1) * self.offset)
        
        self.root.mainloop()
         
    def load(self, name):
        with open(f"maps/{name}.pkl", 'rb') as f:
            map = pkl.load(f)
        return map
    
    def save(self, map, name):
        with open(f"maps/{name}.pkl", 'wb') as f:
            pkl.dump(map, f)
    
    def askSaveMap(self):
        name = simpledialog.askstring("Enter Text", "Enter the map name")
        self.save(self.grid, name)
        return map
    
    def start(self):
        debug = False
        print("Starting")
        # Access the generated grid
        map_grid = map.grid
        
        # Trobar inici(2) i final(3) del recorregut
        for i in range(len(map_grid)):
            for j in range(len(map_grid[i])):
                if map_grid[i][j] == 2: 
                    start = [i, j]
                    map_grid[i][j] = 0
                elif map_grid[i][j] == 3: 
                    end = [i, j]
                    map_grid[i][j] = 0

        # Calcular el path
        path = findPath(map_grid, start, end, True)
        print(type(path))
        
        while (len(path) > 1):
            distAct = getDistance(serial, debug)
            dirAct = getCompass(serial, debug) - self.northOffset
            dir = calculateDir(path)
            
            while (dir != dirAct):
                turnRight(serial, debug)
                dirAct = getCompass(serial, debug) - self.northOffset
            stopTurn(serial, debug)
            
            jump(serial, debug)
            dist = getDistance(serial, debug) 
            if dist + self.squareSize < distAct:
                path.pop(0)
            print(path)
        
    def stop(self):
        pass

image = Image.open("images/casa1.png")

map = MapGenerator("load", image, 1, offset=40, loadPath="casa2")
map.generate_grid()