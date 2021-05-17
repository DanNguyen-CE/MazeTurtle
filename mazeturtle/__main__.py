import sys, time
from distutils.util import strtobool

from maze import Maze
from util import colors

def main(*args): # Args: length:int, height:int, scale:int, speed:int, solve:bool

    if len(args) > 5:
        print(f'{colors.FAIL}ARGUMENT ERROR: Too many arguments. Refer to README.md{colors.END}')
    elif len(args) < 5:
        print(f'{colors.FAIL}ARGUMENT ERROR: Too few arguments. Refer to README.md{colors.END}')

    my_maze = Maze(*args)

    # Generate maze and time execution
    start_time = time.time()
    my_maze.generate()
    end_time = time.time() - start_time

    m, s = divmod(end_time, 60)
    print(f'{colors.OK_CYAN}Generation executed in: {m:.0f}:{s:2.5f}{colors.END}')

    # Solve maze and time execution
    if bool(strtobool(args[4])):
        start_time = time.time()
        my_maze.solve()
        end_time = time.time() - start_time

        m, s = divmod(end_time, 60)
        print(f'{colors.OK_CYAN}Generation executed in: {m:.0f}:{s:2.5f}{colors.END}')

    my_maze.mark_ends()
    my_maze.window.exitonclick()

if __name__ == "__main__":
    main(*sys.argv[1:])
