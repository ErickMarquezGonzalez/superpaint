from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint, QRectF
from PyQt6.QtGui import QPainter, QPen, QImage
from PyQt6.QtGui import QColor


class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StaticContents)
        self.image = QImage(self.size(), QImage.Format.Format_ARGB32)
        self.image.fill(QColor("#042069"))
        self.drawing = False
        self.last_point = QPoint()
        self.pen_color = QColor("#fff")
        self.pen_width = 2
    
    def resizeEvent(self, event):
        if self.width() > self.image.width() or self.height() > self.image.height():
            new_width = max(self.width(), self.image.width())
            new_height = max(self.height(), self.image.height())
            new_image = QImage(new_width, new_height, QImage.Format.Format_ARGB32)
            new_image.fill(QColor("2d2d2d"))
            with QPainter(new_image)  as painter:
                painter.drawImage(0, 0, self.image)
            self.image = new_image
            super().resizeEvent(event)
            self.draw_examples()
    
    def draw_examples(self):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"), 10, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(300, 0, 300, 600)
            painter.drawLine(0, 300, 600, 300)
            painter.drawRect(265, 265, 70, 70)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
