
define bol = Character('Bolb le blob', image="bolb")
define fel = Character('Felix Circoos', image="felix")
define att = 0
define j = Character("[name]")
default app = 0


label start:
    scene bg circus with dissolve
    #$ musiclist = renpy.random.shuffle(["audio/ambi1.wav", "audio/ambi2.wav","audio/ambi3.wav","audio/ambi4.wav","audio/ambi5.wav","audio/ambi6.wav","audio/ambi7.wav","audio/ambi8.wav","audio/ambi9.wav","audio/ambi10.wav","audio/ambi11.wav"])
    play music ["audio/ambi1.wav", "audio/ambi2.wav","audio/ambi3.wav","audio/ambi4.wav","audio/ambi5.wav","audio/ambi6.wav","audio/ambi7.wav","audio/ambi8.wav","audio/ambi9.wav","audio/ambi10.wav","audio/ambi11.wav"] fadein 1.0 fadeout 1.0
    $app = 1
    show felix with moveinbottom
    fel "Bonjour à toi ! "
    extend "... Euuh..."
    extend "Comment tu t'appeles encore ?"  
    python:
        name = renpy.input("Entrez votre nom.", length=32)
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

    #TODO Bolb Default
    bol "..."
    bol "Je vais retourner à ma loge Felix, je dois me préparer pour ma répétition"
    hide bolb with moveoutbottom
    show felix:
        xalign 0.5
    with move
    j "Euh..."
    extend " Lui ai-je fait quelque chose ?" 
    fel "Bolb est un peu difficile à approcher, ça viendra avec le temps." 
    extend " Il est Blobimiste comme il dirait."
    fel "Ah !"
    extend " Je vous laisse vous balader un instant, le travail m'appelle !"
    hide felix with moveoutbottom

    menu:
        "Suivre Bolb":
            show bolb with moveinbottom

            j "Attend Bolb !"
            jump SuivreBolbDansLoge

        "Attendre dehors":
            show bolb with moveinbottom 
            bol "Pourquoi est-ce qu'il reste dehors comme ça ?"
            jump AttendreDehorsChuteBolb


label SuivreBolbDansLoge:
    bol "Pourquoi me suis-tu ?" 
    extend " Laisse moi tranquille !"     #TODO Bolb angry
    j "Mais je..."
    hide bolb with moveoutbottom
    j "Bolb vient de me claquer la porte au nez"

    menu:
        "Forcer la porte":
            j " Attends!"
            jump ForcerLaPorte

        "Le laisser tranquille":
            j "Bien je comprends, je te laisse tranquille"
            j "Je vais essayer de retrouver Felix"
            jump RetournerVersFelix

label ForcerLaPorte:
    j "Je prends mon élan et force la porte"
    bol "*Sploush*"
    j "Qu'est-ce que..."
    extend "???"
    j "Je baisse le regard et trouve Bolb au sol..."
    
    show bolb with moveinbottom
    
    j "...écraser sous mes pieds !"
    j "Je soulève mes pieds et le corps de Bolb est littéralement tel un chewing-gum !"
    j "Il se reforme difficilement et me lance un regard noir avant de refermer la porte d'un coup sec"     #TODO Bolb angry
    hide bolb with moveoutbottom
    j "..."
    fel "[name] !"

    show felix with moveinbottom

    extend " Te voilà !"
    fel "J'ai fini les installations nécessaires pour ton apprentissage. Tu vas pouvoir enfin montrer ton talent !"
    jump FelixArrivePourLeTravail



label AttendreDehorsChuteBolb:
    bol "Je ne lui ai rien demandé..."     #TODO Bolb embarrassed
    hide bolb with moveoutbottom
    j "J'entends une porte grincer et me tourne vers la loge de Bolb."
    show bolb with moveinbottom
    j "la porte s'ouvrir doucement et Blob qui sort mais il s'emmêlent les 'pieds'"
    j "Attention !"
    bol "AHH..."
    j "Je vois Bolb prêt à tomber au sol"

    menu:
        "Commencer à rire de sa situation":
            j "HAHAHA HAHAHA"
            jump RigolerDeBolb
        "Essayer de le rattraper":
            j "Noooon Booolb !!"
            jump RattraperBolb


label RigolerDeBolb:
    j "Bolb se retrouve tel une flaque au sol"
    #TODO Bolb angry
    bol "Cela te fait rire ?" 
    bol "Tu penses que rire du malheur des gens est vraiment Bloob ?"
    bol "Dès que Felix t'as présenté j'ai tout de suite sû que tu n'étais pas une bonne personne..."
    jump FelixArrivePourLeTravail

label RattraperBolb:
    j "Je tends mes mains pour essayer de le rattraper"
    j "Mais une fois en contact je me souviens de la consistance de son corps..."
    j "Je vois Bolb passer à travers moi sans pouvoir rien faire"
    bol "Aaahh *Sploush*"
    bol "Tu n'as pas beaucoup de neurones tu sais"     
    j "Hahaha comment ça ?"
    bol "Tenter de rattraper un blob c'est une première..." #TODO Bolb embarrassed
    bol "Mais j'apprécie bloboup le geste" #TODO Bolb embarrassed
    bol "..."
    bol "Merci à toi !" #TODO Bolb happy
    j "Il n'y a pas de quoi c'est normal"
    j "Je lui offre un sourir et Blob commence à repartit avant d'être interrompue par Felix"
    hide bolb with moveoutbottom

    jump FelixArrivePourLeTravail
        

label FelixArrivePourLeTravail:
    show felix with moveinbottom
    fel "[name] ! J'ai terminé les préparatifs. Suis-moi si tu le veux bien pour te montrer le chapiteau !"
    fel "Donc pour ton premier jour tu vas pouvoir t'entrainer ou bien regarder les répétitions des artistes pour te préparer si tu le veux."
    fel "Hum c'est bien, tout le monde s'entraine comme tu peux le voir !"
    fel "Tiens voici celle de Bolb !"
    hide felix with moveoutbottom
    
    menu:
        "S'installer sur les sièges devant la scène":
            show bolb with moveinbottom
            bol "*Fait du Beatbox*" #TODO Bolb happy
            j "Durant sa prestation, des morceaux de lui-même s'envole pour se retrouver sur les sièges du public"
            j "Il s'arrête subitement, gêné et me regarde"
            jump MorceauxDeBolb


        "Monter sur scène avec lui":
            show bolb with moveinbottom
            j "Laisse moi t'aider à répéter ton spectacle"
            jump RepetitionBolb
            


        "Abandonner Bolb et s'entrainer de son côté":
            jump TravailFinDeJournée


label RepetitionBolb:
    #show bolb with moveinbottom
    bol "Merci à toi, c'est gentil de ta part..." #TODO Bolb embarrassed
    bol "Prends les quilles derrière toi, je dois répéter un spectacle de jonglage"
    j ""
    j "Je m'avance vers les quilles puis me mets en place. Une fois Bolb prêt je lui lance les quilles"
    j "Les quilles volent dans les airs avant d'attérir par surprise..."
    extend "à l'intérieur de lui !"
    bol "oh..."
    j "Hahaha je ne m'attendais pas à ça, tu as viser dans le blob"

    menu:
        "Laisser les quilles dans Bolb":
            j "je le vois rougir d'embarras avant de se retourner et d'aller dans sa loge" #TODO Bolb embarrassed
            
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée

        "Aider Bolb à retirer les quilles":
            j "Hahaha, laisse moi t'aider"
            j "Je m'avance vers Bolb et lui retire toutes les quilles"
            bol "Voici un cadeau pour m'avoir aider..." #TODO Bolb embarrased
            j "Une quille ? Merci je me souviendrais de ton incroyable prestation !"

            #TODO succès
            jump SoireeBolbPourBoire


label MorceauxDeBolb:
    menu:
        "Que faire avec les morceaux ?"
        "Aller les ramasser et aider Bolb":
            j "Attends je vais t'aider !"
            bol "Tu n'es pas obligé tu sais..."
            j "Qu'est ce que tu racontes ?"
            extend " Bien sûr que si ! Je ne peux pas te laisser dans cet état"
            jump AiderMorceauxBolb

        "Laisser les morceaux là où ils sont":
            j "Bolb continue de me regarder..."
            bol "Commme toujours personne n'est là pour m'aider..." #TODO Bolb sad
            bol "Quel monde triste et inutil" #TODO Bolb sad

            fel "Oh Bolb encore !"
            show felix with moveinbottom
            bol "Je vois Felix s'avancer et récupérer les morceaux éparpillés de partout"
            fel "Je t'ai déjà dit de ne pas tenté le Beatbox, pourquoi t'acharnes-tu comme ça ?"
            bol "Je veux juste en faire..." #TODO Bolb sad
            extend " comme tout le monde..."
            $ Achievement.add(achievement_name['blobsolo'])
           
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée


label AiderMorceauxBolb:
    j "Je me faufile sur les différents sièges pour récupérer tous les morceaux que je vois et m'approche de Bolb pour le lui donner"
    bol "Je te remercie..."
    bol "Je ne pensais pas qu'une personne pouvait être aussi gentille" #TODO Bolb happy
    bol "Mais il te reste un morceau ici..."
    extend " Ne bouge pas."
    j "Bolb s'approche de moi et je le sens sur le haut de ma tête"
    j "Qu'est-ce que...?"
    bol "Tu avais un morceau sur la tête"
    bol "Pour m'avoir aider..." #TODO Bolb embarrassed
    extend " Je te le donne" #TODO Bolb embarrassed
    bol "Accepte le comme cadeau s'il te plait"
    bol "Je vais maintenant retourner à ma loge" #TODO Bolb happy
    j "Je te raccompagne !"
    bol "Merci..." #TODO Bolb happy

    jump SoireeBolbPourBoire

label LaisserMorceauxBolb:
    
   
    bol "ma répétition..." #TODO Bolb sad
    extend " Elle est fichue..."
    j "Bolb me regarde mais je ne réagis pas. Il baisse doucement la tête"

    #TODO succès
    #TODO condition soirée
    jump SoireeBolbPourBoire
    jump TravailFinDeJournée





label SoireeBolbPourBoire:
    "" "Soirée avec Bolb"
    jump bolbNAPasDeVin


label TravailFinDeJournée:
    j "Je pense que je vais aller travailler maintenant"
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
    #TODO mini bulle avec Felix ?
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
    bol "Pas grave, ça m'arrive tout le temps. De toute façon, on ne me laisse jamais rien faire." #TODO Bolb sad
    bol "Si c'est comme ça, je pense que c'est mieux que tu rentres chez toi. J'ai envie de passer la soirée seul. Comme d'habitude." #TODO Bolb sad
    menu:
        "Bonne idée.":
            #TODO
            pass
        "Malheureusement je suis encore nécessaire au boulot.":
            jump travailTriste


label travailTriste:
    bol "D'accord"
    bol "Moi qui pensait qu'on pourrait passer une soirée sympathique malgré tout." #TODO Bolb sad
    bol "C'est pas grave, on aura peut-être encore l'occasion de se revoir." #TODO Bolb sad
    bol "Rentre bien"
    jump travailJ1

label travailJ1:
    #TODO
    return

label joueurVaChercherABoire:
    bol "C'est merveilleux, c'est parfait, c'est génial ! Mais il ne faut pas que mon patron sache !"
    j "Je ne savais pas qu'il était si tyrannique..."
    bol "En fait, je ne supporte pas bien l'alcool, mais j'adore cette invention humaine. Surtout le vin rouge." #TODO Bolb embarrassed
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
    bol "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?" #TODO Bolb sad
    menu:
        "Garder un silence gênant.":
            bol "..."
            bol "C'est pas drôle, n'est ce pas ?"

        "Lui dire que sa blague n'est pas drôle":
            bol "..." #TODO Bolb sad
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
    bol "Uhuhuhuh du vin !" #TODO Bolb happy
    bol "Du bordeaux en plus ! Quel régale !"
    bol "Que la fête commence !"
    #TODO Dissolve to black
    bol "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?"
    bol "Oh regarde !"
    #TODO Dissolve bolb
    bol "Oulà ! Regarde, mon corps !"
    bol "Je deviens mauve hihi." 
    bol "J'en connais un qui ne sera pas content demain..." #TODO Bolb sad
    bol "Je sais que je ne t'ai pas dis, mais je ne digère pas bien les boissons..."
    jump maisonHeureux

label maisonHeureux:
    bol "..."
    bol "Merci."
    bol "Je ne me suis jamais senti accueilli comme ça." #TODO Bolb embarrassed
    bol "Tu vas presque me redonner le sourire."
    bol "Prenons encore un petit quelque chose et finissons notre soirée tranquillement."
    #TODO jump maison jour 2

label maisonTriste:
    #TODO 




            



