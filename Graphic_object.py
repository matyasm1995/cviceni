import turtle
from abc import ABC,abstractmethod


class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass

class Point(GraphicObject):
    def __init__(self,ax = 0, ay =0):
        self.x = ax
        self.y = ay

    def draw(self):
        turtle.goto(self.x,self.y)
        turtle.dot(3)

    def str(self):
        return 'Points ({},{})'.format(self.x,self.y)

class PolyLine(GraphicObject):
    def __init__(self,points):
        self.pts = points

    def draw(self):
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.down()
        for p in self.pts:
            turtle.goto(p.x, p.y)
        turtle.up()

    def str(self):
        return 'Polyline ,{} points)'.format(len(self.pts))


class Polygon(GraphicObject):
    def __init__(self, points):
        self.pts = points

    def draw(self):
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.down()
        for p in self.pts:
            turtle.goto(p.x, p.y)
        turtle.goto(self.pts[0].x, self.pts[0].y)
        turtle.up()

    def str(self):
        return 'Polygon ,{} points)'.format(len(self.pts))


class LineSegment(PolyLine):
    def __init__(self, p1, p2):
        self.pts = [p1,p2]


class Rectangle(Polygon):
    def __init__(self, LL, UR):
        self.pts = [LL,Point(UR.x, LL.y),UR,Point(LL.x, UR.y)]

