import numpy as np
import turtle, sys 
from distutils.util import strtobool

from generators import dfs_generator, it_dfs_generator
from solvers import bfs_solver

from graph import Graph
from util import colors

class Maze():
    def __init__(self, length:int, height:int, scale:int, speed:int, solve:bool):
        try:
            length = int(length)
            height = int(height)
            self.scale = int(scale)
            self.speed = int(speed)
            self.generator = bool(strtobool(solve))

        except ValueError as err:
            print(
                f'{colors.FAIL}VALUE ERROR: {err.args[0]} --'
                f'Arguments usage int:length, int:height, int:scale, '
                f'int:speed, bool:solve {colors.END}'
            )
            sys.exit()

        self.columns = height//self.scale
        self.rows = length//self.scale
        self.total = self.rows*self.columns

        print(f'\n{colors.OK_CYAN}Maze Size: {self.rows}x{self.columns} -- '
            f'Draw Speed: {self.speed}{colors.END}')

        self.grid = []
        self.graph = Graph() # Graph representation to generate maze on
        self.maze = Graph() # Graph representation of generated maze

        # Create turtle and screen
        self.turtle = turtle.Turtle()
        self.window = turtle.Screen()

        # Initialize turtle and grid
        self.turtle_set()
        self.init_grid()

    def init_grid(self): 
        self.grid = np.arange(self.total).reshape(self.rows,self.columns)

        for x in range(self.rows):
            for y in range(self.columns):
                if (y-1 >= 0):
                    top = self.grid[x][y-1]
                    self.graph.add_edge(self.grid[x][y], top)
                if (x-1 >= 0): 
                    left = self.grid[x-1][y]
                    self.graph.add_edge(self.grid[x][y], left)
                if (x+1 < self.rows):
                    right = self.grid[x+1][y]
                    self.graph.add_edge(self.grid[x][y], right)
                if (y+1 < self.columns):
                    bot = self.grid[x][y+1]
                    self.graph.add_edge(self.grid[x][y], bot)

    def turtle_set(self):
        self.window.bgcolor('#%02x%02x%02x' % (44, 52, 66))
        self.turtle.speed(self.speed)
        self.turtle.pensize(self.scale-(self.scale*.2))
        self.turtle.shape('circle')
        self.turtle.color('yellow')
        self.turtle.pencolor('white')
        self.turtle.up()
        self.turtle.goto((-.5*self.rows)*self.scale,(-.5*self.columns)*self.scale)
        self.turtle.pendown()

    def generate(self):
        print(f'{colors.OK_GREEN}Generating Maze using randomized DFS w/ backtracking...{colors.END}')

        if self.rows > 20 or self.columns > 20:
            print(f'{colors.OK_GREEN}Maze size above recursion depth limit. Using iterative implementation...{colors.END}')
            it_dfs_generator(self, 0)
            return

        visited = [False]*self.total
        road_used = []
        dfs_generator(self, 0, visited, road_used, -1)

    def solve(self):
        print(f'{colors.OK_GREEN}Solving Maze using BFS...{colors.END}')
        self.draw_path(bfs_solver(self, 0, self.total - 1), 'Red')

    def mark_ends(self):
        self.turtle.ht()
        self.turtle.pensize(self.scale*.6)
        self.turtle.up()
        self.turtle.goto((-.5*self.rows)*self.scale,(-.5*self.columns)*self.scale)
        self.turtle.down()
        self.turtle.seth(180)
        self.turtle.color("green")
        self.turtle.forward(self.scale)
        self.turtle.up()
        path= self.grid[self.rows-1][self.columns-1]
        self.turtle.goto(((path % self.rows)-.5*self.rows)*self.scale,((path // self.rows)-.5*self.columns) * self.scale)
        self.turtle.down()
        self.turtle.color("red")
        self.turtle.seth(0)
        self.turtle.forward(self.scale)
        self.turtle.up()
        self.turtle.backward(self.scale)
        print(f'\n{colors.OK_GREEN}- DONE -{colors.END}\n')

    def draw_path(self, path, color): # Draws path on top of maze
        self.turtle.pensize(self.scale * 0.4)
        self.turtle.pencolor(color)
        self.turtle.up()
        self.turtle.goto((-.5 * self.rows) * self.scale, (-.5 * self.columns) * self.scale)
        self.turtle.pendown()

        for v in path:
            self.turtle.goto(((v % self.rows) - .5 * self.rows) * self.scale,
                             ((v // self.rows) - .5 * self.columns) * self.scale)
