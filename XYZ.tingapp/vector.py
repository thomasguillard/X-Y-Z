class Vector:
    def __init__(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z
    
    def info(self):
        return [self.x, self.y, self.z]