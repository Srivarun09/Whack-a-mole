import sys
import random 
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QInputDialog, QMessageBox
from PyQt6.QtCore import QTimer


class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(400, 400)

        self.grid_box = QGridLayout()
        self.buttons = []

        self.score = 0

        self.create_gridbox()
        self.place_mole()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.grid_box)

        self.score_label = QLabel("Score: 0", central_widget)
        self.score_label.setGeometry(5, 0, 100, 20)

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.end_game)
        self.timer.start(self.duration * 1000)
    
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

            self.score = self.score + 1
            self.score_label.setText("Score: " + str(self.score))

            self.buttons[self.mole_row][self.mole_col].setText("")

            self.place_mole()

    def end_game(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

        QMessageBox.information(self,"Game Over","Time is up! Your score is " + str(self.score))

app = QApplication(sys.argv)

while True:
    input_box = QInputDialog()
    input_box.setWindowTitle("Game Duration")
    input_box.setLabelText("Please enter a duration in seconds:")
    input_box.setFixedSize(400, 400)

    if input_box.exec():
        duration = input_box.textValue()
    else:
        sys.exit()

    try:
        duration = int(duration)

        if 15 <= duration <= 60:
            break
        else:
            QMessageBox.warning("Invalid Duration","Please enter a time between 15-60 secs.")
            

    except ValueError:
        QMessageBox.warning("Invalid Duration","Please enter a time between 15-60 secs.")


app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())


