import math
from math import sqrt

class Vector:
    '''
        Home made 3D Vector librairy
        Errors are more than likely \o/
    '''
    def __init__(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z
    
    def info(self):
        return [self.x, self.y, self.z]
        
    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
            
    def mul(self, factor):
        self.x *= factor
        self.y *= factor
        self.z *= factor

    def div(self, divisor):
        self.x /= divisor
        self.y /= divisor
        self.z /= divisor
           
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
        
    def cross(self, other):
        newx = self.y * other.z - self.z * other.y
        newy = self.z * other.x - self.x * other.z
        newz = self.x * other.y - self.y * other.x
        return Vector(newx, newy, newz)
        
    def mag2(self):
        return pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)
    
    def mag(self):
        return sqrt(self.mag2())
    
    def norm(self):
        v = divVector(self, self.mag())
        self.x = v.x
        self.y = v.y
        self.z = v.z

def subVectors(v1, v2):
    newx = v1.x - v2.x
    newy = v1.y - v2.y
    newz = v1.z - v2.z
    return Vector(newx, newy, newz)

def addVectors(v1, v2):
    newx = v1.x + v2.x
    newy = v1.y + v2.y
    newz = v1.z + v2.z
    return Vector(newx, newy, newz)

def mulVector(v, factor):
    newx = factor * v.x
    newy = factor * v.y
    newz = factor * v.z
    return Vector(newx, newy, newz)

def divVector(v, divisor):
    newx = v.x / divisor
    newy = v.y / divisor
    newz = v.z / divisor
    return Vector(newx, newy, newz)