from Graphic_object import Point,PolyLine,Polygon,Rectangle,LineSegment
import turtle

pt = Point()
l = PolyLine([Point(10,10), Point(70,100)])
pg = Polygon([Point(10,10), Point(70,100),Point(200,200)])
rect = Rectangle(Point(0,0),Point(10,10))
seg = LineSegment(Point(0,0),Point(10,10))

turtle.up()

pt.draw()
l.draw()
pg.draw()
rect.draw()

turtle.exitonclick()