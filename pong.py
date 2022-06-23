
# Import required library
import turtle, time
 
 
# Create screen
sc = turtle.Screen()

#sc.title("Pong game")
sc.bgcolor("black")
#sc.addshape('backdrop2.gif')
sc.setup(width=1000, height=600)

turtle.bgpic('backdrop.gif')
# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")

left_pad.color('black', 'blue')
left_pad.shapesize(stretch_wid=6, stretch_len=1)
left_pad.penup()
left_pad.goto(-385, 0)
 
 
# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
#right_pad.color("red")
right_pad.color('black', 'red')
right_pad.shapesize(stretch_wid=6, stretch_len=1)
right_pad.penup()
right_pad.goto(385, 0)
 
 
# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(0)
hit_ball.shape("circle")
hit_ball.color('white', 'black')
#hit_ball.color("black")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5
 
 
# Initialize the score
left_player = 0
right_player = 0
 
 
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)

sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
# highlight = turtle.Turtle()
# highlight.shape('square')
# highlight.color('black', 'cyan')
# #highlight.setfillopacity(30)
# highlight.shapesize(stretch_wid=2, stretch_len=28)
# highlight.penup()
# highlight.goto(0, 275)
sketch.color("gray")
sketch.write("Left_player : 0    Right_player: 0", align="center", font=("Courier", 24, "bold"))
sketch.color("red", "white")
sketch.write("Left_player : 0    Right_player: 0", align="center", font=("Courier", 24, "normal"))
#sketch.write("Hello World", move=False, align="left", font=("Verdana", 24, "bold"))
#sketch.color("white")
#sketch.write("Hello World", move=False, align="left", font=("Verdana", 24, "normal"))
 
# Functions to move paddle vertically
def paddleaup():
    y = left_pad.ycor()
    #for x in range(4):
    #    y+=5
    #    left_pad.sety(y)
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    #for x in range(4):
    #    y-=5
    #    left_pad.sety(y)
    y -= 20
    left_pad.sety(y)
 
 
def paddlebup():
    y = right_pad.ycor()
    #for x in range(4):
    #    y+=5
    #    right_pad.sety(y)
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown():
    y = right_pad.ycor()
    #for x in range(4):
    #    y-=5
    #    right_pad.sety(y)
    y -= 20
    right_pad.sety(y)
 
 
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
 
start = time.time()
speed_multiplier = 1
required = 5
while True:
    sc.update()
    if time.time() - start > required and required != 35:
        print(time.time()-start, required)
        speed_multiplier *= 1.05
        required+= 15
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
 
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1#speed_multiplier
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1#speed_multiplier
 
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        speed_multiplier,start,required = 1, time.time(), 5
        #hit_ball.dy *= -5
        hit_ball.dx = 5
        hit_ball.dy = -5
        left_player += 1
        sketch.clear()
        sketch.color('gray')
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "bold"))
        sketch.color('black')
        sketch.write("Left_player : {}    Right_player: {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    elif hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        speed_multiplier,start,required = -1, time.time(), 5
        hit_ball.dx = 5
        hit_ball.dy = -5
        #hit_ball.dy = -5
        right_player += 1
        sketch.clear()
        sketch.color('gray')
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "bold"))
        sketch.color('black')
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 left_player, right_player), align="center",
                                 font=("Courier", 24, "normal"))
 
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+70 and hit_ball.ycor() > right_pad.ycor()-70):
        hit_ball.setx(360)
        hit_ball.dx*=-speed_multiplier
        
    if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+70 and hit_ball.ycor()>left_pad.ycor()-70):
        hit_ball.setx(-360)
        hit_ball.dx*=-speed_multiplier