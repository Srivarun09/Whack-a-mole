import sys
import random 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget


class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(400, 400)

        self.grid_box = QGridLayout()
        self.buttons = []

        self.create_gridbox()
        self.place_mole()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.grid_box)

    def create_gridbox(self):
        for row in range(4):
            row_buttons = []

            for column in range(4):
                button = QPushButton("")
                self.grid_box.addWidget(button, row, column)
                row_buttons.append(button)

                button.clicked.connect(lambda clicked, r=row, c=column: self.button_clicked(r, c))
                
            self.buttons.append(row_buttons)

    def place_mole(self):
        self.mole_row = random.randint(0, 3)
        self.mole_col = random.randint(0, 3)

        self.buttons[self.mole_row][self.mole_col].setText("MOLE")

    def button_clicked(self, row, column):
        if row == self.mole_row and column == self.mole_col:
            print("Mole clicked!")

            self.buttons[self.mole_row][self.mole_col].setText("")

            self.place_mole()


app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())