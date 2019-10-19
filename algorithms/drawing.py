import turtle


def drawSquare():
    # window = turtle.Screen()
    # window.screensize(100, 100, 'green')
    drawSq()
    turtle.screensize(100, 100)
    # print(window.screensize())
    turtle.done()


def drawSq():
    board = turtle.Turtle()
    board.penup()
    board.goto(-120, 120)
    board.pendown()
    for i in range(4):
        board.forward(500)
        board.right(90)
