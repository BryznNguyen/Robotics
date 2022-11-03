#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from const import *
from motor_control import *
from path_plan import return_path
import time 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

class Node():
    def __init__(self, block=None, position=None):
        self.block = block
        self.position = position

        self.g = 0 #G = distance from the start point
        self.h = 0 #H = distance from the end point
        self.f = 0 #F = G + H

    def __eq__(self, other):
        return self.position == other.position


def astar(course, start, end):
    # assigning start and end node
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = 0
    end_node = Node(None, end)
    end_node.g = 0
    end_node.h = 0
    end_node.f = 0
    debug = 0

    # init open and closed list
    # open meaning set of blocks that havent been looked at
    # closed meaning set blocks that have been accessed
    open = []
    closed = []

    # Add the start node
    open.append(start_node)

    # Loop until you find the end
    while len(open) > 0:

        # gets the node at the top of the list
        current_node = open[0]
        current_index = 0
        for index, item in enumerate(open):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # gets rid of current in the open ist instead adding it to the closed list
        open.pop(current_index)
        closed.append(current_node)
        debug = debug + 1
        print(debug)
        # if the path finds the end point
        if current_node == end_node:
            print("found end")
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.block

            path.reverse() # reverses the list from start to finish
            return path

        # blocks near the current block
        neighbors = []      # looks for all  the surrounding squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(course) - 1) or node_position[0] < 0 or node_position[1] > (len(course[len(course)-1]) -1) or node_position[1] < 0:
                continue

            # if the current block course is not an obstacle
            if course[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            neighbors.append(new_node)

        # look through the neighbors
        for neighbor in neighbors:
            for close in closed:
                if neighbor == close:
                    continue

            # assign the f g h values
            neighbor.g = current_node.g + 1
            neighbor.h = ((neighbor.position[0] - end_node.position[0]) ** 2) + ((neighbor.position[1] - end_node.position[1]) ** 2)
            neighbor.f = neighbor.g + neighbor.h

            # neighbor is already in the open list
            for open_node in open:
                if neighbor == open_node and neighbor.g > open_node.g:
                    continue

            # otherwise add to the open list
            open.append(neighbor)

def move (path,course):
    #if only x is increasing move UP
    #if only x is decreasing move BACK
    #if only y is increasing rotate 90 right and move down
    #if only y is decreasing rotate 90 left and move up
    #if x and y increase rotate 45 right and move up
    #if x and y decrease rotate 45 right and move back

    #square is 0.305m across and 0.431m diagonal
    distance = 0

    dis = "distance: "
    for idx, x in enumerate(path):
        if (idx + 1 < len(path)):
            current = x
            next = path[idx+1]
            result = tuple(map(lambda i,j: i - j, next, current))
            pnt = "move "
            print(pnt,idx+1)
            
            if (result == (0,1)):
                print("move forward")
                distance += .305
                print("%s %.3f " % (dis, distance))
                move_forward90()
                
            elif (result == (0,-1)):
                print("move backwards")
                distance += .305
                print("%s %.3f " % (dis, distance))
                move_backwards90()
            elif (result == (1,0)):
                print("rotate 90 right and move up then rotate back")
                distance += .305
                print(dis, distance)
                turn_right90()
                move_forward90()
                turn_left90()
            elif (result == (-1,0)):
                print("rotate 90 left and move back then rotate back")
                distance += .305
                print("%s %.3f " % (dis, distance))
                turn_left90()
                move_forward90()
                turn_right90()
            elif (result == (1,1)):
                print("rotate 45 right")
                distance += .431
                print("%s %.3f " % (dis, distance))
                
                y1 = path[idx][0] +1 
                x1 = path[idx][1] +0 

                y2 = path[idx+1][0] +0
                x2 = path[idx+1][1] +1


                if(course[y1][x1] == 1):
                    move_forward90()
                    turn_right90()
                    move_forward90()
                    turn_left90()
                    print("1 U R U L")
                    dummy = 0

                elif(course[y2][x2] == 1):
                    turn_right90()
                    move_forward90()
                    turn_left90()
                    move_forward90()
                    print("2 R U L U")
                    dummy = 0
                else:
                    turn_right90()
                    move_forward90()
                    turn_left90()
                    move_forward90()
                    print("3 R U L U")
                    dummy = 0


            elif (result == (-1,1)):
                print("rotate 45 left")
                distance += .431
                print("%s %.3f " % (dis, distance))

                y1 = path[idx][0] +0 
                x1 = path[idx][1] +1 

                y2 = path[idx+1][0] -1
                x2 = path[idx+1][1] +0

                #print(y)
                #print(x)
                #print("object at ",course[y][x])
                if(course[y1][x1] == 1):
                    turn_left90()
                    move_forward90()
                    turn_right90()
                    move_forward90()
                    dummy = 0
                    print("1 L U R U")

                elif(course[y2][x2] == 1):
                    move_forward90()
                    turn_left90()
                    move_forward90()
                    turn_right90()
                    dummy = 0
                    print("2 U L U R")
                else:
                    move_forward90()
                    turn_left90()
                    move_forward90()
                    turn_right90()
                    print("3 U L U R")

            elif (result == (1,-1)):
                print("rotate 45 left")
                distance += .431
                print("%s %.3f " % (dis, distance))

                move_forward90()
                turn_left90()
                move_forward90()
                turn_right90()

                #turn_left45()
                #move_backwards45()
                #turn_right45()
            elif (result == (-1,-1)):
                print("rotate 45 right and move back then rotate back")
                distance += .431
                print("%s %.3f " % (dis, distance))
                move_forward90()
                turn_right90()
                move_forward90()
                turn_left90()
                
    

def main():
    #0 represents free space
    #1 represents obstacles points
    #2 represents obstacle cushion
    start = (8, 1)  # start
    end = (4, 12)  # end
    #(y,x)
    course = [[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0
              [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
              [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2 
              [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
              [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #4
              [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], #5
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], #6
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], #7
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
              [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] #10
    

    path = astar(course, start, end)
   # print(path)
   # path =[(8, 1), (7, 1), (6, 1), (5, 1), (4, 2), (4, 3), (5, 4), (6, 4), (7, 4), (8, 5), (7, 6), (6, 7), (5, 8), (4, 8), (3, 8), (2, 9), (3, 10), (4, 11)]  
    move(path,course)

if __name__ == '__main__':
   #
    main()
    ev3.speaker.beep()
    ev3.speaker.beep()

    
   # turn_left45()
   # move_forward45()
   # turn_right45()
   # move_forward90()
   # turn_left45()
   # move_forward45()
   # turn_right45()
    
   # time.sleep(5)
    

 


