import random
import turtle
import robot

obstacle = []
turtle_home = []
obstacles_list = []
top_exit = []
left_exit = []
bottom_exit = []
right_exit = []

def obstacles():
    """Gets a list of obstacles at random"""
    global obstacle, obstacles_list, turtle_home, turtle_exit
    exit_gate = "none"
 
    maze = [
            
            'aaaaaaaaaattaaaaaaaaaaaaaa',
            'a  a              a      a',
            'a              a         a',
            'a   aaaa   a   aaaaa aaaaa',
            'a      a   a           a a',
            'a  a   aaaa  aaaaaaa   a a',
            'a  a    a      a       a a',
            'a  aaaaaaaaa   a   aaaaa a',
            'a          a   a         a',
            'a  aaaaa   aaaa   a  aaaaa',
            'a      a a   a   a a     a',
            'a    a   aaaaa   a   aa  a',
            'a              a         a',
            'a  aaaaa   a     aaaaaaa a',
            'a  a       aa      a   a a',
            'a  a   aaaa a  aaaaa   a r',
            'a  a     a     a   a     r',
            'a  aaaaaaaaa   a   a   a a',
            'a  a           a   a   a a',
            'a  a   aaaaaa  a   a   a a',
            'a  a    a              aza',
            'a  aaaaaaaaa   a   aaaaa a',
            'a          a  a          a',
            'a  aaaaa   aaaa   a  aaaaa',
            'a      a a   a   a a     a',
            'aa   a   aaaaa   a   aa  a',
            'a   a          a         a',
            'a  aaaaa   a     aaaaaaa a',
            'a  a                a  a a',
            'a  a   aaaa  aaaaaaa   a a',
            'a              a   aaaaa a',
            'a          a   a         a',
            'a      a a   a   a a     a',
            'aa   a   aaaaa   a   aa  a',
            'a      a   a           a a',
            'l  a   aaa  a aaaaaa   a a',
            'l  a    a      a       a a',
            'a  aaaaaaaaa   a   aaaaa a',
            'a              a         a',
            'a  aaaaa   aaaa   a  aaaaa',
            'a      a a   a   a a     a',
            'a   a          a         a',
            'a  aaaaa   a     aaaaaaa a',
            'a  a       aa       a  a a',
            'a  a                   a a',
            'a  a       a a       a   a',
            'a  a                 a   a',
            'a  a                 a   a',
            'aaaaaaaaaaabbaaaaaaaaaaaaa'
            
    ]
    gates = ["l", "b", "t", "r"]
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            screen_x = -100 + (x*8)
            screen_y = 200 - (y*8) - 8
            if maze[y][x] == "a":
                obstacles_list.append((screen_x,screen_y))
            elif maze[y][x] == "z":
                turtle_home.append((screen_x,screen_y))
            elif maze[y][x] == "t":
                top_exit.append((screen_x,screen_y))
            elif maze[y][x] == "r":
                right_exit.append((screen_x,screen_y))
            elif maze[y][x] == "b":
                bottom_exit.append((screen_x,screen_y))
            elif maze[y][x] == "l":
                left_exit.append((screen_x,screen_y))
            elif maze[y][x] in gates and maze[y][x] != exit_gate:
                obstacles_list.append((screen_x,screen_y))
    return obstacles_list

    # obstacle = []
    # list_obsticles = []
    random_positioned_obsticle = random*randint(1,10)
    #print(random_positioned_obsticle)
    for each_positioned_obsticle in range(random_positioned_obsticle):
        list_obsticles.append((random*randint(-100,100),random*randint(-200,200)))
    obstacle = list_obsticles
    return list_obsticles

def open_exit(gate):
    """Navigates to the four positions 
    if the user selects the specified position"""
    if gate == "top":
        opend = top_exit
    if gate == "left":
        opend = left_exit
    if gate == "bottom":
        opend = bottom_exit
    if gate == "right":
        opend = right_exit
    for obstacle in obstacles_list:
        if obstacle in opend:
            obstacles_list.remove(obstacle)

    return opend

def block_list(i):
    the_list = []
    for x in range(i[0],i[0]+5):
        for y in range(i[1],i[1]+5):
            obstacle_tuple = x,y
            the_list.append(obstacle_tuple)
    return the_list



def is_position_blocked(x,y):
    """The function returns true 
    if the position (x,y) falls inside an obstacle"""
    # if obstacles in range(x ,x + 4) and obstacles in range(y,y + 4):
    #     return True
    # else:
    #     return False
    block_total_list = []
    for i in obstacle:
        block = block_list(i)
        block_total_list += block
    co_ord = x,y
    for i in block_total_list:
        if i == co_ord:
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """This function returns true if there is an obstacle 
    in the line between the coordinates (x1, y1) and (x2, y2)*"""
    # if x1==x2 or y1==y2:
    #     return True
    # else:
    #     return False
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if is_position_blocked(x,y):
                return True
    return False

def get_obstacles():
    return obstacles()
 
