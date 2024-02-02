# app/backend/backend.py

import mysql.connector

class Backend:
    
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="store"
        )
        self.cursor = self.connection.cursor()

    def get_all_products(self):
        query = """
            SELECT product.id, product.name, product.description, 
                   product.price, product.quantity, category.name AS category
            FROM product
            JOIN category ON product.id_category = category.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def is_valid_price(self, price):
        try:
            price = float(price)
            return price >= 0 and round(price, 2) == price
        except ValueError:
            return False

    def is_valid_quantity(self, quantity):
        try:
            quantity = int(quantity)
            return quantity > 0
        except ValueError:
            return False

    def add_product(self, name, description, price, quantity, category):
        # Vérifier si la quantité est valide
        if not self.is_valid_quantity(quantity):
            print("La quantité n'est pas valide. Veuillez saisir un nombre entier positif.")
            return

        # Vérifier si le prix est valide
        if not self.is_valid_price(price):
            print("Le prix n'est pas valide. Veuillez saisir un nombre décimal avec deux chiffres après la virgule.")
            return

        # Vérifier si le produit avec le même nom existe déjà
        existing_product_query = "SELECT id, quantity FROM product WHERE name = %s"
        existing_product_values = (name,)
        self.cursor.execute(existing_product_query, existing_product_values)
        existing_product = self.cursor.fetchone()

        if existing_product:
            # Ajouter la quantité au produit existant
            new_quantity = existing_product[1] + quantity
            update_product_query = "UPDATE product SET quantity = %s WHERE id = %s"
            update_product_values = (new_quantity, existing_product[0])
            self.cursor.execute(update_product_query, update_product_values)
        else:
            # Ajouter le produit s'il n'existe pas
            insert_product_query = """
                INSERT INTO product (name, description, price, quantity, id_category)
                SELECT %s, %s, %s, %s, category.id FROM category
                WHERE category.name = %s
            """
            insert_product_values = (name, description, price, quantity, category)
            self.cursor.execute(insert_product_query, insert_product_values)

        self.connection.commit()

    def modify_product(self, product_id, new_values):
        query = "UPDATE product SET name=%s, description=%s, price=%s, quantity=%s, id_category=%s WHERE id=%s"
        values = (*new_values, product_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def remove_product(self, product_id):
        query = "DELETE FROM product WHERE id = %s"
        values = (product_id,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
