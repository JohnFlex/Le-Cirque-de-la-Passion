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
    fel "Bonjour à toi ! Je te présente Bolb notre Blobissime clown !"
    bol "..."
    bol "Je vais retourner à ma loge Felix, je dois me préparer"
    "" "Bolb s'en va sans même me regarder"
    j "Euh... Je lui ai fait quelque chose ?"
    fel "Bolb est un peu difficile à approcher, ça viendra avec le temps. Il est Blobimiste comme il dirait."
    fel "Je vous laisse vous balader un instant, le travail m'appelle !"

    menu:
        "Suivre Bolb":
            j "Attend Bolb !"
            jump SuivreBolbDansLoge
        "Attendre dehors":
            bol "(Regarde par le trou de serrure) Pourquoi reste-t-il dehors ?"
            "BOUM"
            jump AttendreDehorsChuteBolb


label SuivreBolbDansLoge:
    bol "Pourquoi me suis-tu ? Laisse moi tranquille !"
    j ""
    menu:
        "Forcer la porte":
            j "Non attends !"
            jump ForcerLaPorte
        "Le laisser tranquille":
            "D'accord..."
            jump RetournerVersFelix

label ForcerLaPorte:
    j "Je force la porte..."
    "" "Je sens quelque chose sous mes pieds..."
    jump FelixArrivePourLeTravail



label AttendreDehorsChuteBolb:
    bol "Regarde par le trou de serrure Pourquoi reste-t-il dehors ?"
    "" "La porte s'ouvre..."
    j "Attention !"
    bol "AHH..."

    menu:
        "Rigoler de sa situation":
            j "HAHAHA HAHAHA"
            jump RigolerDeBolb
        "Rattraper Bolb":
            j "Noooon Booolb !!"
            jump RattraperBolb


label RigolerDeBolb:
    "" "Bolb se retrouve tel une flaque au sol"
    bol "Cela te fait rire ? (Rouspete)"
    jump FelixArrivePourLeTravail

label RattraperBolb:
    j "Je tends mes mains pour essayer de le rattraper"
    jump FelixArrivePourLeTravail
        

label FelixArrivePourLeTravail:
    fel "Oh te voilà ! Vite suis-moi, ton travail de clown t'appelle !"
    fel "Pour ton premier jour tu vas pouvoir t'entrainer et regarder les répétitions si tu le veux. Tiens, voici celle de Bolb"
    
    menu:
        "S'installer sur les sièges devant la scène":
            bol "Fait du Beatbox"
            "" "Des morceaux de Bolb s'envolent pour se retrouver dans le public"
            jump MorceauxDeBolb


        "Monter sur scène avec lui":
            j "Laisse moi t'aider à répéter ton spectacle"
            jump RepetitionBolb
            


        "Abandonner Bolb et s'entrainer de son côté":
            jump TravailFinDeJournée


label RepetitionBolb:
    bol "Merci à toi..."
    bol "Prends les quilles derrière toi, je répète un spectacle de jonglage"
    j "Je m'avance vers les quilles puis me mets en place. Une fois Bolb prêt je lui lance les quilles"
    bol "oh..."
    "" "Toutes les quilles atterissent à l'intérieur de Bolb"

    menu:
        "Laisser les quilles dans Bolb":
            bol "rougit d'embarras et retourne dans sa loge"
            
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée

        "Aider Bolb à retirer les quilles":
            j "Hahaha, laisse moi t'aider"
            j "Je m'avance vers Bolb et lui retire toutes les quilles"
            bol "Voici un cadeau pour m'avoir aider..."
            "Une quille ? Merci je me souviendrais de ton incroyable prestation !"

            #TODO succès
            jump SoireeBolbPourBoire


label MorceauxDeBolb:
    menu:
        "Que faire avec les morceaux ?"
        "Les ramasser et aider Bolb":
            j "Attends je vais t'aider !"
            jump AiderMorceauxBolb

        "Laisser les morceaux là où ils sont":
            "" "Bolb se retrouve tout petit et essaye de se déplacer sans succès"
           
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée


label AiderMorceauxBolb:
    j "Je me faufile sur les différents sièges pour récupérer tous les morceaux que je vois et m'approche de Bolb pour le lui donner"
    bol "prends le morceau dans les cheveux et nous le donne"
    jump SoireeBolbPourBoire

label LaisserMorceauxBolb:
    bol "ma répétition...est fichu..."
    "" "Bolb se reconstruit seul tant bien que mal et te regarde d'un oeil mauvais"

    #TODO succès
    #TODO condition soirée
    jump SoireeBolbPourBoire
    jump TravailFinDeJournée





label SoireeBolbPourBoire:
    "" "Soirée avec Bolb"


label TravailFinDeJournée:
    j "Je vais aller travailler maintenant"










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