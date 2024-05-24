import controller
from PyQt6.QtWidgets import (
    QLabel, 
    QTextEdit,
    QVBoxLayout, 
    QWidget,
    )

class WorkoutsWidget(QWidget):
    def __init__(self):

        super().__init__()
        
        # Create QLabel widgets with the greeting message and instructions
        title_label = QLabel("Your workouts")
        self.setStyleSheet("color: #76ABAE")

        self.workout_details = QTextEdit()
        

        self.load_workouts()
        

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(self.workout_details)
        
        
        # Set the layout for the widget
        self.setLayout(layout)

    def load_workouts(self):
        workout_data = controller.get_workouts()
        self.workout_details.setHtml(workout_data)