Lancer le programme : 

- cloner le repo Git : git clone https://github.com/jonathangraff/calculatrice.git
- aller dans ce repo : cd calculatrice
- lancer le container : sudo docker-compose up

Aller sur le Swagger en local : 
 http://0.0.0.0:80/docs

Pour la route 'calculate' :
- Mettre {'calculation' : "4 1 2 + * 2 - 5/"} dans le body de la request par exemple

Pour la route get_data : 
Le fichier csv à récupérer contenant les calculs présents dans la base de données se trouve dans le container.
- récupérer l'ID du container : sudo docker ps 
- se placer dans le container : docker exec -it {id_du_container} sh
- lire le fichier : cat data.csv
