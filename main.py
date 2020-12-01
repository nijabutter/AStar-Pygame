import pygame
import random
import time
import math
from Cell import Cell

W_WIDTH, W_HEIGHT = 800, 800 # window size
ACROSS, DOWN = 100, 100 # columns and rows
FPS = 1000 # maxmimum 1000

C_HEIGHT = W_HEIGHT // DOWN
goalX = (ACROSS-1) * C_WIDTH
goalY = (DOWN-1) * C_HEIGHT
window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
pygame.display.set_caption("A* Pathfinding")
isRunning = True
background = (0, 0, 0)
pygame.init()

isWaiting = True

startX = 0
startY = 0
if FPS > 1000:
    FPS = 1000
fpsdelay = 1000 // FPS
def findLowestF():
    lowestIndex = 0
    for i in range(len(openSet)):
        if openSet[i].f < openSet[lowestIndex].f:
            lowestIndex = i
    return openSet[lowestIndex]

def heuristic(ax, ay, bx, by):
    return math.sqrt((bx-ax)**2 + (by-ay)**2)

def Setup():
    global current
    global openSet
    global closedSet
    global solutionFound
    global cells
    global path
    solutionFound = False
    closedSet = []
    openSet = []
    cells = []
    path = []
    for y in range(DOWN):
        cells.append([])
        for x in range(ACROSS):
            cells[y].append(Cell(window, x*C_WIDTH, y*C_HEIGHT, C_WIDTH, C_HEIGHT, x, y))
            if x > 0:
                # add to left neighbour
                cells[y][x-1].neighbours.append(cells[y][x])
                cells[y][x].neighbours.append(cells[y][x-1])
            if y > 0:
                # add to top neighbour
                cells[y-1][x].neighbours.append(cells[y][x])
                cells[y][x].neighbours.append(cells[y-1][x])
                # # top right
                if x < ACROSS-1:
                    cells[y][x].neighbours.append(cells[y-1][x+1])
                    cells[y-1][x+1].neighbours.append(cells[y][x])
                if x > 0:
                    # top left
                    cells[y-1][x-1].neighbours.append(cells[y][x])
                    cells[y][x].neighbours.append(cells[y-1][x-1])
    openSet.append(cells[startY][startX])
    current = openSet[0]

def generateObstacles():
    for row in cells:
        for cell in row:
            if random.randint(1, 10) < 3:
                cell.obstacle = True
    cells[goalY//C_HEIGHT][goalX//C_WIDTH].obstacle = False

def Draw():
    global current
    global path
    global solutionFound
    if not isWaiting and not solutionFound:
        if len(openSet) > 0:
            current = findLowestF()
            if current.x == goalX and current.y == goalY:
                path.append(current)
                while current.previous != None:
                    path.append(current.previous)
                    current = current.previous
                solutionFound = True
                print("done")
                return
            openSet.remove(current)
            closedSet.append(current)

            for n in current.neighbours:
                if n.obstacle:
                    continue
                if n in closedSet:
                    continue
                tentativeG = current.g + 1
                if n not in openSet:
                    openSet.append(n)
                elif tentativeG > n.g:
                    continue
                n.g = tentativeG
                n.h = heuristic(n.x, n.y, goalX, goalY)
                n.f = n.g + n.h 
                n.previous = current
                #current = n
        else:
            solutionFound = True
            print("no solution")
    

    window.fill(background)
    for y in range(DOWN):
        for x in range(ACROSS):
            if cells[y][x].obstacle:
                cells[y][x].draw((0,0,0))
            else:
                cells[y][x].draw((200, 200, 200))
    
    for i in range(len(closedSet)):
        closedSet[i].draw((100, 0, 0))
    for i in range(len(openSet)):
        openSet[i].draw((0, 150, 0))
    filled_rect = pygame.Rect(goalX, goalY, C_WIDTH, C_HEIGHT)
    pygame.draw.rect(window, (255,0,0), filled_rect)
    if not isWaiting:
        current.draw((0, 0, 255))
    for p in path:
        filled_rect = pygame.Rect(p.x, p.y, C_WIDTH, C_HEIGHT)
        pygame.draw.rect(window, (0,0,255), filled_rect)
    pygame.display.flip()

def Input():
    global isWaiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global isRunning
            isRunning = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                isWaiting = False
            elif event.key == pygame.K_r:
                Setup()
                isWaiting = True
            elif event.key == pygame.K_g:
                generateObstacles()
    isClicked = pygame.mouse.get_pressed()
    if isClicked[0]:
        pos = pygame.mouse.get_pos()
        mX, mY = int(pos[0]/C_WIDTH), int(pos[1]/C_HEIGHT)
        cells[mY][mX].obstacle = True
    elif isClicked[2]:
        pos = pygame.mouse.get_pos()
        mX, mY = int(pos[0]/C_WIDTH), int(pos[1]/C_HEIGHT)
        cells[mY][mX].obstacle = False

Setup()
while isRunning:
    Input()
    Draw()
    pygame.time.delay(fpsdelay)
