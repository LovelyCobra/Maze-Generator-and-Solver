import sys, os, time, random

#Helper function to visualize the maze
def maze_visual(maze):
    w = len(maze[0])
    h = len(maze)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nGRAND MINOTAURUS MAZE:\n")
    for line in range(h):
        l = ""
        for posit in range(w):
            if maze[line][posit] == 0 or maze[line][posit] == 3:
                l = l + " "
            elif maze[line][posit] == 1:
                l = l + "█"
            else:
                l = l + "*"
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
    
    w = len(maze[0])
    h = len(maze)
    alm = allowed_moves(mpos)
    alm.remove(pos)
    
    for m in alm:
        b = m[0]
        a = m[1]
        if maze[b][a] == 0 or b not in range(h-1) or a not in range(w-1):
            return False
    return True

#Generating a list of valid moves from a position
def valid_move_list(maze, pos):
    vml = []
    for move in allowed_moves(pos):
        if valid_move(maze, pos, move):
            vml.append(move)
    return vml

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
    
    #Initial early_pos and position
    e_p = [0, 1]
    p_s = [1, 1]
    
    maze_visual(maze)
    time.sleep(0.5)
    #List of randomly generated passages (placemets of zeros) in the maze (i.e excluding the first two above)
    passages = []
    switch = False
    #making randomly winding passages through the base, one main, leading from the start to the end, and N branches with dead ends
    while True:
                
        while len(valid_move_list(maze, p_s)) > 0:
            m_list = valid_move_list(maze, p_s)
            
            l = len(m_list) - 1
            ind = random.randint(0, l)
            move = m_list[ind]
            y = move[0]
            x = move[1]
            maze[y][x] = 0
            e_p = p_s
            p_s = [y, x]
            passages.append(p_s)
            maze_visual(maze)
        
        
        if p_s[0] > height - 7 and  p_s[1] > width - 7:
            switch = True
        
        lgth = len(passages)
        
        if switch and lgth > height * width * 7 // 12:
            break
        index = random.randint(2, lgth - 2)
        p_s = passages[index]
        e_p = passages[index-1]
        
    yy = height
    xx = width-1
    while maze[yy][xx] == 1:
        maze[yy][xx] = 0
        maze_visual(maze)
        xx -= 1
        if maze[yy][xx] == 0 or maze[yy][xx-1] == 0:
            break
        maze[yy][xx] = 0
        maze_visual(maze)
        time.sleep(0.5)
        yy -= 1
        
    return maze
    
    
if __name__ == "__main__":
    #Width and height of the maze, not counting borders all around
    width = 60
    height = 40
    
    m = maze_generate(width, height)
    
    #maze_visual(m)
