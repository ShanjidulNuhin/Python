text ="Hello\nWold"
print(text)
print(repr(text))

# You will need to write a format string which prints out the data using the following syntax:
# Hello John Doe. Your current balance is $53.44.

balance=53.44
name = "John Doe"
print("Hello %s. Your current balance is %f."%(name,balance))