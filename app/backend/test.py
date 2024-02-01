# test_backend.py

from backend import Backend

def test_backend():
    # Créez une instance de Backend
    backend = Backend()

    try:
        # Ajoutez un produit
        backend.add_product("Produit Test", "Description du produit test", 19.99, 10, 1)

        # Obtenez tous les produits et imprimez-les
        products = backend.get_all_products()
        print("Produits actuels dans la base de données:")
        for product in products:
            print(product)

        # Modifiez le produit ajouté
        backend.modify_product(1, ("Nouveau Nom", "Nouvelle Description", 29.99, 15, 2))

        # Obtenez à nouveau tous les produits et imprimez-les
        updated_products = backend.get_all_products()
        print("Produits mis à jour dans la base de données:")
        for product in updated_products:
            print(product)

        # Supprimez le produit ajouté
        backend.remove_product(1)

        # Obtenez une dernière fois tous les produits et imprimez-les
        final_products = backend.get_all_products()
        print("Produits restants dans la base de données:")
        for product in final_products:
            print(product)

    finally:
        # Fermez la connexion à la base de données
        backend.close_connection()

if __name__ == "__main__":
    test_backend()
