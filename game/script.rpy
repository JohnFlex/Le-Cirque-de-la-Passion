# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")
define bol = Character('Bolb le blob', color="#c8ffc8")
define j = Character('Joueur', color="#c8ffc8")
define fel = Character('Felix Circoos', color="#c8ffc8")
#Attirance envers la personne sur la route actuelle
define att = 0


#    menu:
#       "":
#         j ""
#         jump 
#       "":
#           bol ""
#           jump




# Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"



label bolbNAPasDeVin:
    bol "Ah mais en fait j'ai pas de vin !"
    menu:
        "Lui proposer d'aller chercher quelque chose":
            jump joueurVaChercherABoire
        "Décider d'appeler Felix pour qu'il nous donne quelque chose":
            jump joueurAppelleFelix


label joueurVaChercherABoire:
    j "Ah mais je peux aller chercher quelque chose moi-même, ça ne vas pas nous empècher de passer une bonne soirée !"
    bol ""


label joueurAppelleFelix:
    j "Ah ! Bah je vais appeler Felix dans ce cas"