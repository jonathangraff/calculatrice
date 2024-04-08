Lancer le programme : 

- cloner le repo Git
- docker-compose up

Aller sur le Swagger en local : 
 http://0.0.0.0:80/docs

Le fichier csv à récupérer contenant les calculs présents dans la base de données se trouve dans le container.
docker exec -it {id_du_container} sh
cat data.csv
