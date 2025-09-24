from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget

from src.label_input_widget import LabelInputWidget


class GoodExemple(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Good Exemple")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout_vertical = QVBoxLayout()

        self.label_input = LabelInputWidget("Nom :")
        self.label_input2 = LabelInputWidget("Prénom :")
        self.label_input3 = LabelInputWidget("Email :")

        self.label_input4 = LabelInputWidget("Age :")
        self.label_input5 = LabelInputWidget("Sexe :")

        self.button = QPushButton("Valider")
        self.button.clicked.connect(self.on_button_clicked)

        self.assemble_widgets()

        central_widget.setLayout(self.layout_vertical)

    def on_button_clicked(self) -> None:
        print("nom :", self.label_input.text())
        print("prénom :", self.label_input2.text())
        print("email :", self.label_input3.text())

    def assemble_widgets(self) -> None:
        self.layout_vertical.addWidget(self.label_input)
        self.layout_vertical.addWidget(self.label_input2)
        self.layout_vertical.addWidget(self.label_input3)

        self.layout_vertical.addStretch()

        self.layout_vertical.addWidget(self.label_input4)
        self.layout_vertical.addWidget(self.label_input5)
        self.layout_vertical.addWidget(self.button)
