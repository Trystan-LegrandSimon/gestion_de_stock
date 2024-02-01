# app/main.py

import sys
from PySide6.QtWidgets import QApplication
from frontend.dashboard import Dashboard
from backend.backend import Backend  # Importez la classe Backend

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Créez une instance de Backend
    data_manager = Backend()

    # Passez l'instance de Backend lors de la création de StockManagementApp
    window = Dashboard(data_manager)

    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())
