import vector
from vector import *

import tingbot
from tingbot import screen

class Edge:
    '''
        An Edge is line in 3d space between two Vertices.
    '''
    def __init__(self, _vertex1, _vertex2, _stroke):
        self.start = _vertex1
        self.end = _vertex2
        self.stroke = _stroke
    
    def plot(self):
        screen.line(
            start_xy = (self.start.coordinates.x, self.start.coordinates.y),
            end_xy = (self.end.coordinates.x, self.end.coordinates.y),
            width = self.stroke,
            color = 'grey',
        )
    
    def plotDebug(self,_i):
        screen.text(
            _i,
            xy = ((self.start.coordinates.x + self.end.coordinates.x)/2, (self.start.coordinates.y + self.end.coordinates.y)/2),
            align = 'center',
            color = 'grey',
        )


