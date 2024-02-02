# app/main.py

import sys
from PySide6.QtWidgets import QApplication
from frontend.StockManagementApp import StockManagementApp
from backend.backend import Backend

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Créez une instance de Backend
    data_manager = Backend()

    # Passez l'instance de Backend lors de la création de StockManagementApp
    window = StockManagementApp(data_manager)

    window.setGeometry(100, 100, 800, 700)
    window.show()
    sys.exit(app.exec())