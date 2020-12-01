# A* in Pygame

Requires pygame:

`pip install pygame`

Use left click to draw obstacles and left click to remove them.

Press `R` to restart and `SPACE` to begin the search.

Use left click to draw  obstacles, right click to remove them and `G` to generate random obstacles.

The program will search until all cells are checked or a valid path has been found.
Diagonals are valid, however they can go through obstacles.

For example this is a valid move:
```
oooooooo███████
████████ooooooo
```

This has been implemented into a maze generator to solve mazes
https://github.com/nijabutter/Maze-Solver-Pygame/
