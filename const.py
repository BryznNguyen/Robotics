#============================================================
#
#                         Project 1
#               CSE 4360 - Robotics 
#            The University of Texas at Arlington
#            
#============================================================
#            Authors:
#            Preston Mann 1001677983 
#            Bryan Nguyen 1001719605
#============================================================
#
# File: main.py
#
# Brief: this file has all the constant values for the robot
#        all constant values for turning and moving are here
#        this file is missing the values for start and goal positnons and the map
#
# Revision History:
# Date       | Engineer     | Description
# -----------|--------------|--------------------------------
# 11-2-2022  | Bryan, N     | Initial Release
# 11-2-2022  | Preston, M   | Initial Release
#
#============================================================

import math
turning_time = 1525
off_set45 = 120
#off_set90= 120
off_set90 = 5

movement_time90 = 1235*2
movement_time45 = movement_time90*math.sqrt(2)-60
#60 was better than 80
wheel_diameter = 120
# this value was wheel_diameter in cm but then changed by 100 to slow down the car 

wheel_circumference = wheel_diameter * 3.14159
circumferences = 300 / wheel_circumference
movement_speed = total_degrees = circumferences * 360
turning_speed = total_degrees / 2

start_location = (0.305, 1.219)
goal_location = (3.658, 1.829)

obsticales = [(0.61, 2.743),(0.915, 2.743),(1.219, 2.743),(1.829, 1.219),
              (1.829, 1.524),( 1.829, 1.829), (1.829, 2.134),(2.743, 0.305),
              (2.743, 0.61),(2.743, 0.915),(2.743, 2.743),(3.048, 2.743),
              (3.353, 2.743)]

# double obstacle[MAX_OBSTACLES][2] = /* obstacle locations */
# {{0.61, 2.743},{0.915, 2.743},{1.219, 2.743},{1.829, 1.219},#
# {1.829, 1.524},{ 1.829, 1.829}, {1.829, 2.134},{2.743, 0.305},
# {2.743, 0.61},{2.743, 0.915},{2.743, 2.743},{3.048, 2.743},
# {3.353, 2.743},
# {-1,-1},{-1,-1},{-1,-1},{-1,-1},{-1,-1},{-1,-1},{-1,-1},{-1,-1},{-1,-1},
# {-1,-1},{-1,-1},{-1,-1}}


#obsticales_blocks = obsticales
#i = 0
#for _ in obsticales:
 #   obsticales_blocks[i] = ( int(round(float(obsticales_blocks[i][0])/.305,0)), int(round(float(obsticales_blocks[i][1])/.305,0)))
  #  i += 1
#map = [[0 for x in range(16+1)] for y in range(10+1)]

#i = 0
#print(obsticales_blocks)
#for _ in obsticales_blocks:
 #   x = int(obsticales_blocks[i][0])
  #  y = int(obsticales_blocks[i][1])
   # print(obsticales_blocks[i][0],obsticales_blocks[i][1])
    #map[y][x] = 1
    #i = i + 1


#for _ in map:
    #print(_)  

O = 0 #represents free space
X = 1 #represents bstace
S = 2 #start
N = 3 #end



mapped = [[O, O, O, O, O, O, O, X, O, O, O, O, O, O, O],
          [O, O, O, O, O, O, O, X, O, O, O, O, O, O, O],
          [O, O, O, O, O, O, O, X, O, O, O, O, O, O, O],
          [O, S, O, O, O, X, O, O, O, O, O, O, O, O, O],
          [O, O, O, O, O, X, O, O, O, O, O, O, O, O, O],
          [O, O, O, O, O, X, O, O, O, O, N, O, O, O, O],
          [O, O, O, O, O, X, O, O, O, O, O, O, O, O, O],
          [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O],
          [O, X, X, X, O, O, O, X, X, X, O, O, O, O, O],
          [O, O, O, O, O, O, O, O, O, O, O, O, O, O, O]]

