from PyQt6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QTextEdit, QWidget


class GridLayoutDemo(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Grid Layout Demo")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.setStyleSheet("""
            QLabel {
                background-color: grey;
                border: 1px solid #000;
            }

            QPushButton {
                background-color: green;
                border: 1px solid #000;
            }

            QTextEdit {
                background-color: blue;
                border: 1px solid #000;
            }
        """)

        button_full_width = QPushButton("Full Width")

        text_edit_square = QTextEdit()
        text_edit_square.setPlaceholderText("A")

        other_text_edit = QTextEdit()
        other_text_edit.setPlaceholderText("B")

        self.grid_layout.addWidget(button_full_width, 0, 0, 1, 3)
        self.grid_layout.addWidget(text_edit_square, 1, 0, 2, 2)
        self.grid_layout.addWidget(other_text_edit, 1, 2, 1, 1)

        self.grid_layout.setSpacing(20)
        self.grid_layout.setContentsMargins(10, 10, 10, 10)

        # self.grid_layout.setRowStretch(0, 1)
        # self.grid_layout.setRowStretch(1, 2)
        # self.grid_layout.setRowStretch(2, 1)

        # self.grid_layout.setColumnStretch(0, 1)
        # self.grid_layout.setColumnStretch(1, 2)
        # self.grid_layout.setColumnStretch(2, 1)
