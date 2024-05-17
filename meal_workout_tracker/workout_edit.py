import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QTextEdit,
    QTimeEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFormLayout,
    QPushButton,
)


class WorkoutEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10, 10)
        layout = QFormLayout()
        self.workout_type_input = QLineEdit()
        self.workout_type_input.setPlaceholderText("Enter your title: ")
        self.workout_type_input.setPlaceholderText("Enter your workout type: ")
        self.notes_edit = QTextEdit()
        layout.addRow("Title: ", QLineEdit())
        layout.addRow("Exercises: ", QLineEdit())
        layout.addRow("Start time: ", QLineEdit())
        layout.addRow("Notes: ", QLineEdit())

        button = QPushButton("Cancel", self)

    

        widget = QWidget()
        self.setLayout(layout)
