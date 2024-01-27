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
    bol "Ah mais en fait je n'ai rien à boire !"
    menu:
        "Lui proposer d'aller chercher quelque chose":
            jump joueurVaChercherABoire
        "Décider d'appeler Felix pour qu'il nous donne quelque chose":
            jump joueurAppelleFelix


label joueurAppelleFelix:
    j "Ah ! Bah je vais appeler Felix dans ce cas."
    bol "Je ne suis pas sur que c'est une bonne idée... Mais demande lui s'il a du vin rouge."
    j "Monsieur Circoos ? êtes-vous disposé ?"
    show felix 
    fel "Que puis-je faire pour vous ?"
    menu:
        "Je voudrais, si vous en avez bien-sur..."

        "Du vin rouge":
            jump felixRemballe
            
        "De la Vodka":
            jump felixRemballe


label felixRemballe:
    fel "Pardon ? Mais ça ne va pas dans la tête ?"
    fel "Je ne peux pas vous donner ça, la performance de Bolb sera absolument affectée demain !"
    hide felix  
    j "Ne sois pas triste Bolb, je ne savais pas qu'il était si tyranique."
    bol "Pas grave, ça m'arrive tout le temps. De toute façon, on ne me laisse jamais rien faire."
    bol "Si c'est comme ça, je pense que c'est mieux que tu rentres chez toi. J'ai envie de passer la soirée seul. Comme d'habitude."
    menu:
        "Bonne idée.":
            #TODO
            pass
        "Malheuresement je suis encore nécessaire au boulot.":
            jump travailTriste


label travailTriste:
    bol "D'accord"
    bol "Moi qui pensait qu'on pourrait passer une soirée sympathique malgré tout."
    bol "C'est pas grave, on aura peut-être encore l'occasion de se revoir."
    bol "Rentre bien"
    jump travailJ1

label travailJ1:
    #TODO
    return

label joueurVaChercherABoire:
    bol "C'est merveilleux, c'est parfait, c'est génial ! Mais il ne faut pas que mon patron sache !"
    j "Je ne savais pas qu'il était si tyrannique..."
    bol "En fait, je ne supporte pas bien l'alcool, mais j'adore cette invention humaine. Surtout le vin rouge."
    j "D'accord."
    #TODO Change scene background to shop
    menu:
        "Prendre du vin rouge":
            jump vinRouge
        "Prendre de la Vodka":
            jump vodka

label vodka:
    #TODO Scene Baground loge
    bol "De la Vodka ? Il n'y avait que ça ?"
    bol "Bon..."
    bol "Juste un petit verre alors."
    #TODO Dissolve to black
    bol "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?"
    menu:
        "Garder un silence gênant.":
            bol "..."
            bol "C'est pas drôle, n'est ce pas ?"

        "Lui dire que sa blague n'est pas drôle":
            bol "..."
            bol "Mais..."

    #TODO Bol angry
    bol "Vous êtes tous les mêmes, vous les humains."
    bol "Vous servez à rien."
    bol "Vous êtes répugnants."
    bol "Je vous déteste."
    bol "J'aurais du rester sur ma planète."
    bol "Et me faire exploser comme tout le monde."
    bol "Et pourtant je suis là."
    bol "A vivre une vie misérable en train de m'étouffer avec vos quilles et vos balles."
    bol "Rien ne sert plus à rien."
    menu:
        "Il suffit ! Je ne suis pas là pour t'entendre de plaindre !":
            j "Et c'est toi qui le dis ! Tu aurais du faire comme tu dis."
            j "Toi et ton espèce de diformes décimés avez eu ce que vous méritez !"
            bol "..."
            bol "Tu avais l'air pourtant d'être une personne différente."
            bol "Nous pouvons en rester là. Je vais te demander de partir."
            j "Je n'ai pas besoin de ta permission, boulette."
            jump maisonTriste
        "Pardon Bolb, je ne voulais pas t'offenser.":
            jump maisonHeureux


label vinRouge:
    bol "Uhuhuhuh du vin !"
    bol "Du bordeaux en plus ! Quel régale !"
    bol "Que la fête commence !"
    #TODO Dissolve to black
    bol "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?"
    bol "Oh regarde !"
    #TODO Dissolve bolb
    bol "Oulà ! Regarde, mon corps !"
    bol "Je deviens mauve hihi."
    bol "J'en connais un qui ne sera pas content demain..."
    bol "Je sais que je ne t'ai pas dis, mais je ne digère pas bien les boissons..."
    jump maisonHeureux

label maisonHeureux:
    bol "..."
    bol "Merci."
    bol "Je ne me suis jamais senti accueilli comme ça."
    bol "Tu vas presque me redonner le sourire."
    bol "Prenons encore un petit quelque chose et finissons notre soirée tranquillement."
    #TODO jump maison jour 2

label maisonTriste:
    #TODO 




            



