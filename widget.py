import sys
import pandas as pd
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog

# test
 # you are cool
#test
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Load the UI file
        uic.loadUi("form.ui", self)

        # Connect the button to a function
        self.pushButton.clicked.connect(self.load_file)

        # Example of accessing widgets
        self.logEntryButton.clicked.connect(self.log_entry_action)
        self.logOutButton.clicked.connect(self.log_out_action)
        self.comboBox.currentIndexChanged.connect(self.combo_box_changed)

        # Apply dark background and widget styles
        self.setStyleSheet("""
        QWidget {
            background-color: #2E2E2E; /* Dark grey test color */
            color: white; /* White text */
        }
        QLabel {
            color: white; /* Label text color */
        }
        QLineEdit {
            background-color: #3E3E3E; /* Slightly lighter grey */
            color: white;
            border: 1px solid #5E5E5E;
            padding: 5px;
        }
        QPushButton {
            background-color: #5A5A5A; /* Button background */
            color: white;
            border: 1px solid #3E3E3E;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #777777; /* Lighter grey when hovering */
        }
        QComboBox {
            background-color: #3E3E3E;
            color: white;
            border: 1px solid #5E5E5E;
            padding: 5px;
        }
        QTextEdit {
            background-color: #3E3E3E;
            color: white;
            border: 1px solid #5E5E5E;
        }
        QSlider::groove:horizontal {
            background: #5A5A5A; /* Slider groove background */
            height: 10px;
        }
        QSlider::handle:horizontal {
            background: #777777; /* Slider handle */
            width: 15px;
            margin: -5px 0; /* Align handle with groove */
        }
    """)


    # Define functions to handle button clicks
    def load_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_path:
            df = pd.read_excel(file_path)
            print(df)  # This will print the DataFrame, replace this with code to display in a QTableWidget if needed

    def log_entry_action(self):
        print("Log Entry Button Clicked")

    def log_out_action(self):
        print("Log Out Button Clicked")

    def combo_box_changed(self, index):
        selected_option = self.comboBox.currentText()
        print(f"ComboBox changed to: {selected_option}")

    def slider_changed(self, value):
        print(f"Slider value changed to: {value}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
