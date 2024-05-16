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
)


class WorkoutEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10, 10)
        layout = QVBoxLayout()
        self.workout_type_input = QLineEdit()
        self.workout_type_input.setPlaceholderText("Enter your workout type: ")
        self.notes_edit = QTextEdit()
        layout.addWidget(self.workout_type_input)
        layout.addWidget(self.notes_edit)

        widget = QWidget()
        widget.setLayout(layout)
