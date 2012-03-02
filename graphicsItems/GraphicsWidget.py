from pyqtgraph.Qt import QtGui, QtCore  
from pyqtgraph.GraphicsScene import GraphicsScene
from GraphicsItemMethods import GraphicsItemMethods

__all__ = ['GraphicsWidget']
class GraphicsWidget(GraphicsItemMethods, QtGui.QGraphicsWidget):
    def __init__(self, *args, **kargs):
        """
        Extends QGraphicsWidget with several helpful methods and workarounds for PyQt bugs. 
        Most of the extra functionality is inherited from GraphicsObjectSuperclass.
        """
        QtGui.QGraphicsWidget.__init__(self, *args, **kargs)
        GraphicsItemMethods.__init__(self)
        GraphicsScene.registerObject(self)  ## workaround for pyqt bug in graphicsscene.items()

    #def getMenu(self):
        #pass
        
    def setFixedHeight(self, h):
        self.setMaximumHeight(h)
        self.setMinimumHeight(h)

    def setFixedWidth(self, h):
        self.setMaximumWidth(h)
        self.setMinimumWidth(h)
        
    def height(self):
        return self.geometry().height()
    
    def width(self):
        return self.geometry().width()

    def boundingRect(self):
        br = self.mapRectFromParent(self.geometry()).normalized()
        #print "bounds:", br
        return br
        
    def shape(self):  ## No idea why this is necessary, but rotated items do not receive clicks otherwise.
        p = QtGui.QPainterPath()
        p.addRect(self.boundingRect())
        #print "shape:", p.boundingRect()
        return p


