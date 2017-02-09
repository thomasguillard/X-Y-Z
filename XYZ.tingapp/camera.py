import vector
from vector import *

class Camera:
    '''
        This object is representing a camera.
        It has a position and a direction.
        The direction is a normalized vector between the camera position and the World's origin
    '''

    def __init__(self):
        self.pos = Vector(500, 500, 500)
        self.dir = Vector(1, 0, 0)
    
    def rotateDirection(self):
        '''
            Dir goes between the origin and the camera position
            Dir = Origin - pos
            Doing this makes sure the camera is always pointing towars the World's origin
        '''
        self.dir = vector.subVectors(Vector(0,0,0), self.pos)
        self.dir.norm()
