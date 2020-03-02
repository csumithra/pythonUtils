from random import randint


answer = randint(1,10)
print(answer)



while True:
    try:
        guess = int(input("Enter a number between 1 and 10: "))
        if guess > 0 and guess < 10:
            if guess == answer:
                print("You guessed it right!")
                break
        else:
            print("You need to enter a number between 1 and 10")
    except ValueError as e:
        print("Exception: Please enter a number.", e)
        continue
