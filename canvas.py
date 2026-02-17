from PyQt6.QtWidgets import QWidget, QMessageBox, QFileDialog
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
    
    
    def paintEvent(self, event):
        with QPainter(self) as painter:
            painter.drawImage(event.rect(), self.image, event.rect())
        
    
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
        self.update()
    
    def mousePressEvent(self, a0):
        if a0.button() == Qt.MouseButton.LeftButton:
            self.last_point = a0.position().toPoint()
            self.drawing = True
    
    def mouseMoveEvent(self, a0):
        if (a0.buttons() & Qt.MouseButton.LeftButton) and self.drawing:
            self.draw_line_to(a0.position().toPoint())

    def mouseReleaseEvent(self, a0):
        if (a0.button() == Qt.MouseButton.LeftButton) and self.drawing:
            self.draw_line_to(a0.position().toPoint())
            self.drawing = False
    
    def draw_line_to(self, end_point):
        with QPainter(self.image) as painter:
            painter.setPen(QPen(self.pen_color, self.pen_width, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            painter.drawLine(self.last_point, end_point)
            #painter.drawEllipse(end_point, 30, 30)
        self.update()
        self.last_point = end_point

    def clear(self):
        self.image.fill(QColor("042069"))
        self.update()

    def save_image(self):
        file_path = QFileDialog.getSaveFileName(
            self,
            "Save image",
            "",
            "PNG files (*.png);;All files (*)"
        )

        if file_path:
            print(file_path)
            self.image.save(file_path[0])
            QMessageBox.information(self, "Super Paint", "Imagen guardada correctamente")

    def open_image(self):
        file_path = QFileDialog.getOpenFileName(
            self,
            "Abir Image",
            "",
            "PNG Files (*.png);;All Files (*)"
        )

        if file_path:
            self.image = QImage(file_path[0])
            self.update()
    
    def draw_grid(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            r = int(w / value)
            for i in range(int(value)):
                painter.drawLine(r*i, 0, r*i, h)
                painter.drawLine(0, r*i, w, r*i)
        self.update()

    def draw_star(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            mid_w = w // 2
            mid_h = w // 2
            div = int(mid_w / int(value))
            painter.drawLine(mid_w, 0, mid_w, h)
            painter.drawLine(0, mid_h, w, mid_h)
            for x in range(1, value):
                painter.drawLine(mid_w, div*x, (mid_w + (div*x)), mid_h)
                painter.drawLine(mid_w, div*x, (mid_w - (div*x)), mid_h)
                painter.drawLine(mid_w, h-(div*x), (mid_w + (div*x)), mid_h)
                painter.drawLine(mid_w, h-(div*x), (mid_w - (div*x)), mid_h)
        self.update()
    

    def draw_estrelladoble(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            mid_w = w // 2
            mid_h = w // 2
            div = int(mid_w / int(value))
            for x in range(1, value):
                painter.setPen(QPen(QColor("#f00"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
                painter.drawLine(mid_w, div*x, (mid_w + (div*x)), mid_h)
                painter.drawLine(mid_w, div*x, (mid_w - (div*x)), mid_h)
                painter.drawLine(mid_w, h-(div*x), (mid_w + (div*x)), mid_h)
                painter.drawLine(mid_w, h-(div*x), (mid_w - (div*x)), mid_h)

                painter.setPen(QPen(QColor("#00f"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
                painter.drawLine(div*x, div*x, mid_w + (div*x), mid_h -(div*x))
                painter.drawLine(div*x, div*x, mid_w - (div*x), mid_h + (div*x))
                painter.drawLine(w - (div*x), h - (div*x), mid_w - (div*x), mid_h + (div*x))
                painter.drawLine(w - (div*x), h - (div*x), mid_w + (div*x), mid_h -(div*x))
        self.update()
    
    def draw_fower(self, value):
        self.clear()
        with QPainter(self.image) as painter:
            painter.setPen(QPen(QColor("#f00"), 1, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))
            w = self.image.width()
            h = self.image.height()
            mid_w = w // 2
            mid_h = w // 2
            div = int(mid_w / int(value))
            painter.drawLine(mid_w, 0, mid_w, h)
            painter.drawLine(0, mid_h, w, mid_h)
            for x in range(1, value):
                painter.drawLine(0, div*x, (0 + (div*x)), mid_h)
                painter.drawLine(div*x, 0, mid_w, 0 + (div*x))

                painter.drawLine(w - div*x, 0, mid_w, 0 +div*x)
                painter.drawLine(w, 0 + (div*x),w - (div*x), mid_h)

                painter.drawLine(w, h - (div*x),w - (div*x), mid_h)
                painter.drawLine(mid_w, mid_h + (div*x),mid_w + (div*x), h)

                painter.drawLine(mid_w, mid_h + (div*x),mid_w - (div*x), h)
                painter.drawLine(0, h -(div*x), (0 + (div*x)), mid_h)
        self.update()
    
    def draw_tablero(self, value):
        self.clear()

        with QPainter(self.image) as painter:
            painter.setPen(Qt.PenStyle.NoPen)
            w = self.image.width()
            h = self.image.height()
            w_celda = w / value
            h_celda = h / value

            for fila in range(value):
                for columna in range(value):
                    if (fila + columna) % 2 == 0:
                        painter.setBrush(QColor("#FFF"))
                    else:
                        painter.setBrush(QColor("#000"))
                    rect = QRectF(
                        columna * w_celda,
                        fila * h_celda,
                        w_celda,
                        h_celda
                    )
                    painter.drawRect(rect)
        self.update()
