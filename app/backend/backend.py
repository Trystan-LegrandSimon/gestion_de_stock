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

    def add_product(self, name, description, price, quantity, id_category):
        query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        values = (name, description, price, quantity, id_category)
        self.cursor.execute(query, values)
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