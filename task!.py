from os import name

name="Shanjidul"
age=21
height = "5'6"
is_student=True

print(f'My name is {name}, I am {age} years old, my height is {height} and i am a student.{is_student}')

name2=input("Enter your name:")
age2=int(input("Enter your age:"))
if age2>20:
    print(f'Hello {name2}\t you are under {age2} years old')
else:
    print(f'Hello {name2}\t you are {age2} years old')
