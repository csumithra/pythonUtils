#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#Suppose the following input is supplied to the program: 9
#Then, the output should be: 11106


num = input("Enter a number : ")

print(int(num)+ int(num + num) + int(num+num+num) + int(num+num+num+num))

