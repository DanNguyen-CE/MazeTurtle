# Maze Turtle - A Python Turtle Maze Visualizer

<p align="center"><img src="/media/maze_animation.gif"></p>

A maze generation and solving visualizer using Python's [``Turtle``](https://docs.python.org/3/library/turtle.html) graphics library. This program uses a randomized Depth First Search (DFS) to generate the maze and shortest path Breadth First Search (BFS) to solve the maze.

## Configuration
There are a few input parameters for maze generation
```
python maze_generator.py 300, 300, 10, 0, true
```
Main takes 5 arguments: (int) ``length``, (int) ``height``, (int) ``scale``, (int) ``speed``, (bool) ``solve``

``length, height, scale`` are values to determine the size of the maze. Scale will determine how large the turtle's pen size will be and consequently divide length and height. So, (300, 300, 10) would result in a 30x30 maze with a pen size of 10.

``speed`` can take values from 1-10 (slow to fast), with 0 being a special value which is the fastest.

``solve`` can take either 'true' or 'false' which draws the maze solution after generation or not.

### KNOWN ISSUE: Cannot create a non-square maze. Length & Height must be equal.

## How To Run

General Requirements: [``Python3``](https://www.python.org/downloads/), [``Numpy``](https://numpy.org/)

To Run:
```
$ ./MazeTurtle> python mazeturtle 300, 300, 10, 1, true
```
