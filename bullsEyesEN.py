from graphics import*

bEyesWin = GraphWin ("bEyes", 500, 500)
bEyesWin.setCoords(0, 0, 500, 500)

rCir = Circle (Point(250,250), 100)
rCir.setFill("red")	
rCir.draw(bEyesWin)

bEyesWin.getMouse ()
bEyesWin.close ()
