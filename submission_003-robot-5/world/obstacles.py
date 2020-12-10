import random

obstacle = []

def obstacles():
    """Gets a list of obstacles at random"""
    global obstacle
    obstacle = []
    list_obsticles = []
    random_positioned_obsticle = random.randint(1,10)
    #print(random_positioned_obsticle)
    for each_positioned_obsticle in range(random_positioned_obsticle):
        list_obsticles.append((random.randint(-100,100),random.randint(-200,200)))
    obstacle = list_obsticles
    return list_obsticles


def block_list(i):
    the_list = []
    for x in range(i[0],i[0]+5):
        for y in range(i[1],i[1]+5):
            obstacle_tuple = x,y
            the_list.append(obstacle_tuple)
    return the_list



def is_position_blocked(x,y):
    """The function returns true if the position (x,y) falls inside an obstacle"""
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
    """This function returns true if there is an obstacle in the line between the coordinates (x1, y1) and (x2, y2)."""
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

     
    
    






















































