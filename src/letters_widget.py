from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget


class LettersWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        first_letters_with_position = [
            ("A", 0, 0),
            ("B", 0, 1),
            ("C", 0, 2),
            ("D", 1, 0),
            ("E", 1, 1),
            ("F", 1, 2),
        ]

        for letter, row, column in first_letters_with_position:
            button = QPushButton(letter)
            grid_layout.addWidget(button, row, column)

        grid_layout.addWidget(QPushButton("G"), 2, 1, 1, 2)
