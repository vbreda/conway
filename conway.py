import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 4

def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
    
grid = np.zeros(N*N).reshape(N,N)
addGlider(1, 1, grid)

#Random
x = np.random.choice([0,255], 4*4, p=[0.1, 0.9]).reshape(4, 4) 

#Chosen
np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])

plt.imshow(grid, interpolation='nearest')
plt.show()
