import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget


class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(400, 400)

        grid_box = QGridLayout()
        for row in range(4):
            for column in range(4):
                button = QPushButton("")
                grid_box.addWidget(button, row, column)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_box)

app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())