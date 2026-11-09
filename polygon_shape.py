import turtle

class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if sides < 3:
            raise ValueError("the number of sides >= 3")
        if side_length <= 0:
            raise ValueError("side length >= 0")
        if pen_size <= 0:
            raise ValueError("pen size >= 0")
        
        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.setheading(self.angle)
        self.turtle.color(self.color)
        self.turtle.pensize(self.pen_size)
        self.turtle.pendown()

        for _ in range(self.sides):
            self.turtle.forward(self.side_length)
            self.turtle.left(360/self.sides)

        self.turtle.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self.x = x
        self.y = y
        self.turtle.clear()
        self.draw()