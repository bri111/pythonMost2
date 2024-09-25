import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSlider, QComboBox, QTextEdit
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar Alignment")
        self.setGeometry(100, 100, 800, 600)

        # Main Layout
        main_layout = QVBoxLayout()

        # Toolbar Layout
        toolbar_layout = QHBoxLayout()

        # Add label and input for each column
        utc_label = QLabel("UTC")
        self.utc_input = QLineEdit()
        toolbar_layout.addWidget(utc_label)
        toolbar_layout.addWidget(self.utc_input)

        moc_label = QLabel("MOC")
        self.moc_input = QLineEdit()
        toolbar_layout.addWidget(moc_label)
        toolbar_layout.addWidget(self.moc_input)

        met_label = QLabel("MET")
        self.met_input = QLineEdit("0")
        toolbar_layout.addWidget(met_label)
        toolbar_layout.addWidget(self.met_input)

        slt_label = QLabel("SLT")
        self.slt_input = QLineEdit("0")
        toolbar_layout.addWidget(slt_label)
        toolbar_layout.addWidget(self.slt_input)

        mjd_label = QLabel("MJD")
        self.mjd_input = QLineEdit("0")
        toolbar_layout.addWidget(mjd_label)
        toolbar_layout.addWidget(self.mjd_input)

        mode_label = QLabel("Mode")
        self.mode_select = QComboBox()
        self.mode_select.addItems(["Choose", "Option 1", "Option 2"])
        toolbar_layout.addWidget(mode_label)
        toolbar_layout.addWidget(self.mode_select)

        # Buttons
        log_review_btn = QPushButton("Log Review")
        log_review_btn.clicked.connect(self.get_data)  # Connect button click to function
        toolbar_layout.addWidget(log_review_btn)

        # Add other buttons (if needed)
        log_entry_btn = QPushButton("Log Entry")
        log_entry_btn.clicked.connect(lambda: self.data_display.append("Log Entry clicked!"))
        toolbar_layout.addWidget(log_entry_btn)

        log_in_btn = QPushButton("Log In")
        log_in_btn.clicked.connect(lambda: self.data_display.append("Log In clicked!"))
        toolbar_layout.addWidget(log_in_btn)

        log_out_btn = QPushButton("Log Out")
        log_out_btn.clicked.connect(lambda: self.data_display.append("Log Out clicked!"))
        toolbar_layout.addWidget(log_out_btn)

        bg_monitor_btn = QPushButton("B/G Monitor")
        bg_monitor_btn.clicked.connect(lambda: self.data_display.append("B/G Monitor clicked!"))
        toolbar_layout.addWidget(bg_monitor_btn)

        main_layout.addLayout(toolbar_layout)

        # Slider example
        slider_layout = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        slider_layout.addWidget(QLabel("Select a value using the slider:"))
        slider_layout.addWidget(self.slider)

        main_layout.addLayout(slider_layout)

        # Add a text area to display the retrieved data
        self.data_display = QTextEdit()
        self.data_display.setReadOnly(True)  # Make it read-only
        main_layout.addWidget(self.data_display)

        # Set the main layout
        self.setLayout(main_layout)

    def get_data(self):
        # Retrieve data from inputs
        utc_value = self.utc_input.text()
        moc_value = self.moc_input.text()
        met_value = self.met_input.text()
        slt_value = self.slt_input.text()
        mjd_value = self.mjd_input.text()
        mode_value = self.mode_select.currentText()  # Get selected text from combo box
        slider_value = self.slider.value()  # Get current value from the slider

        # Format the retrieved data into a string
        data_string = f"UTC: {utc_value}\nMOC: {moc_value}\nMET: {met_value}\nSLT: {slt_value}\nMJD: {mjd_value}\nMode: {mode_value}\nSlider Value: {slider_value}\n"

        # Display the data in the text area
        self.data_display.setText(data_string)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
