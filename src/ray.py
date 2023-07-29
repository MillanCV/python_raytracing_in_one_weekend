from vec3 import Point3

class Ray:
    def __init__(self, origin: Point3 = None, direction: Point3 = None):
        self.origin = origin
        self.direction = direction
        
    def get_origin(self):
        return self.origin
    
    def get_direction(self):
        return self.direction
    
    def at(self, t: int):
        return self.origin+(self.direction*t)