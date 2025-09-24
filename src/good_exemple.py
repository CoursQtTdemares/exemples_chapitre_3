from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class GoodExemple(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Good Exemple")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_vertical = QVBoxLayout()

        # label + line_edit dans un layout horizontal
        layout_horizontal = QHBoxLayout()
        name_label = QLabel("Nom :")
        name_line_edit = QLineEdit()
        layout_horizontal.addWidget(name_label)
        layout_horizontal.addWidget(name_line_edit)

        # button
        button = QPushButton("Valider")

        layout_vertical.addLayout(layout_horizontal)
        layout_vertical.addWidget(button)

        central_widget.setLayout(layout_vertical)
