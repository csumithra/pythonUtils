#Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:

#D 100
#W 200
#D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:

#D 300
#D 300
#W 200
#D 100
#Then, the output should be: 500

total = 0

while True:
    data = input()
    if len(data) == 0:
        break

    values = data.split(' ')
    if values[0] == 'D':
        total += int(values[1])
    if values[0] == 'W':
        total -= int(values[1])


print(total)