# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# Then, the output of the program should be: 2.23606



import math
pos = [0,0]

while True:
    s = input()

    if len(s) == 0:
        break
    activity = s.split(" ")

    direction = activity[0]
    steps_taken = int(activity[1])

    if direction == 'UP':
        pos[0] += steps_taken
    elif direction == 'DOWN':
        pos[0] -= steps_taken
    elif direction == 'LEFT':
            pos[1] -= steps_taken
    elif direction == 'RIGHT':
        pos[1] += steps_taken
    else:
        pass

print(pos)

print(math.sqrt(pos[0]**2 + pos[1]**2))