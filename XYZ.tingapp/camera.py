import vector
from vector import *

class Camera:
    '''
        This object is representing a camera.
        It has a position and a direction.
        The direction is a normalized vector between the camera position and the World's origin
    '''

    def __init__(self, d):
        self.d = d
        self.pos = Vector(self.d, 0, 0)
        self.dir = Vector(1, 0, 0)
    
    def rotateDirection(self):
        '''
            Dir goes between the origin and the camera position
            Dir = Origin - pos
            Doing this makes sure the camera is always pointing towars the World's origin
        '''
        self.dir = vector.subVectors(Vector(0,0,0), self.pos)
        self.dir.norm()
    
    def moveTo(self, x, y, z):
        self.pox.x = x
        self.pox.y = y
        self.pox.z = z
    
    def rotateZ(self, a):
        a_r = a * math.pi / 180
        xt = self.pos.x * math.cos(a_r) - self.pos.y * math.sin(a_r)
        yt = self.pos.x * math.sin(a_r) + self.pos.y * math.cos(a_r)
        self.pos.x = xt
        self.pos.y = yt
    
    def project(self, vertex):
        v = vector.subVectors(vertex.coordinates, self.pos)
        #print v.info()
        dist = vertex.coordinates.dot(self.dir)
        #print dist
        newx = vertex.coordinates.x - dist * self.dir.x
        newy = vertex.coordinates.y - dist * self.dir.y
        newz = vertex.coordinates.z - dist * self.dir.z
        vertex.proj.x = newx
        vertex.proj.y = newy
        vertex.proj.z = newz
        #print vertex.proj.info()