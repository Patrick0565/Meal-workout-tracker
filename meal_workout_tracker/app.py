"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from workout_edit import WorkoutEdit
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Workout Tracker")

        self.app_options_combo = QComboBox()
        self.app_options_combo.addItems(["Home", "Meals info", "Workout info"])

        self.workout_edit = WorkoutEdit()

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.app_options_combo)

        layout.addWidget(self.workout_edit)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
