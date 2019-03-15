from graphics import*

bEyesWin = GraphWin ("bEyes", 500, 500)
bEyesWin.setCoords(0, 0, 500, 500)

def draw_Cir(cX, cY, size, color, Win):
    circle = Circle(Point(cX, cY),70)
    circle.setFill(color)
    circle.draw(Win)

draw_Cir(250, 250,70, "red", bEyesWin)

bEyesWin.getMouse ()
bEyesWin.close ()
