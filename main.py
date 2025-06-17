import os
import sys

from PySide6.QtWidgets import QApplication, QWidget
from player import Ui_Form

class ClaseVentana(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ClaseVentana, self).__init__(parent)
        self.setupUi(self)
        

def main():
    app = QApplication(sys.argv) 
    window = ClaseVentana()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()