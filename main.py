#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from form import Ui_MainWindow
import pyqt_custom_titlebar_window
import qdarktheme
import pyautogui
import sys

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        qdarktheme.setup_theme("dark")
        self.setWindowTitle("Screen Shot")
        
        self.start.clicked.connect(self.screenshot)
        
    def screenshot(self):
        self.file = QFileDialog().getSaveFileName(self,"Save Scren Shot","C:\\","PNG Files *.png")
        file_path = self.file[0]
        
        screen = pyautogui.screenshot()
        screen.save(file_path)
        
        image = QPixmap(file_path)
        self.label.setPixmap(image)
        
        self.label_path.setText(file_path)
        
def main():
    app = QApplication(sys.argv)
    custom_title = pyqt_custom_titlebar_window.CustomTitlebarWindow(Window())
    custom_title.setButtonHint(["close"])
    custom_title.setButtons()
    custom_title.setGeometry(500,100,591,510)
    
    custom_title.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    