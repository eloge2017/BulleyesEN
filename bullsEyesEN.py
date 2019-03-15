from graphics import*

bEyesWin = GraphWin ("bEyes", 500, 500)
bEyesWin.setCoords(0, 0, 500, 500)

def draw_Cir(cX, cY, size, color, Win,x):
    circle = Circle(Point(cX, cY),(size/6) * (x * 6))
    #circle.setFill(color)
    circle.draw(Win)
for i in range (6): 
    size=10
    draw_Cir(250, 250, size, "red", bEyesWin, i)
    

bEyesWin.getMouse ()
bEyesWin.close ()
