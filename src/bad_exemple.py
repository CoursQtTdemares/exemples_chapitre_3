from PyQt6.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QWidget


class BadExemple(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Bad Exemple")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label = QLabel("Hello, World!", central_widget)
        label.move(10, 10)
        label.resize(80, 30)

        line_edit = QLineEdit(central_widget)
        line_edit.move(200, 30)
        line_edit.resize(200, 30)

        button = QPushButton("Click me", central_widget)
        button.move(120, 50)
        button.resize(100, 30)
