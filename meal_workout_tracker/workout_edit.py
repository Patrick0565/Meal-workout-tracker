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
    QHBoxLayout,
    QComboBox,
    QDialog,
)


class WorkoutEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10, 10)
        self.layout = QFormLayout()
        self.workout_title_input = QLineEdit()
        self.workout_type_input = QLineEdit()
        self.start_time_input = QTimeEdit()
        self.workout_title_input.setPlaceholderText("Enter your title: ")
        self.workout_type_input.setPlaceholderText("Enter your workout type: ")
        self.notes_edit = QTextEdit()
        self.layout.addRow("Title: ", self.workout_title_input)
        self.layout.addRow("Exercises: ", self.workout_type_input)
        self.layout.addRow("Start time: ", self.start_time_input)
        self.layout.addRow("Notes: ", self.notes_edit)

        button_layout = QHBoxLayout()
        
        cancel_button = QPushButton("Cancel", self)
        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.add_workout)
        enter_button = QPushButton("Enter", self)
        
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(add_button)
        button_layout.addWidget(enter_button)
        
        self.layout.addRow(button_layout)

        widget = QWidget()
        self.setLayout(self.layout)

    def add_workout(self):
        # Get input
        missing = []
        title = self.workout_title_input.text()
        if not title:
            missing.append("title")
        exercise = self.workout_type_input.text()
        if not exercise:
            missing.append("exercise")
        start_time = self.start_time_input.text()
        if not start_time:
            missing.append("time")
        notes = self.notes_edit.toPlainText()
        if not notes:
            missing.append("notes")
        
        if missing:
            self.alert_user(missing)

    def alert_user(self, missing):
        msg = "You are missing the following infomation\n"
        for item in missing:
            msg += item + "\n"
        
        alert = QDialog(self)
        alert.setWindowTitle("alert")
        

        # 


