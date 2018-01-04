import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Olympic(QWidget):
    
  def __init__(self):
    super().__init__()
    self.d = 100
    self.setGeometry(500, 500, 550, 550)
    self.setFixedSize(550, 550) #Aesthetic purpose
    self.setWindowTitle('Olympic Rings') 
    self.xpos = 0
    self.ypos = 0
    self.show() # this should be the last line of your constructor.
  
  def mousePressEvent(self, event):
    #call self attributes so they can be called under paintEvent. These are the mouseclick values used for rectangle color fill
    self.xpos = event.x()
    self.ypos = event.y()
  
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    '''setting pen colors, all same pixel'''
    bluePen = QPen(QBrush(Qt.blue), 5)
    yellowPen = QPen(QBrush(Qt.yellow), 5)
    blackPen = QPen(QBrush(Qt.black), 5)
    greenPen = QPen(QBrush(Qt.green), 5)
    redPen = QPen(QBrush(Qt.red), 5)
    '''setting rings'''
    #bluePen
    qp.setPen(bluePen)
    qp.drawEllipse(100, 225, self.d, self.d)
    #yellowPen
    qp.setPen(yellowPen)
    qp.drawEllipse(160, 270, self.d, self.d)
    #blackPen
    qp.setPen(blackPen)
    qp.drawEllipse(225, 225, self.d, self.d)
    #greenPen
    qp.setPen(greenPen)
    qp.drawEllipse(290, 270, self.d, self.d)
    #redPen
    qp.setPen(redPen)
    qp.drawEllipse(350, 225, self.d, self.d)
    '''make interlocking pattern. Overlapping the top intersections'''
    #blue
    qp.setPen(bluePen)
    qp.drawChord(100, 225, 100, 100, 0*16, 25*16)
    #yellow
    qp.setPen(yellowPen)
    qp.drawChord(160, 270, 100, 100, 60*16, 25*16)
    #black
    qp.setPen(blackPen)
    qp.drawChord(225, 225, 100, 100, 0*16, 25*16)
    #green
    qp.setPen(greenPen)
    qp.drawChord(290, 270, 100, 100, 60*16, 25*16)
    self.update()
    '''setting rectangles'''
    #blue
    if ((self.xpos - 150)**2 + (self.ypos - 275)**2)**0.5 <= 50 and ((self.xpos - 210)**2 + (self.ypos - 320)**2)**0.5 > 50: #excludes yellow intersection with blue
        qp.setPen(bluePen)
        qp.drawRect(150, 100, 240, 75)
        qp.fillRect(150, 100, 240, 75, Qt.blue)
    #yellow
    elif ((self.xpos - 210)**2 + (self.ypos - 320)**2)**0.5 <= 50 and ((self.xpos - 150)**2 + (self.ypos - 275)**2)**0.5 > 50 and ((self.xpos - 275)**2 + (self.ypos - 275)**2)**0.5 > 50: #excludes blue and black intersections with yellow
        qp.setPen(yellowPen)
        qp.drawRect(150, 100, 240, 75)
        qp.fillRect(150, 100, 240, 75, Qt.yellow)
    #black
    elif ((self.xpos - 275)**2 + (self.ypos - 275)**2)**0.5 <= 50 and ((self.xpos - 210)**2 + (self.ypos - 320)**2)**0.5 > 50 and ((self.xpos - 340)**2 + (self.ypos - 320)**2)**0.5 > 50: #exclude yellow and green intersections with black
        qp.setPen(blackPen)
        qp.drawRect(150, 100, 240, 75)
        qp.fillRect(150, 100, 240, 75, Qt.black)
    #green
    elif ((self.xpos - 340)**2 + (self.ypos - 320)**2)**0.5 <= 50 and ((self.xpos - 275)**2 + (self.ypos - 275)**2)**0.5 > 50 and ((self.xpos - 400)**2 + (self.ypos - 275)**2)**0.5 > 50: #excluses black red intersections with green
        qp.setPen(greenPen)
        qp.drawRect(150, 100, 240, 75)
        qp.fillRect(150, 100, 240, 75, Qt.green)
    #red
    elif ((self.xpos - 400)**2 + (self.ypos - 275)**2)**0.5 <= 50 and ((self.xpos - 340)**2 + (self.ypos - 320)**2)**0.5 > 50: #excludes green intersection with red
        qp.setPen(redPen)
        qp.drawRect(150, 100, 240, 75)
        qp.fillRect(150, 100, 240, 75, Qt.red)
    #blue and yellow intersection
    elif ((self.xpos - 150)**2 + (self.ypos - 275)**2)**0.5 <= 50 and ((self.xpos - 210)**2 + (self.ypos - 320)**2)**0.5 <= 50:
        qp.setPen(bluePen)
        qp.drawRect(150, 100, 120, 75)
        qp.fillRect(150, 100, 120, 75, Qt.blue)
        qp.setPen(yellowPen)
        qp.drawRect(270, 100, 120, 75)
        qp.fillRect(270, 100, 120, 75, Qt.yellow)
    #yellow and black intersection
    elif ((self.xpos - 210)**2 + (self.ypos - 320)**2)**0.5 <= 50 and ((self.xpos - 275)**2 + (self.ypos - 275)**2)**0.5 <= 50:
        qp.setPen(yellowPen)
        qp.drawRect(150, 100, 120, 75)
        qp.fillRect(150, 100, 120, 75, Qt.yellow)
        qp.setPen(blackPen)
        qp.drawRect(270, 100, 120, 75)
        qp.fillRect(270, 100, 120, 75, Qt.black)
    #black and green intersection
    elif ((self.xpos - 275)**2 + (self.ypos - 275)**2)**0.5 <= 50 and ((self.xpos - 340)**2 + (self.ypos - 320)**2)**0.5 <= 50:
        qp.setPen(blackPen)
        qp.drawRect(150, 100, 120, 75)
        qp.fillRect(150, 100, 120, 75, Qt.black)
        qp.setPen(greenPen)
        qp.drawRect(270, 100, 120, 75)
        qp.fillRect(270, 100, 120, 75, Qt.green)
    #green and red intersection
    elif ((self.xpos - 340)**2 + (self.ypos - 320)**2)**0.5 <= 50 and ((self.xpos - 400)**2 + (self.ypos - 275)**2)**0.5 <= 50:
        qp.setPen(greenPen)
        qp.drawRect(150, 100, 120, 75)
        qp.fillRect(150, 100, 120, 75, Qt.green)
        qp.setPen(redPen)
        qp.drawRect(270, 100, 120, 75)
        qp.fillRect(270, 100, 120, 75, Qt.red)
    qp.end()

if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Olympic()
  sys.exit(app.exec_())