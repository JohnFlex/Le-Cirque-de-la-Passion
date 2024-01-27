
define bol = Character('Bolb le blob', image="bolb")
define fel = Character('Felix Circoos', image="felix")
define att = 0
define j = Character("[name]")

#    menu:
#       "":
#         j ""
#         jump 
#       "":
#           bol ""
#           jump



label start:
    scene bg cirque with dissolve
    show felix with moveinbottom
    fel "Bonjour à toi ! "
    extend "... Euuh..."
    extend "Comment tu t'appeles encore ?"  
    python:
        name = renpy.input("", length=32)
        name = name.strip()

        if not name:
            name = "Pat Smith"


    fel "[name] ! Désolé, je n'avais pas ton CV avec ! Je te présente Bolb notre Blobissime clown !"
    show felix:
        xalign 0.17
        yalign 1.0
    with move

    show bolb:
        xalign 0.8
        yalign 1.0
    with moveinbottom

    bol "..."
    bol "Je vais retourner à ma loge Felix, je dois me préparer"
    hide bolb with moveoutbottom
    #"" "Bolb s'en va sans même me regarder"
    j "Euh... Je lui ai fait quelque chose ?"
    fel "Bolb est un peu difficile à approcher, ça viendra avec le temps. Il est Blobimiste comme il dirait."
    fel "Je vous laisse vous balader un instant, le travail m'appelle !"
    hide felix with moveoutbottom

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
    jump travailTriste





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




            



