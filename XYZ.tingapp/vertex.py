import vector
from vector import *

import tingbot
from tingbot import screen

class Vertex:
    '''
        A vertex is a point in 3d space.
        It has 3 coordinates.
    '''
    def __init__(self, _x, _y, _z, _stroke):
        self.coordinates = Vector(_x, _y, _z)
        self.proj = Vector(0, 0, 0)
        self.stroke = _stroke
    
    def plot(self):
        screen.rectangle(
            xy = (self.coordinates.x, self.coordinates.y),
            size = tuple([self.stroke]*2),
            color = 'white',
            align = 'center',
        )
    def plotDebug(self, _i):
        screen.text(
            _i,
            xy = (self.coordinates.x, self.coordinates.y),
            align = 'center',
            color = 'white',
        )


