import turtle
import random

"""Describe this function...
"""
def make_recursive_square(length, level):
  for count in range(4):
    turtle.forward(length / 4)
    turtle.left(90)
    if level > 1:
      make_recursive_square(length / 2, level - 1)
    turtle.right(90)
    turtle.forward(length * 0.75)
    turtle.right(90)


turtle.shape("turtle")
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
turtle.speed(100)
make_recursive_square(100, 3)