from graphics import *

### Open a graphic window
win = GraphWin("Shapes")
### draw a red circle centered at point (100,100) within radius 30
center = Point(100,100)
circ = Circle(center,30)
circ.setFill("red")
circ.draw(win)

### put a textual lable in the center
label = Text(center,"Red box")
label.draw(win)

### draw a square using rectangle object
square = Rectangle(Point(30,30),Point(70,70))
square.draw(win)

###draw a line segment using Line object
line = Line(Point(20,30),Point(180,165))
line.draw(win)

### draw oval using oval object
oval = Oval(Point(20,180),Point(180,190))
oval.draw(win)
