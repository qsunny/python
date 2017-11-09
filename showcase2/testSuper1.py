class LoggingDict(dict):
    def __setitem__(self,key,value):
        logging.info('Setting %r to %r' %(key,value))
        super().__setitem__(key,value)
        

"""    
class LoggingDict(SomeOtherMapping):
    def __setitem__(self,key,value):
        logging.info('Setting %r to %r' %(key,value))
        super().__setitem__(key,value)
  

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

pprint(LoggingOD.__mro__)
"""  



class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()
print(dir(cs))

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)
        
class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.movable.draw()
        super().draw()
        
class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass
        
MovableColoredShape(color='red', shapename='triangle',
                    x=10, y=20).draw()        