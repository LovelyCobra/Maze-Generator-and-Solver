import os, time, random
from cobraprint import *

def ready(height):
    n = height//2 - 3
   
    print(cur_pos_abs(n, 1) + " "*67)
    print(67 * " ")    
    print(col.CYAN + " ██████      ███████      ██      ███████  ██     ██    ███████    " + col.END)
    print(col.CYAN + " ██    ███   ██         ██  ██    ██    ██  ██   ██    ██     ██   " + col.END)
    print(col.CYAN + " ██     ███  ██         ██  ██    ██     ██  ██ ██             ██  " + col.END)
    print(col.CYAN + " ██    ███   █████     ██    ██   ██      ██  █ █          █████   " + col.END)
    print(col.CYAN + " ██████      ██       ██      ██  ██      ██  ███         ██       " + col.END)
    print(col.CYAN + " ██  ██      ██       ██████████  ██     ██   ███         ██       " + col.END)
    print(col.CYAN + " ██   ██     ██      ██        ██ ██    ██    ███                  " + col.END)
    print(col.CYAN + " ██    ███   ███████ ██        ██ ███████     ███         ██       " + col.END)
    print(67 * " ")
    print(67 * " ")
    
    

#Helper function to visualize the maze
def maze_visual(maze):
    w = len(maze[0])
    h = len(maze)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{col.MAGENTA}GRAND MINOTAURUS MAZE:{col.END}\n")
    for line in range(h):
        l = ""
        for posit in range(w):
            if maze[line][posit] == 0:
                l = l + " "
            elif maze[line][posit] == 1:
                l = l + "█"
            elif maze[line][posit] == 3:
                l = l + col.GREY + "█" + col.END
            else:
                l = l + col.RED + "▪" + col.END
        print(l)
        
def allowed_moves(pos):
    x = pos[0] #Row from the top down
    y = pos[1] #Position from the left to the right
    
    return [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]

#Establishing whether a move from a reached position is valid, i.e fulfilling border and "non-connecting" conditions
def valid_move(maze, pos, mpos):
    
    w = len(maze[0])  #Maze width
    h = len(maze)     #Maze height
    
    # 'pos' = position already reached; 
    # 'mpos' = potential next position, that needs to be checked first for border and "non-connecting" condition to establish 
    # whether it is a "valid move" (i.e the positions SURROUNDING it need to be checked)
    
    alm = allowed_moves(mpos)  #Allowed moves from the potential next position
    alm.remove(pos)            #Removing the reached position from the allowed moves, thus preventing the backward move
    
    for m in alm:
        b = m[0]
        a = m[1]
        if b not in range(h) or a not in range(w): #Keeping the created passages away from borders
            return False
        if maze[b][a] == 0:         #Preventing a newly created passage to connect to a previously created passage
            return False
    return True

#Generating a list of valid moves from a position
def valid_move_list(maze, pos):
    vml = []
    for move in allowed_moves(pos):
        if valid_move(maze, pos, move):
            vml.append(move)
    return vml

#########################################
# THE MAIN FUNCTION generating the maze #     along with the visualization of the process
#########################################

def maze_generate(width, height):
    maze = []
    border = [1 for i in range(width)]
    top_row = [1, 0]
    top_row.extend(border.copy())
    bottom_row = border.copy()
    bottom_row.extend([0, 1])
    maze.extend([top_row, top_row.copy()])
    
    body = [1 for j in range(width + 2)]
    
    #pre-generating the base for the maze, made of only walls at first, and start and end (exit) openings
    for _ in range(height - 2):
        maze.append(body.copy())
    maze.extend([bottom_row, bottom_row.copy()])
    maze_visual(maze)
    time.sleep(0.5)
    
    #Initial position
    p_s = [1, 1]
    
    #List of randomly generated passages (placemets of zeros) in the maze (i.e excluding the first and the last one)
    passages = []
   
    # Cutting randomly winding passages through the base; all created branches are dead ends
    while True:
        while len(valid_move_list(maze, p_s)) > 0:
            m_list = valid_move_list(maze, p_s)
            
            move = random.choice(m_list)
            x = move[0]
            y = move[1]
            maze[x][y] = 0
            p_s = [x, y]
            passages.append(p_s)
            print(cur_pos_abs(x+4, y+1)+" ")
            time.sleep(.02)
        
        lgth = len(passages)
        
        if lgth > height * width * 7 // 12:
            break
        p_s = random.choice(passages[2:-2])
    
    
    # Randomly choosing between creating opening above or to the left of the exit passage, or leaving it unconnected. 
    # This part decides whether the maze is solvable (which is between a third and half of the time depending on the size of the maze) or not.
    
    j = random.randint(0, 2)
    if j == 0:
        maze[height][width-1] = 0
        print(cur_pos_abs(height+4, width)+" ")
    elif j == 1:
        maze[height-1][width] = 0
        print(cur_pos_abs(height+3, width+1)+" ")
    
    # Saving the resulting maze in the text file "maze_container.txt"
    with open("maze_container.txt", "a") as file:
        file.write(str(maze))
        file.write("\n\n")
    
    time.sleep(2)
        
    return maze

if __name__ == '__main__':
    pass
