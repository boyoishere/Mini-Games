import turtle as ttl
import random

def cracks(t, length, angle, depth):
    if depth == 0 or length < 5:
        return
    t.forward(length)
    for turn in [angle, -angle]:  # Left and right branches
        if random.choice([True, False]):
            t.right(turn)
            cracks(t, length * random.uniform(0.5, 0.75), angle, depth - 1)
            t.left(turn)  # Return to original direction
    t.backward(length)

def sym_cracks(t):
    for x in [-100, 0, 100]:  # Left, middle, and right positions
        t.penup()
        t.goto(x, -100)
        t.setheading(60 if x < 0 else (120 if x > 0 else 90))
        t.pendown()
        cracks(t, random.randint(80, 120), random.randint(15, 30), random.randint(3, 5))

# -------------- MAIN --------------
ttl.setup(432, 432)  # Smaller window size
ttl.bgcolor("black")
t = ttl.Turtle()
t.speed(0)
t.color("white")
sym_cracks(t)
t.hideturtle()
ttl.done()
