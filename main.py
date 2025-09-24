import sys

from PyQt6.QtWidgets import QApplication

from src.grid_example import GridLayoutDemo


def main() -> int:
    """Entry point for exemples_chapitre_3."""
    app = QApplication(sys.argv)

    window = GridLayoutDemo()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
