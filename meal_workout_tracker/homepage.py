"""
This will be the homepage
Shouldn't have too much stuff here
Will greet the user and explain how to use the app
"""

# homepage.py
from PyQt6.QtWidgets import (
    QLabel, 
    QVBoxLayout, 
    QWidget,
    )

class HomePageWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create QLabel widgets with the greeting message and instructions
        greeting_label = QLabel("Welcome to the Homepage")
        instruction_label1 = QLabel("Here are some instructions on how to use the app:")
        instruction_label2 = QLabel("- Select 'Workout info' from the drop-down menu to edit workout information.")
        instruction_label3 = QLabel("- Select other options from the drop-down menu to navigate to different sections of the app.")
        instruction_label4 = QLabel("- You can create a title for your workouts. (ex: Chest Day)")
        instruction_label5 = QLabel("- You can add exercises to your workouts. (ex: Bench press, Push-ups)")
        instruction_label6 = QLabel("- You can also add the time to begin your workout. (ex: 16:15)")
        instruction_label7 = QLabel("- And finally, you can add notes to each workout. (ex: Do high weight, and low reps.)")


        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(greeting_label)
        layout.addWidget(instruction_label1)
        layout.addWidget(instruction_label2)
        layout.addWidget(instruction_label3)
        layout.addWidget(instruction_label4)
        layout.addWidget(instruction_label5)
        layout.addWidget(instruction_label6)
        layout.addWidget(instruction_label7)
        
        # Set the layout for the widget
        self.setLayout(layout)