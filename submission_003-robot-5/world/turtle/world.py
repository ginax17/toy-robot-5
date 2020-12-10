import turtle
import random
import world
from maze import mazerunner as the_maze
import sys
import maze

opend = []

# print(obstacles)
turtle_obstacles = []

turtle_reference = turtle.Turtle()
turtle_reference.penup()

# The maze runner / automated turtle robot
Mazerunner = turtle.Turtle()
Mazerunner.color('pink')
Mazerunner.penup()


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def setup_world():
    turtle_reference.penup()
    turtle_reference.goto(-100,200)
    turtle_reference.pendown()
    turtle_reference.color('red')
    turtle_reference.goto(100,200)
    turtle_reference.goto(100,-200)
    turtle_reference.goto(-100,-200)
    turtle_reference.goto(-100,200)
    turtle_reference.penup()

    turtle_reference.home()
    turtle_reference.setheading(90)
    # draw_obstacle(obstacles)    


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def obstacle_check(x,y):
    if maze.mazerunner.is_path_blocked(position_x, position_y, x, y):
        return True
    elif maze.mazerunner.is_position_blocked(x,y):
        return True
    else:
        return False


def update_position(steps, current_direction_index):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        x = obstacle_check(new_x,new_y)
        if x == False:
            position_x = new_x
            position_y = new_y
            turtle_reference.goto(new_x,new_y)
            return True, ''
        else:
            return False, 'obstacle'
    return False, 'border'


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def print_obstacles(obs):
    """Draws the obstacles's x and y coordinates """
    # print(obs)
    turtle_reference.speed(0)
    turtle_reference._delay(0)
    for ob in obs:
        turtle_reference.goto(ob[0],ob[1])
        turtle_reference.pendown()
        turtle_reference.begin_fill()
        for i in range(4):
            turtle_reference.forward(8)
            turtle_reference.left(90)
        turtle_reference.end_fill()
        turtle_reference.penup()
        turtle_reference.home()
        turtle_reference.setheading(90)


def exit_function():
    window.exitonclick()
    sys.exit()


def opend_gate():
    gates = ["l", "b", "t", "r"]
    exit_gate = input('choose an exit gate ["t", "r", "l", "b"] ')
    while exit_gate.lower() not in gates:
        opend_gate()

    return exit_gate.lower()


def run_up(obs):
    if Mazerunner.heading() == 90:
        x_walls = round(Mazerunner.xcor(),0)
        y_walls = round(Mazerunner.ycor(),0)
        if (x_walls, y_walls) in opend:   # check turtle coordinates are at the exit_gate line
            print("Finished")
            exit_function()
        if (x_walls -8, y_walls ) in obs:  # check to see if they are obstacles on the left
            if (x_walls, y_walls + 8) not in obs:
                Mazerunner.forward(8)
            else:
                Mazerunner.right(90)
        else:
            Mazerunner.left(90)
            Mazerunner.forward(8)


def run_down(obs):
    if Mazerunner.heading() == 270:                   # check to see if the sprite is pointing down
        x_walls = round(Mazerunner.xcor(),0)          # sprite x coordinates =
        y_walls = round(Mazerunner.ycor(),0)
        if (x_walls, y_walls) in opend:          # if sprite and the
            print("Finished")
            exit_function()
        if (x_walls +8, y_walls) in obs:          # check to see if they are obstacles on the left
            if(x_walls, y_walls -8) not in obs:   # check to see if path ahead is clear
                Mazerunner.forward(8)
            else:
                Mazerunner.right(90)
        else:
            Mazerunner.left(90)
            Mazerunner.forward(8)


def run_left(obs):
    if Mazerunner.heading() == 0:
        x_walls = round(Mazerunner.xcor(),0)
        y_walls = round(Mazerunner.ycor(),0)
        if (x_walls, y_walls) in opend:   # check turtle coordinates are at the exit_gate line
            print("Finished")
            exit_function()
        if (x_walls, y_walls +8) in obs:       # check to see if they are obstacles on the left
            if(x_walls +8, y_walls) not in obs:
                Mazerunner.forward(8)
            else:
                Mazerunner.right(90)
        else:
            Mazerunner.left(90)
            Mazerunner.forward(8)


def run_right(obs):
    if Mazerunner.heading() == 180:

        x_walls = round(Mazerunner.xcor(),0)
        y_walls = round(Mazerunner.ycor(),0)
    
        if (x_walls, y_walls) in opend:   # check turtle coordinates are at the exit_gate line
            print("Finished")
            exit_function()
        if (x_walls, y_walls -8) in obs:  # check to see if they are obstacles on the left
            if (x_walls - 8, y_walls) not in obs:
                Mazerunner.forward(8)
            else:
                Mazerunner.right(90)
        else:
            Mazerunner.left(90)
            Mazerunner.forward(8)



def mazerunner_main(gate):
    # window = turtle.Screen()
    # window.setup(400, 600)
    # window.bgcolor("black")
    # window.title("mazerunner")
    global opend
    obs = the_maze.obstacles_list
    setup_world()               # setup the screen
    print_obstacles(obs)        # print the maze walls

    # print(obs)
    turtle_reference.hideturtle()
    Mazerunner.setposition(the_maze.turtle_home[0])
    opend = the_maze.open_exit(gate)
    while Mazerunner.position() != opend:
        Mazerunner.speed(0)
        Mazerunner._delay(4)
        run_left(obs)
        run_up(obs)
        run_right(obs)
        run_down(obs)


    turtle.done()
    return False

if __name__ == "__main__":
    mazerunner_main()