import random
import matplotlib.pyplot as plt
def create_maze(size):
    maze = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
    maze[0][0] = 0
    maze[size-1][size-1] = 0
    return maze
size = 10
maze = create_maze(size)
plt.imshow(maze, cmap='binary')
plt.show()
