secret = 15
count = 0

while True:
    guess = int(input("Guess the secret number: "))
    count += 1

    if guess == secret:
        print("Correct")
        print("count:", count)
        break
    else:
        print("Wrong Try again.")