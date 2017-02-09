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
        v = self.divVectors(self.mag())
        self.x = v.x
        self.y = v.y
        self.z = v.z

def subVectors(self, other):
    newx = self.x - other.x
    newy = self.y - other.y
    newz = self.z - other.z
    return Vector(newx, newy, newz)

def addVectors(self, other):
    newx = self.x + other.x
    newy = self.y + other.y
    newz = self.z + other.z
    return Vector(newx, newy, newz)

def mulVectors(self, factor):
    newx = factor * self.x
    newy = factor * self.y
    newz = factor * self.z
    return Vector(newx, newy, newz)

def divVectors(self, divisor):
    newx = self.x / divisor
    newy = self.y / divisor
    newz = self.z / divisor
    return Vector(newx, newy, newz)