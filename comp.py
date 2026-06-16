import random
# sec = random.randint(1,100)
# print(f"Your random number is {sec}")

num =random.randint(1,10)
while True:
    guess=int(input("Enter a number, what is in your mind?"))

    if guess == num:
        print("You guess the currect number")
        break
    elif guess < num:
        print("You guess too low")
    else:
        print("You guess too high"
