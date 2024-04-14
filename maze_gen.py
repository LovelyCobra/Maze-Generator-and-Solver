import os, time, random

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    
def ready(height):
    n = (height - 8) // 2
    for n in range(4):
        print("\n")
        
    print(colors.CYAN + "██████      ███████      ██      ███████  ██     ██    ███████" + colors.END)
    print(colors.CYAN + "██    ███   ██         ██  ██    ██    ██  ██   ██    ██     ██" + colors.END)
    print(colors.CYAN + "██     ███  ██         ██  ██    ██     ██  ██ ██             ██" + colors.END)
    print(colors.CYAN + "██    ███   █████     ██    ██   ██      ██  █ █          █████" + colors.END)
    print(colors.CYAN + "██████      ██       ██      ██  ██      ██  ███         ██" + colors.END)
    print(colors.CYAN + "██  ██      ██       ██████████  ██     ██   ███         ██" + colors.END)
    print(colors.CYAN + "██   ██     ██      ██        ██ ██    ██    ███" + colors.END)
    print(colors.CYAN + "██    ███   ███████ ██        ██ ███████     ███         ██" + colors.END)
    
#Helper function to visualize the maze
def maze_visual(maze):
    w = len(maze[0])
    h = len(maze)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nGRAND MINOTAURUS MAZE:\n")
    for line in range(h):
        l = ""
        for posit in range(w):
            if maze[line][posit] == 0:
                l = l + " "
            elif maze[line][posit] == 1:
                l = l + "█"
            elif maze[line][posit] == 3:
                l = l + colors.GREEN + "█" + colors.END
            else:
                l = l + "x"
        print(l)
    time.sleep(0.02)

#Generating a list of possible moves from a position
def allowed_moves(pos):
    y = pos[0] #Row from the top down
    x = pos[1] #Position from the left to the right
    
    return [[y + 1, x], [y, x + 1], [y - 1, x], [y, x - 1]]

#Establishing whether a move from a reached position is valid, i.e fulfilling border and "non-connecting" conditions
def valid_move(maze, pos, mpos):
    y = pos[0]
    x = pos[1]
    yy = mpos[0] #Row from the top down
    xx = mpos[1] #Position from the left to the right
    
    w = len(maze[0])  #Maze width
    h = len(maze)     #Maze height
    alm = allowed_moves(mpos)  #Allowed moves from the position of the move
    alm.remove(pos)            #Removing the reached position from the allowed moves, thus preventing the backward move
    
    for m in alm:
        b = m[0]
        a = m[1]
        if b not in range(h) or a not in range(w): #Keeping the created passages away from borders
            return False
        if maze[b][a] == 0:         #Preventing a newly created passage to connect to a previously connected passage
            return False
    return True

#Generating a list of valid moves from a position
def valid_move_list(maze, pos):
    vml = []
    for move in allowed_moves(pos):
        if valid_move(maze, pos, move):
            vml.append(move)
    return vml

#THE MAIN FUNCTION generating the maze
def maze_generate(width, height):
    maze = []
    border = [1 for i in range(width)]
    top_row = [1, 0]
    top_row.extend(border.copy())
    bottom_row = border.copy()
    bottom_row.extend([0, 1])
    maze.extend([top_row, top_row.copy()])
    
    body = [1 for j in range(width + 2)]
    
    #pre-generating the base for the maze, made of only walls at first, and start and end openings
    for i in range(height - 2):
        maze.append(body.copy())
    maze.extend([bottom_row, bottom_row.copy()])
    maze_visual(maze)
    time.sleep(0.5)
    
    #Initial position
    p_s = [1, 1]
    
    #List of randomly generated passages (placemets of zeros) in the maze (i.e excluding the first and the last one)
    passages = []
   
    #cutting randomly winding passages through the base
    while True:
        while len(valid_move_list(maze, p_s)) > 0:
            m_list = valid_move_list(maze, p_s)
            
            l = len(m_list) - 1
            ind = random.randint(0, l)
            move = m_list[ind]
            y = move[0]
            x = move[1]
            maze[y][x] = 0
            p_s = [y, x]
            passages.append(p_s)
            maze_visual(maze)
        
        lgth = len(passages)
        
        if lgth > height * width * 7 // 12:
            break
        index = random.randint(2, lgth - 2)
        p_s = passages[index]
        
    j = random.randint(0, 2)
    if j == 0:
        maze[height][width-1] = 0
    elif j == 1:
        maze[height-1][width] = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    
    with open("maze_container.txt", "a") as file:
        file.write(str(maze))
    
    maze_visual(maze)
    time.sleep(2)
    
        
    return maze
    
if __name__ == "__main__":
    #Width and height of the maze, not counting borders all around
    width = 60
    height = 40
    
    m = maze_generate(width, height)
