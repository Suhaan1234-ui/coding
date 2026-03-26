class Test:
    def __init__(self):
        self._x = 0

    @property #property help behave method like an attritube
    def x(self):          # getter is used to read the value
        return self._x

    @x.setter
    def x(self, value):   # setter is used to change the value
    
        self._x = value