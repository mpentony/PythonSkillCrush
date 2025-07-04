import turtle as turtle
import random

#setup screen
screen = turtle.Screen()
screen.title("Turtle Sandbox")
screen.bgcolor("lightblue")

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, the drawing app will draw the shape you selected.")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  # Star
  turtle.pencolor("blue")
  for i in range(5):
    turtle.forward(100)
    turtle.right(144)

def square():
  # Square
  turtle.pencolor("red")
  for i in range(4):
    turtle.forward(100)
    turtle.right(90)

def hexagon():
  # Hexagon
  turtle.pencolor("purple")
  for i in range(6):
    turtle.forward(100)
    turtle.right(60)

selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()

screen.mainloop()