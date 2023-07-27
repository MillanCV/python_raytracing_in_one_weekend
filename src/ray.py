from vec3 import Point3

class Ray:
    def __init__(self, origin: Point3 = None, direction: Point3 = None):
        self.origin = origin
        self.direction = direction
        
    def origin(self):
        return self.origin
    
    def direction(self):
        return self.direction
    
    def at(self, t: int):
        return self.origin+(self.direction*t)