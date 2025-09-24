from PyQt6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class LabelInputWidget(QWidget):
    def __init__(self, text_label: str) -> None:
        super().__init__()

        layout_horizontal = QHBoxLayout()

        label = QLabel(text_label)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(text_label)

        layout_horizontal.addWidget(label)
        layout_horizontal.addWidget(self.line_edit)

        self.setLayout(layout_horizontal)

    def text(self) -> str:
        return self.line_edit.text()
