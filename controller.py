from PyQt6.QtGui import QColor


class MainController:
    def __init__(self, main_window, ui):
        self.main_window = main_window
        self.ui = ui
        self.canvas = ui.widget
        self.ui.comboDibujos.addItems(["", "Cuadricula", "Estrella"])
        self.connect_signals()
    
    def connect_signals(self):
        self.ui.txtColor.textChanged.connect(self.update_color)
        self.ui.slider.valueChanged.connect(self.upadate_pincel)
        self.ui.btnBorrador.clicked.connect(self.set_eraser)
        self.ui.btnGuardar.clicked.connect(self.canvas.save_image)
        self.ui.actionOpen.triggered.connect(self.canvas.open_image)

    def open_file(self):
        self.canvas.save_image()
        
    def set_eraser(self):
        self.canvas.pen_color = QColor("042069")

    def upadate_pincel(self, width):
        figura = self.ui.comboDibujos.currentText()
        if figura == "":
            self.canvas.pen_width = width
        elif figura == "Cuadricula":
            self.canvas.draw_grid(width)
        elif figura == "Estrella":
            self.canvas.draw_star(width);
        else:
            print("Sin seleccion")

    
    def update_color(self):
        color = self.ui.txtColor.toPlainText().strip()
        print(color)
        fondo = QColor(color)
        self.canvas.pen_color = fondo
        if fondo.isValid():
            self.ui.txtColor.setStyleSheet(f"background-color: {color}; color:{self.color_inverso(fondo).name()}")
    
    def color_inverso(self, color):
        inverso= QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverso