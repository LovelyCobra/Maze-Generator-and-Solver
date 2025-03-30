import os, time, random, re
from maze_generator import *
from cobraprint import *
import input_valid as iv
from input_valid import *


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
        
#Generating a list of possible moves from a position
def allowed_moves(pos):
    x = pos[0] #Row from the top down
    y = pos[1] #Position from the left to the right
    
    return [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]


#The main recursive function with backtracking        
def through_maze(maze, pos, end):
    h = len(maze)    #Maze's height, corresponds to "x"
    
    #Coordinates within the maze
    x = pos[0] #Row from the top down, starting from 1
    y = pos[1] #Position from the left to the right, starting from 1
    
    #Base case
    print(cur_pos_abs(x, y)+col.RED+"▪"+col.END)
    time.sleep(.04)
    
    if [x + 1, y] == end and maze[x-3][y-1] == 0:
        print(cur_pos_abs(x + 1, y)+col.RED+"▪"+col.END+cur_down_start(h + 4 - x))
        print(f"\n{col.BLUE}{style.rapid_blink}B I N G O !{res_all}\nThe maze {col.GREEN}S O L V E D !! ☺{col.END}\n")
        return True
    
    else:
        for move in allowed_moves(pos):
            b = move[0] # Corresponds to "x"
            a = move[1] # Corresponds to "y"
            if maze[b-4][a-1] == 0:
                print(cur_pos_abs(b, a)+col.RED+"▪"+col.END)
                maze[b-4][a-1] = 2
                
                if through_maze(maze, [b, a], end):
                    return True
                print(cur_pos_abs(b, a)+col.GREY+"█"+col.END)
                maze[b-4][a-1] = 3
                time.sleep(.04)
       
    return False


if __name__ == '__main__':
    
    os.system('cls' if os.name == 'nt' else 'clear')
    # statement = f"\nWelcome to {col.MAGENTA}GRAND MINOTAURUS MAZE{col.END}\n\nIf you wish the maze to be generated randomly, type your chosen {col.GREY}width{col.END} and {col.GREY}height{col.END} of the maze \nas {col.GREY}2 positive integers greater than 10 and lesser than the width and the height of your screen \n(recommended size: 35, 20), separated by {col.RED}', '{col.END} \n    and press {col.GREEN}ENTER{col.END}.\n\nOtherwise input your own maze (as a {col.GREY}2D list of zeros and ones{col.GREY}, \nwhere zeros are free passages and ones represent walls){col.END}\n    and only then press {col.GREEN}ENTER{col.END}:\n\n"
    # regex = "\d+, \d+"
    # value = (10, 60)
    
    inp = input(f"\nWelcome to {col.MAGENTA}GRAND MINOTAURUS MAZE{col.END}\n\nIf you wish the maze to be generated randomly, type your chosen {col.GREY}width{col.END} and {col.GREY}height{col.END} of the maze \nas {col.GREY}2 positive integers greater than 10 and lesser than the width and the height of your screen \n(recommended size: 35, 20), separated by {col.RED}', '{col.END} \n    and press {col.GREEN}ENTER{col.END}.\n\nOtherwise input your own maze (as a {col.GREY}2D list of zeros and ones{col.GREY}, \nwhere zeros are free passages and ones represent walls){col.END}\n    and only then press {col.GREEN}ENTER{col.END}:\n\n")
    
    # inp = iv.valid_input(statement, regex, value)
    
    # if inp:
    #     width, height = inp
    if re.search("\d\d, \d\d", inp):
        [width, height] = [int(item) for item in inp.split(', ')]
        maze = maze_generate(width, height)
        
        for _ in range(3):
            ready(height)
            time.sleep(.7)
            maze_visual(maze)
            time.sleep(.7)
            
    else:
        # Converting the input as a single string into a 2D list of zeros and ones
        maze = []
        input = inp[2:-2].split('], [')
        for line in input:
            l = [int(item) for item in line.split(', ')]
            maze.append(l)
        maze_visual(maze)
        time.sleep(1)
    
    width = len(maze[0])
    height = len(maze)
    
    # Start position
    x = 4
    y = 2
    pos = [x, y]
    
    # End position
    end = [height + 3, width - 1]
    
    
    solved = through_maze(maze, pos, end)
    if not solved:
        print(cur_down_start(height + 4 - x)+col.RED+style.rapid_blink+"T O U G H   L U C K !"+res_all+"\nThe maze is  N O T  solvable. :-( ☺\n")     
    