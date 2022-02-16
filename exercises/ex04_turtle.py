"""todo."""

__author__ = "730523706"


from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    initial_tutle: Turtle = Turtle()
    # Create a backround for the scene(sky, grass, sun, and cloud)
    draw_grass(initial_tutle, -250, -250, 500, 250)
    draw_sky(initial_tutle, -250, 0, 500, 250)
    draw_sun(initial_tutle, -200, 150, 25)
    draw_cloud(initial_tutle, -100, 150, 300, 15)
    # Start to add in trees to the canvas
    draw_tree(initial_tutle, 30, 40, -185, -76, 100)
    draw_tree(initial_tutle, 35, 55, 113, -120, 160)
    # Add in some rockes to the canvas
    draw_rock(initial_tutle, 140, -225, 70, 50, 55)
    draw_rock(initial_tutle, -140, -200, 100, 55, 70)
    done()


def draw_triangle(tri: Turtle, x: float, y: float, length: float) -> None:
    """Draw a triangle with the given side lengths whose bottom-left corner is positioned at x, y."""
    tri.penup()
    tri.goto(x, y)
    tri.setheading(0.0)
    tri.pendown()
    i: int = 0 
    while i < 3:
        tri.forward(length)
        tri.left(120)
        i += 1


def draw_rectangle(rect: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw a rectangle with the given length and width whose bottom-left corner is positioned at x, y."""
    rect.penup()
    rect.goto(x, y)
    rect.setheading(0.0)
    rect.pendown()
    
    i: int = 0
    while i < 4:
        if i == 0 or i == 2:
            rect.forward(length)
            rect.left(90)
        else:
            rect.forward(width)
            rect.left(90)
        i += 1


def draw_grass(grass: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the grass part of the background of the canvas."""
    grass.begin_fill()
    grass.color(0, 154, 23)
    grass.fillcolor(0, 154, 23)
    draw_rectangle(grass, x, y, length, width)
    grass.end_fill()


def draw_sky(sky: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draw the sky part of the background of the canvas."""
    sky.begin_fill()
    sky.color(135, 206, 235)
    sky.fillcolor(135, 206, 235)
    draw_rectangle(sky, x, y, length, width)
    sky.end_fill()


def draw_tree(tree: Turtle, trunk_base: float, trunk_height: float, x: float, y: float, branches: float) -> None:
    """Draw a tree with the given measurements where the bottom-left of trunk is located at x, y."""
    # Start with trunk
    tree.penup()
    tree.pendown()
    tree.begin_fill()
    tree.color(150, 75, 0)
    tree.fillcolor(150, 75, 0)
    draw_rectangle(tree, x, y, trunk_base, trunk_height)
    tree.end_fill()
    tree.begin_fill()
    tree.color(45, 90, 39)
    tree.fillcolor(45, 90, 39)
    # Move onto leaves
    start_of_branches_x: float = x - (branches - trunk_base) / 2
    start_of_branches_y: float = trunk_height + y
    draw_triangle(tree, start_of_branches_x, start_of_branches_y, branches)
    tree.end_fill()


def draw_rock(rock: Turtle, x: float, y: float, base: float, side_one: float, side_two: float) -> None:
    """Draw a grey rock with the bottom-left located at x,y with the given side legnths."""
    rock.penup()
    rock.goto(x, y)
    rock.setheading(0.0)
    rock.pendown()
    rock.begin_fill()
    rock.color(128, 132, 135)
    rock.fillcolor(128, 132, 135)
    i: int = 0
    while i < 6:
        if i == 0 or i == 3:
            rock.forward(base)
            rock.left(45)
        elif i == 1 or i == 5:
            rock.forward(side_one)
            rock.left(75)
        else:
            rock.forward(side_two)
            rock.left(60)
        i += 1
    rock.end_fill()


def draw_sun(sun: Turtle, x: float, y: float, side: float) -> None:
    """Draw a sun for the background of the canvas with the bottom-left located at x, y."""
    sun.penup()
    sun.goto(x, y)
    sun.setheading(0.0)
    sun.pendown()
    sun.begin_fill()
    sun.color(250, 253, 15)
    sun.fillcolor(250, 253, 15)
    i: int = 0
    while i < 12:
        sun.forward(side)
        sun.left(30)
        i += 1
    sun.end_fill()


def draw_cloud(cloud: Turtle, x: float, y: float, base: float, side: float) -> None:
    """Draw a white cloud that is base long and it's botton-left is located at x, y."""
    cloud.penup()
    cloud.goto(x, y)
    cloud.setheading(0.0)
    cloud.pendown()
    cloud.begin_fill()
    cloud.color(255, 255, 255)
    cloud.fillcolor(255, 255, 255)
    i: int = 0
    while i < 12:
        if i == 0 or i == 6:
            cloud.forward(base)
            cloud.left(30)
        else:
            cloud.forward(side)
            cloud.left(30)
        i += 1
    cloud.end_fill()


if __name__ == "__main__":
    main()