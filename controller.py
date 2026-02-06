from PyQt6.QtGui import QColor

class MainController:
    def __init__(self, main_window, ui):
        self.main_window = main_window
        self.ui = ui
        self.connect_signals()
    
    def connect_signals(self):
        self.ui.txtColor.textChanged.connect(self.update_color)

    def upadate_pincel(self):
        width = self.ui.silder.value
        print(width)
    
    def update_color(self):
        color = self.ui.txtColor.toPlainText().strip()
        print(color)
        fondo = QColor(color)
        if fondo.isValid():
            self.ui.txtColor.setStyleSheet(f"background-color: {color}; color:{self.color_inverso(fondo).name()}")
    
    def color_inverso(self, color):
        inverso= QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverso