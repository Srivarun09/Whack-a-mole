import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget


class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(400, 400)

        grid_box = QGridLayout()
        self.buttons = []
        for row in range(4):
            row_buttons = []
            for column in range(4):
                button = QPushButton("")
                grid_box.addWidget(button, row, column)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=column: self.button_clicked(r, c))
                self.buttons.append(row_buttons)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_box)

app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())
        