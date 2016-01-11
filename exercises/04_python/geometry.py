class Point:
    def __init__(self,x=0,y=0):
        self.x = x;
        self.y = y;
    def distance_from(self, p2):
        distance = (self.x - p2.x)*(self.x - p2.x) + (self.y - p2.y)*(self.y - p2.y);
        distanceFinal = distance**(0.5);
        return distanceFinal;

class Circle:
    def __init__(self,point=Point(0,0),r=0):
        self.center = point;
        self.radius = r;
    def is_inside(self,point):
        if((point.x - self.center.x)*(point.x - self.center.x) + (point.y - self.center.y)*(point.y - self.center.y) < self.radius*self.radius):
            return True;
        else:
            return False;
