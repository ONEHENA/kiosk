import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.number = 0

        self.ui.pushButton.clicked.connect(self.on_button_clicked)
        self.ui.pushButton_2.clicked.connect(self.on_button_2_clicked)
    
    def on_button_clicked(self):
        self.number += 1
        self.ui.label.setText(str(self.number))  # 'setText' 메서드에 문자열을 전달해야 합니다.

    def on_button_2_clicked(self):
        self.number -= 1
        self.ui.label.setText(str(self.number))  # 'setText' 메서드에 문자열을 전달해야 합니다.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
