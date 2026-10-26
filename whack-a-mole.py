import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox, QLineEdit
from PyQt6.QtCore import QTimer


# Starting screen
class DurationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Window variables
        self.setWindowTitle("Game Duration")
        self.setFixedSize(400, 400)

        # Starting screen styling
        self.setStyleSheet("""QWidget{
                background-color: #D9EAC8;
                color: #6B4423;}

            QLineEdit{
                background-color: white;
                border: 2px solid #A77B50;
                border-radius: 8px;
                padding: 8px;}

            QPushButton{
                background-color: #C49A6C;
                color: #6B4423;
                border: 2px solid #A77B50;
                border-radius: 10px;
                padding: 8px;
                font-weight: bold;}""")

        # Starting screen duration
        self.label = QLabel("Please enter a duration in seconds:", self)
        
        self.duration_input = QLineEdit(self)
        self.start_button = QPushButton("Start Game", self)

        # Position the widgets
        self.label.setGeometry(40, 100, 320, 30)

        self.duration_input.setPlaceholderText("Enter 15–60 seconds")
        self.duration_input.setGeometry(40, 145, 320, 40)

        self.start_button.setGeometry(120, 210, 160, 45)

        # Connect the button
        self.start_button.clicked.connect(self.start_game)

    def start_game(self):
        try:
            duration = int(self.duration_input.text())

            if 15 <= duration <= 60:
                self.game_window = MyFirstWindow(duration)
                self.game_window.show()
                self.close()
            else:
                QMessageBox.warning(self,
                    "Invalid Duration",
                    "Please enter a time between 15-60 secs.")

        except ValueError:
            QMessageBox.warning(self,
                "Invalid Duration",
                "Please enter a valid number.")

# Main Whack a Mole game
class MyFirstWindow(QMainWindow):
    def __init__(self, duration):
        super().__init__()

        # Window variables
        self.setWindowTitle("Whack-a-mole")
        self.setFixedSize(400, 400)

        # Game variables
        self.duration = duration
        self.grid_box = QGridLayout()
        self.buttons = []
        self.score = 0

        # Create the grid
        self.create_gridbox()
        self.place_mole()

        # Main game widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(self.grid_box)

        # Light green background
        central_widget.setStyleSheet("background-color: #D9EAC8;")

        # Score label
        self.score_label = QLabel("Score: 0", central_widget)
        self.score_label.setGeometry(5, 0, 100, 20)

        # Time label
        self.time_label = QLabel("Time: " + str(self.duration) + "s", central_widget)
        self.time_label.setGeometry(345, 0, 100, 20)

        # Countdown variables
        self.time_left = self.duration

        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)
        self.countdown_timer.start(1000)

        # Timer
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.end_game)
        self.timer.start(self.duration * 1000)

    def create_gridbox(self):
        for row in range(4):
            row_buttons = []

            for column in range(4):
                button = QPushButton("")

                # Box size
                button.setMinimumSize(80, 50)

                # Light brown buttons
                button.setStyleSheet(""" QPushButton{
                        background-color: #C49A6C;
                        color: #6B4423;
                        border: 2px solid #A77B50;
                        border-radius: 10px;
                        font-weight: bold;}""")

                self.grid_box.addWidget(button, row, column)
                row_buttons.append(button)

                button.clicked.connect(
                    lambda clicked, r=row, c=column:
                    self.button_clicked(r, c))

            self.buttons.append(row_buttons)

    def place_mole(self):
        # Chooses mole randomly in the grid 
        self.mole_row = random.randint(0, 3)
        self.mole_col = random.randint(0, 3)

        self.buttons[self.mole_row][self.mole_col].setText("MOLE")

    def button_clicked(self, row, column):
        # Increase the score when the mole is clicked 
        if row == self.mole_row and column == self.mole_col:
            print("Mole clicked!")

            self.score = self.score + 1
            self.score_label.setText("Score: " + str(self.score))

            self.buttons[self.mole_row][self.mole_col].setText("")
            self.place_mole()

    def update_timer(self):
        # Decreases the time and updates display
        self.time_left = self.time_left - 1
        self.time_label.setText("Time: " + str(self.time_left) + "s")

    def end_game(self):
        # Stops the countdown once game ends 
        self.countdown_timer.stop()

        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

            with open("score.txt", "a") as file:
                file.write(str(self.score) + "\n")

        # Displays final score 
        QMessageBox.information(self,"Game Over","Time is up! Your score is " + str(self.score))

# Starting the application
app = QApplication(sys.argv)
duration_window = DurationWindow()
duration_window.show()
sys.exit(app.exec())



