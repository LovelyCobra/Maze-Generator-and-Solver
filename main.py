import sys, os, time, random
import maze_gen as mg

#Generating a list of possible moves from a position
def allowed_moves(pos):
    y = pos[0] #Row from the top down
    x = pos[1] #Position from the left to the right
    
    return [[y + 1, x], [y, x + 1], [y - 1, x], [y, x - 1]]


#The main recursive function with backtracking        
def through_maze(maze, pos, end):
    w = len(maze[0]) #Maze's width
    h = len(maze)    #Maze's height
    
    #Coordinates within the maze
    y = pos[0] #Row from the top down
    x = pos[1] #Position from the left to the right
    
    #Base case
    maze[y][x] = 2
    
    if [y + 1, x] == end:
        maze[y + 1][x] = 2
        mg.maze_visual(maze)
        print("\nB I N G O !\nThe maze S O L V E D !!\n")
        return True
    
    else:
        for move in allowed_moves(pos):
            b = move[0]
            a = move[1]
            if maze[b][a] == 0:
                maze[b][a] = 2
                mg.maze_visual(maze)
                if through_maze(maze, [b, a], end):
                    return True
                maze[b][a] = 3
            
    return False
   

if __name__ == "__main__":
    #Width and height without borders; after adding borders the actual width and height is + 2
    width = 40
    height = 20
    
    start = [0, 1]
    end = [height + 1, width]
    
    m = mg.maze_generate(width, height)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(4):
        print("R E A D Y   T O   G O ???")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
    
    solved = through_maze(m, start, end)
    if not solved:
        print("\nT O U G H   L U C K !\nThe maze is  N O T  solvable. :-(\n")
    # ▪
