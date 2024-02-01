-- Insérer des catégories
INSERT INTO category (name) VALUES ('Électronique');
INSERT INTO category (name) VALUES ('Vêtements');
INSERT INTO category (name) VALUES ('Mobilier');

-- Insérer des produits
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Téléviseur HD', 'Écran plat 55 pouces', 799, 10, 1);
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Chemise en coton', 'Taille M, couleur bleue', 29, 50, 2);
INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Canapé en cuir', 'Design moderne, couleur noire', 999, 5, 3);


ALTER TABLE product AUTO_INCREMENT = 1;
