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

        self.label_input = LabelInputWidget("Nom :")
        self.label_input2 = LabelInputWidget("Prénom :")
        self.label_input3 = LabelInputWidget("Email :")

        button = QPushButton("Valider")
        button.clicked.connect(self.on_button_clicked)

        layout_vertical.addWidget(self.label_input)
        layout_vertical.addWidget(self.label_input2)
        layout_vertical.addWidget(self.label_input3)
        layout_vertical.addWidget(button)

        central_widget.setLayout(layout_vertical)

    def on_button_clicked(self) -> None:
        print("nom :", self.label_input.text())
        print("prénom :", self.label_input2.text())
        print("email :", self.label_input3.text())
