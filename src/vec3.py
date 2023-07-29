import math

class Vec3:
    def __init__(self, e0: float = 0, e1: float = 0, e2: float = 0):
        self.e = [e0, e1, e2]
        
    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]
    
    def z(self):
        return self.e[2]
    
    def __neg__(self):
        return Vec3(e0 = -self.e[0], e1=-self.e[1], e2=-self.e[2])
    
    def __getitem__(self, key):
        return self.e[key]
    
    def __setitem__(self, key, value):
        self.e[key] = value
        
    def __add__(self, v):
        return Vec3(
            e0= self.e[0] + v.e[0],
            e1= self.e[1] + v.e[1],
            e2= self.e[2] + v.e[2]
        )
        
    def __sub__(self, v):
        return Vec3(
            e0= self.e[0] - v.e[0],
            e1= self.e[1] - v.e[1],
            e2= self.e[2] - v.e[2]
        )

    def __mul__(self, t):
        return Vec3(
            e0= self.e[0] * t,
            e1= self.e[1] * t,
            e2= self.e[2] * t
        )

    def __truediv__(self, t):
        return Vec3(
            e0= self.e[0] / t,
            e1= self.e[1] / t,
            e2= self.e[2] / t
        )

    def length(self):
        return (self.e[0]**2 + self.e[1]**2 + self.e[2]**2)**0.5

    def length_squared(self):
        return self.e[0]**2 + self.e[1]**2 + self.e[2]**2
    
    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"
    
    @staticmethod
    def dot(u: Vec3, v: Vec3)
        return (u.e[0] * v.e[0] + u.e[1] * v.e[1]+ u.e[2] * v.e[2])
    
def unit_vector(vector: Vec3) -> Vec3:
    return vector/vector.length()
        
Point3 = Vec3
Color = Vec3