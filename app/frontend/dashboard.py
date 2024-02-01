# app/frontend/dashboard.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLabel, QLineEdit, QWidget

from backend.backend import Backend


class Dashboard(QDialog):
    
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)
        self.setWindowTitle("Ajouter un produit")

        self.name_label = QLabel("Nom:")
        self.name_edit = QLineEdit()

        self.description_label = QLabel("Description:")
        self.description_edit = QLineEdit()

        self.price_label = QLabel("Prix:")
        self.price_edit = QLineEdit()

        self.quantity_label = QLabel("Quantité:")
        self.quantity_edit = QLineEdit()

        self.category_label = QLabel("Catégorie:")
        self.category_edit = QLineEdit()

        self.addButton = QPushButton("Ajouter")
        self.addButton.clicked.connect(self.accept)

        layout = QFormLayout()
        layout.addRow(self.name_label, self.name_edit)
        layout.addRow(self.description_label, self.description_edit)
        layout.addRow(self.price_label, self.price_edit)
        layout.addRow(self.quantity_label, self.quantity_edit)
        layout.addRow(self.category_label, self.category_edit)
        layout.addRow(self.addButton)

        self.setLayout(layout)

    def get_product_data(self):
        return {
            'name': self.name_edit.text(),
            'description': self.description_edit.text(),
            'price': float(self.price_edit.text()),
            'quantity': int(self.quantity_edit.text()),
            'category': self.category_edit.text()
        }


class StockManagementApp(QMainWindow):
    
    def __init__(self):
        super(StockManagementApp, self).__init__()

        self.setWindowTitle("Gestion des Stocks")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.product_table = QTableWidget()
        self.product_table.setColumnCount(6)
        self.product_table.setHorizontalHeaderLabels(['ID', 'Nom', 'Description', 'Prix', 'Quantité', 'Catégorie'])

        self.addButton = QPushButton("Ajouter Produit")
        self.addButton.clicked.connect(self.add_product)

        self.addButtonDelete = QPushButton("Supprimer Produit")
        self.addButtonDelete.clicked.connect(self.delete_product)

        self.layout.addWidget(self.product_table)
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.addButtonDelete)

        self.central_widget.setLayout(self.layout)

    def add_product(self):
        dialog = Dashboard(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            product_data = dialog.get_product_data()
            # Ajouter la logique pour insérer le produit dans la base de données
            # Ici, nous ajoutons simplement le produit à la table pour l'exemple
            row_position = self.product_table.rowCount()
            self.product_table.insertRow(row_position)
            for col, value in enumerate(product_data.values()):
                item = QTableWidgetItem(str(value))
                self.product_table.setItem(row_position, col, item)

    def delete_product(self):
        # Récupérez la ligne sélectionnée
        selected_row = self.product_table.currentRow()
        
        # Assurez-vous qu'une ligne est sélectionnée
        if selected_row >= 0:
            # Obtenez l'ID du produit à supprimer depuis la colonne ID (colonne 0)
            product_id = int(self.product_table.item(selected_row, 0).text())

            # Utilisez la classe Backend pour supprimer le produit de la base de données
            backend = Backend()
            backend.remove_product(product_id)

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_from_database()