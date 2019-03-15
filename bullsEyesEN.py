from graphics import*

bEyesWin = GraphWin ("bEyes", 500, 500)
bEyesWin.setCoords(0, 0, 500, 500)

def draw_Cir(cX, cY, size, color, Win):
     for i in range (6): 
        circle = Circle(Point(cX, cY),(size/6) * (i - 6))
        if i%2 == 0:
            circle.setFill(color)
        else:
            circle.setFill(color_rgb(0,0,0))
        circle.draw(Win)
   
size=200
draw_Cir(250, 250, size, "red", bEyesWin)
    

bEyesWin.getMouse ()
bEyesWin.close ()
