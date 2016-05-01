import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    
    max = -1
    index = -1
    
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0.
        if mountain_h > max:
            max = mountain_h
            index = i
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # The number of the mountain to fire on.
    print index
