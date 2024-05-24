"""
app_starter.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from homepage import HomePageWidget
from workout_edit import WorkoutEdit
from workouts import WorkoutsWidget
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

        self.setStyleSheet("background-color: #222831")
        

        # Create main layout
        main_layout = QVBoxLayout()

        # Create dropdown box layout
        dropdown_layout = QVBoxLayout()
        
        title_label = QLabel("<font color='#76ABAE'>Workout Tracker</font>")
        self.app_options_combo = QComboBox()
        self.app_options_combo.setStyleSheet("color: #76ABAE;")
        self.app_options_combo.addItems(["Home", "Meals info", "Workout info", "Add workout"])
        
        dropdown_layout.addWidget(title_label)
        dropdown_layout.addWidget(self.app_options_combo)

        # Create widget layout
        widget_layout = QVBoxLayout()
        self.workout_edit = WorkoutEdit()
        self.home_page = HomePageWidget() 
        self.workouts = WorkoutsWidget() 
        widget_layout.addWidget(self.home_page)
        self.home_page.setVisible(True)
        widget_layout.addWidget(self.workouts)
        self.workouts.setVisible(False)
        widget_layout.addWidget(self.workout_edit)
        self.workout_edit.setVisible(False)

        # Add dropdown layout and widget layout to main layout
        main_layout.addLayout(dropdown_layout)
        main_layout.addLayout(widget_layout)

        # [OPTIONAL] Add a stretch to move everything up
        main_layout.addStretch()

        # Create central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect signal to slot
        self.app_options_combo.currentIndexChanged.connect(self.show_hide_widgets)

    def show_hide_widgets(self, index):
        if index == 0:  
            self.home_page.setVisible(True)
            self.workouts.setVisible(False)
            self.workout_edit.setVisible(False)
        elif index == 2:  
            self.home_page.setVisible(False)
            self.workouts.load_workouts()
            self.workouts.setVisible(True)
            self.workout_edit.setVisible(False)
        elif index == 3:  
            self.home_page.setVisible(False)
            self.workout_edit.setVisible(True)
            self.workouts.setVisible(False)
        else:
            self.home_page.setVisible(False)
            self.workout_edit.setVisible(False)
            self.workouts.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle("Fusion")
    window.show()

    app.exec()
