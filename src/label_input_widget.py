from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class LabelInputWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        layout_horizontal = QHBoxLayout()

        name_label = QLabel("Nom :")
        name_line_edit = QLineEdit()

        layout_horizontal.addWidget(name_label)
        layout_horizontal.addWidget(name_line_edit)

        self.setLayout(layout_horizontal)
