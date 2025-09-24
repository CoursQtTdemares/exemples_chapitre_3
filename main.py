import sys

from PyQt6.QtWidgets import QApplication

from src.good_exemple import GoodExemple


def main() -> int:
    """Entry point for exemples_chapitre_3."""
    app = QApplication(sys.argv)

    window = GoodExemple()
    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
