#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.

#D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:

#100,150,180
#The output of the program should be: 18,22,24

import numpy as np
C, H = 50, 30

D = input("Enter numbers separated by commas: ").split(',')
Q= []

for i in D:
    Q.append(str(np.sqrt((2 * C * float(i))/H)))

print(','.join(Q))



