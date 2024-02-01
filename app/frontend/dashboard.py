# app/frontend/dashboard.py

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QDialog, QFormLayout, QLabel, QLineEdit, QWidget
from backend.backend import Backend

class Dashboard(QMainWindow):
    
    def __init__(self, data_manager):
        super(Dashboard, self).__init__()

        self.data_manager = data_manager

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

        # Chargez les produits au démarrage de l'application
        self.load_products_from_database()

    def load_products_from_database(self):
        # Obtenez tous les produits depuis la base de données
        all_products = self.data_manager.get_all_products()

        # Effacez toutes les lignes actuelles dans la table
        self.product_table.setRowCount(0)

        # Remplissez la table avec les données des produits
        for row, product in enumerate(all_products):
            self.product_table.insertRow(row)
            for col, value in enumerate(product):
                item = QTableWidgetItem(str(value))
                self.product_table.setItem(row, col, item)

    def add_product(self):
        dialog = Dashboard(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            product_data = dialog.get_product_data()

            # Ajoutez le produit à la base de données
            self.data_manager.add_product(
                product_data['name'],
                product_data['description'],
                product_data['price'],
                product_data['quantity'],
                product_data['category']
            )

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_from_database()

    def delete_product(self):
        # Récupérez la ligne sélectionnée
        selected_row = self.product_table.currentRow()
        
        # Assurez-vous qu'une ligne est sélectionnée
        if selected_row >= 0:
            # Obtenez l'ID du produit à supprimer depuis la colonne ID (colonne 0)
            product_id = int(self.product_table.item(selected_row, 0).text())

            # Utilisez la classe Backend pour supprimer le produit de la base de données
            self.data_manager.remove_product(product_id)

            # Chargez à nouveau les produits depuis la base de données et mettez à jour le tableau
            self.load_products_from_database()