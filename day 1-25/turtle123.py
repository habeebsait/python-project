from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
user_input = screen.textinput("Make your bet", "Enter your color")

def move_fd():
  t.fd(20)
  
def right():
  t.right(10)
  
def left():
  t.left(10)
  
def move_bk():
  t.bk(20)
  
def clear():
  t.clear()
  t.penup()
  t.home()
  t.pendown()
  

screen.listen()
screen.onkey("W", move_fd)
screen.onkey("D", right)
screen.onkey("A", left)
screen.onkey("S", move_bk)
screen.onkey("C", clear)