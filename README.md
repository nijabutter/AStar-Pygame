# A* in Pygame

Requires pygame:

`pip install pygame`

Controls:
- <kbd>R</kbd> Reset
- <kbd>G</kbd> Generate random obstacles
- <kbd>Space</kbd> Begin the search.
- Left-Click Draw obstacles
- Right-Click Remove obstacles

It will search until all cells have been checked or a valid path is found.
Diagonals are valid, however they can go through obstacles.

For example this is a valid move:
```
oooooooo███████
████████ooooooo
```

This has been implemented alongside a maze generator to solve mazes:

https://github.com/nijabutter/Maze-Solver-Pygame/
