#Write a method which can calculate square value of number

def square_num(num):
    '''
    Returns the square value of the input number.
    '''
    return num ** 2

print(square_num.__doc__)

print(square_num(int(input('Enter a number: '))))

