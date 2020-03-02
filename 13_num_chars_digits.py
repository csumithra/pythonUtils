#Write a program that accepts a sentence and calculate the number of letters and digits.

#Suppose the following input is supplied to the program:

#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3


data = input("Enter a sentence with text and numbers: ")

digits = 0
letters = 0
print(data)
for val in data :
    if val.isalpha():
        letters += 1
    if val.isdigit():
        digits += 1

print(f"LETTERS = {letters}, DIGITS = {digits}")
