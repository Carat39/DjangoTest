## models.py:
C'est ici que l'on définie nos modèles de la BDD concrètement, avec leurs règles et liaisons avec les autres tables

## forms.py:
On y met les différents formulaire (comme ceux des modification ou de création)
On peut directement faire forms.ModelForm pour reprendre des champs de Modeles précédent ou bien recréer des forms de zéro (forms.Form)

## urls.py:

C'est ici que l'on met les urls du site dans path, puis pour charger la bonne page, on appelle des méthodes dans views.py ou bien admin 

## views.py:

C'est ici que l'on met les comportements de nos urls.
A savoir, est-ce qu'il y a des données à transmettre (comme des ids).
Y'a t-il des formulaires auquel cas import des formulaires

## admin.py:
On y définit ce que l'admin pourra voir (ou peut être selon des vues ici)

## ▶️ Lancement

Se placer dans le même dossier que manage.py
Éxécuter la commande suivante : python manage.py runserver

## Connexion Admin :

ID : CARAT13
MDP : SiteTest21

