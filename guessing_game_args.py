from random import randint

print("start here")

try:
    lower = int(input("Enter lower bound for guessing game: "))
except ValueError:
    print("Please enter a number")

try:
    upper = int(input("Enter upper bound for guessing game: "))
    if upper < lower:
        print(f"Enter a number greater than {lower}")
    print(lower, upper)

    answer = randint(lower, upper)
    print(answer)
except ValueError:
    print("Please enter a number for upper bound")

while True:
    try:
        guess = int(input(f"Enter a number between {lower} and {upper}: "))
        if guess > lower and guess < upper:
            if guess == answer:
                print("You guessed it right!")
                break
        else:
            print(f"You need to enter a number between {lower} and {upper}")
    except ValueError as e:
        print("Exception: Please enter a number.", e)
        continue
