#Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320


def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)


print(fact(8))

'''
8*fact(7)
7*fact(6)
6*fact(5)
5*fact(4)
4*fact(3)
3*fact(2)
2*fact(1)
1*(fact(0))
1
'''
