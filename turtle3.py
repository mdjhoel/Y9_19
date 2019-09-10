from turtle import *
# read about functions
# https://www.w3schools.com/python/python_functions.asp
def square():
    for i in range(4):
        forward(100)
        right(90)

# run new square() function 4 times 
for i in range(4):
    square()
    forward(100)
