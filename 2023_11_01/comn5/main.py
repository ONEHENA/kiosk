import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

        
        

    def on_button_clicked(self):
        text = self.ui.pushbutton.text()
        self.ui.label.setText(text)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())