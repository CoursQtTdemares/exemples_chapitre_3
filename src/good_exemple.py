from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from src.label_input_widget import LabelInputWidget


class GoodExemple(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Good Exemple")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_vertical = QVBoxLayout()

        label_input = LabelInputWidget()
        button = QPushButton("Valider")

        layout_vertical.addWidget(label_input)
        layout_vertical.addWidget(button)

        central_widget.setLayout(layout_vertical)
