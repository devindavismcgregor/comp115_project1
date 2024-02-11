import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("midnightblue")

pen = turtle.Turtle()
pen.speed(0)  

def draw_building(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

def draw_city():
    buildings = [
        (-200, -150, 100, 300, "grey"),
        (-50, -100, 150, 250, "darkgrey"),
        (100, -200, 120, 350, "dimgray"),
        (250, -120, 100, 270, "grey")
    ]
    for building in buildings:
        draw_building(*building)

def draw_star(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

def draw_stars():
    stars = [
        (-300, 200, 5),
        (-100, 250, 5),
        (150, 280, 5),
        (200, 150, 5),
        (50, 180, 5),
        (-200, 100, 5),
        (100, 100, 5),
        (300, 200, 5),
        (250, 50, 5),
        (-150, 50, 5)
    ]
    for star in stars:
        draw_star(*star)

def draw_moon(x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color("lightyellow")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_moon_and_stars():
    draw_moon(-300, 200, 40)
    draw_stars()

def draw_cityatnight():
    draw_city()
    draw_moon_and_stars()

def main():
    pen.hideturtle()
    draw_cityatnight()
    screen.mainloop()

if __name__ == "__main__":
    main()