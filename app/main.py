# app/main.py

import sys
from PySide6.QtWidgets import QApplication
from frontend.dashboard import StockManagementApp

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = StockManagementApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())