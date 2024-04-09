Plan pour la gestion du dev :

1) Gestion de la partie algorithmique : 
- Ecriture des tests que doivent passer la calculatrice
- Gestion des erreurs
- Ecriture d'une fonction qui doit passer ces tests - possible développement en TDD

2) Ajout d'une base de données et d'une fonction qui sauvegarde chaque calcul dans cette BDD

3) Ajout d'une fonction qui sauvegarde la base de données dans un fichier csv

4) Partie API : création avec FastAPI de l'API REST permettant d'envoyer ses calculs et de récupérer le fichier csv via l'API

5) Gestion de la partie frontend en parallèle des parties précédentes

6) Contenerisation de l'application vis Docker