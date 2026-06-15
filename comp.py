import random
sec = random.randint(1,100)
print(f"Your random number is {sec}")

num =random.randint(1,100)
guess=int(input("enter a number, what is in your mind?"))
if guess==num:
    print("You guess the currect number")
elif guess>=num:
    print("You guess too low")
else:
    print("You guess too high")