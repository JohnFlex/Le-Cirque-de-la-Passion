
define bol = Character('Bolb le blob', image="bolb")
define fel = Character('Felix Circoos', image="felix")
define att = 0
define j = Character("[name]")
default app = 0


label start:
    scene bg start with Fade(0.5, 0.5,5.0)
    "" "Tiens ? Je pourrais peut-être postuler..."

    scene bg black with fade
    "" "Une semaine plus tard..."

    scene bg circus with dissolve
    play music ["audio/ambi1.wav", "audio/ambi2.wav","audio/ambi3.wav","audio/ambi4.wav","audio/ambi5.wav","audio/ambi6.wav","audio/ambi7.wav","audio/ambi8.wav","audio/ambi9.wav","audio/ambi10.wav","audio/ambi11.wav"] fadein 1.0 fadeout 1.0
    $app = 1

    show felix:
        xalign 0.5
        yalign 2.7
    with moveinbottom

    fel "Bonjour à toi ! "
    extend "... Euuh..."
    extend "Comment tu t'appelles encore ?"  
    python:
        name = renpy.input("Entrez votre nom.", length=32)
        name = name.strip()

        if not name:
            name = "Pat Smith"

        if (name == "Bolb le blob"):
            Achievement.add(achievement_name['unknown'])

        if not(renpy.exists('audio/4554.mp3')):
            Achievement.add(achievement_name['4554'])


    fel "[name] ! Désolé, je n'avais pas ton CV avec ! Je te présente Bolb notre Blobissime clown !"
    show felix:
        yalign 2.7
        xalign 0.2
    with move

    show bolb:
        xalign 0.6
        yalign 0.6
    with moveinbottom

    bol "..."
    bol "Je vais retourner à ma loge Felix, je dois me préparer pour ma répétition."
    hide bolb with moveoutbottom

    show felix:
        xalign 0.5
        yalign 2.7
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
            #show bolb with moveinbottom

            j "Attends Bolb !"
            jump SuivreBolbDansLoge

        "Attendre dehors":
            scene bg room with dissolve

            show bolb:
                xalign 0.5
                yalign 1.5
            with moveinbottom 

            bol "Pourquoi est-ce qu'il reste dehors comme ça ?"
            jump AttendreDehorsChuteBolb


label SuivreBolbDansLoge:
    scene bg room with dissolve
    scene bg room with hpunch

    show bolb angry:
        xalign 0.5
        yalign 1.5
    with moveinbottom

    play sound "ef_angry.wav"
    #TODO play sound 
    bol angry "Pourquoi me suis-tu ?" 
    extend " Laisse moi tranquille !"
    j "Mais je..."
    hide bolb with moveoutbottom
    j "Bolb vient de me claquer la porte au nez."

    menu:
        "Forcer la porte":
            j " Attends!"
            jump ForcerLaPorte

        "Le laisser tranquille":
            j "Bien je comprends, je te laisse tranquille."
            j "Je vais essayer de retrouver Felix."
            jump FelixArrivePourLeTravail

label ForcerLaPorte:
    $ Achievement.add(achievement_name['sparta'])
    j "Je prends mon élan et force la porte."

    play sound "ef_door.wav"

    bol "*Sploush*"
    j "Qu'est-ce que..."
    extend "???"
    j "Je baisse le regard et trouve Bolb au sol..."
    
    show bolb angry:
        xalign 0.5
        yalign 1.5
    with moveinbottom
    
    #TODO play sound 

    j "...écraser sous mes pieds !"
    j "Je soulève mes pieds et le corps de Bolb est littéralement tel un chewing-gum !"
    play sound "ef_angry.wav"
    show bolb angry with hpunch
    bol angry "Tu viens de m'écraboubler !"
    j "Il se reforme difficilement et me lance un regard noir avant de refermer la porte d'un coup sec."
    hide bolb with moveoutbottom
    j "..."
    fel "[name] !"

    show felix:
        xalign 0.5
        yalign 1.0
    with moveinbottom

    extend " Te voilà !"
    fel "J'ai fini les installations nécessaires pour ton apprentissage. Tu vas pouvoir enfin montrer ton talent !"
    jump FelixArrivePourLeTravail



label AttendreDehorsChuteBolb:
    play sound "ef_embarrassed.wav"
    bol embarrassed "Je ne lui ai rien demandé..."
    hide bolb with moveoutbottom
    j "J'entends une porte grincer et me tourne vers la loge de Bolb."

    show bolb:
        xalign 0.5
        yalign 1.5
    
    with moveinbottom

    j "la porte s'ouvrir doucement et Blob qui sort mais il s'emmêlent les 'pieds'."
    j "Attention !"
    bol "AHH..."
    j "Je vois Bolb prêt à tomber au sol."

    menu:
        "Commencer à rire de sa situation":
            j "Hahaha Hahaha"
            jump RigolerDeBolb
        "Essayer de le rattraper":
            j "Noooon Booolb !!"
            jump RattraperBolb


label RigolerDeBolb:
    j "Bolb se retrouve tel une flaque au sol."
    play sound "ef_angry.wav"
    show bolb angry with hpunch
    bol angry "Cela te fait rire ?" 
    bol angry "Tu penses que rire du malheur des gens est vraiment Bloob ?"
    bol angry "Dès que Felix t'as présenté j'ai tout de suite sû que tu n'étais pas une bonne personne..."
    j "Bolb commence à s'éloigner en ronchonnant."
    hide bolb with moveoutbottom
    jump FelixArrivePourLeTravail

label RattraperBolb:
    j "Je tends mes mains pour essayer de le rattraper"
    j "Mais une fois en contact je me souviens de la consistance de son corps..."
    play sound "ef_special.wav"
    j "Je vois Bolb passer à travers moi sans pouvoir rien faire."

    play sound "ef_door.wav"

    bol "Aaahh *Sploush*"

    bol "Tu n'as pas beaucoup de neurones tu sais."     
    j "Hahaha comment ça ?"
    play sound "ef_embarrassed.wav"
    bol embarrassed "Tenter de rattraper un blob c'est une première..."
    bol embarrassed "Mais j'apprécie bloboup le geste."
    bol "..."
    play sound "ef_shortjoy.wav"
    bol happy "Merci à toi !"
    j "Il n'y a pas de quoi c'est normal."
    j "Je lui offre un sourir et Blob commence à repartir avant d'être interrompue par Felix."
    hide bolb with moveoutbottom

    jump FelixArrivePourLeTravail
        

label FelixArrivePourLeTravail:
    scene bg circus with dissolve

    show felix:
        xalign 0.5
        yalign 2.7   
    with moveinbottom

    fel "[name] ! J'ai terminé les préparatifs. Suis-moi si tu le veux bien pour te montrer le chapiteau !"
    fel "Donc pour ton premier jour tu vas pouvoir t'entrainer ou bien regarder les répétitions des artistes pour te préparer si tu le veux."
    fel "Hum c'est bien, tout le monde s'entraine comme tu peux le voir !"
    fel "Tiens voici celle de Bolb !"
    hide felix with moveoutbottom
    
    menu:
        "S'installer sur les sièges devant la scène":
            
            stop music fadeout 2.0
            show nbg circus lum 
            with dissolve  

            show bolb:
                xalign 0.5
                yalign 0.6
            with moveinbottom

            bol happy "Lumière..."
            play music ["ef_beatbox.wav", "ef_shortjoy.wav"]
            bol happy "..."
            hide nbg circus lum with dissolve
            play music ["audio/ambi1.wav", "audio/ambi2.wav","audio/ambi3.wav","audio/ambi4.wav","audio/ambi5.wav","audio/ambi6.wav","audio/ambi7.wav","audio/ambi8.wav","audio/ambi9.wav","audio/ambi10.wav","audio/ambi11.wav"] fadein 1.0 fadeout 1.0
            play sound "ef_applause.mp3" fadein 1.0
            "" "Durant sa prestation, des morceaux de lui-même s'envole pour se retrouver sur les sièges du public"
            stop sound fadeout 1.0
            j "Il s'arrête subitement, gêné et me regarde"
            jump MorceauxDeBolb


        "Monter sur scène avec lui":

            show bolb:
                xalign 0.5
                yalign 0.6
            with moveinbottom

            j "Laisse moi t'aider à répéter ton spectacle."
            jump RepetitionBolb
            


        "Abandonner Bolb et s'entrainer de son côté":
            jump TravailFinDeJournée


label RepetitionBolb:
    #show bolb with moveinbottom
    play sound "ef_embarrassed.wav"
    bol embarrassed "Merci à toi, c'est gentil de ta part..."
    bol "Prends les quilles derrière toi, je dois répéter un spectacle de jonglage."
    j "Je m'avance vers les quilles puis me mets en place. Une fois Bolb prêt je lui lance les quilles."
    j "Les quilles volent dans les airs avant d'attérir par surprise..."
    extend "à l'intérieur de lui !" #dans son ventre
    bol "Oh oh..."
    j "Hahaha je ne m'attendais pas à ça, tu as viser dans le blob !"

    menu:
        "Laisser les quilles dans Bolb":
            show bolb embarrassed with moveinbottom
            j "Je le vois rougir d'embarras avant de se retourner et d'aller dans sa loge."
            hide bolb with moveoutbottom
            
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée

        "Aider Bolb à retirer les quilles":
            j "Hahaha, laisse moi t'aider."
            j "Je m'avance vers Bolb et lui retire toutes les quilles."
            play sound "ef_embarrassed.wav"
            bol embarrassed "Voici un cadeau pour m'avoir aider..."
            j "Une quille ? Merci je me souviendrais de ton incroyable prestation !"

            $ Achievement.add(achievement_name['strike'])

            bol default  "Dit..."
            extend "Suis moi si tu veux bien."
            bol embarrassed "J'aimerai passer du temps avec toi."

            jump SoireeBolbPourBoire


label MorceauxDeBolb:
    menu:
        "Que faire avec les morceaux ?"
        "Aller les ramasser et aider Bolb.":
            j "Attends je vais t'aider !"
            bol "Tu n'es pas obligé tu sais..."
            j "Qu'est ce que tu racontes ?"
            extend " Bien sûr que si ! Je ne peux pas te laisser dans cet état."
            jump AiderMorceauxBolb

        "Laisser les morceaux là où ils sont":
            j "Bolb continue de me regarder..."
            play sound "ef_shortsad.wav"
            bol sad "Commme toujours personne n'est là pour m'aider..."
            bol sad "Quel monde triste et inutile."
            $ Achievement.add(achievement_name['blobsolo'])

            
            show bolb:
                xalign 0.6
                yalign 0.6
            with move

            show felix nervous:
                yalign 2.7
                xalign 0.2
            with moveinbottom
            fel nervous "Oh Bolb encore !"
            j "Je vois Felix s'avancer et récupérer les morceaux éparpillés de partout."
            fel nervous "Je t'ai déjà dit de ne pas tenté le Beatbox, pourquoi t'acharnes-tu comme ça ?"
            play sound "ef_shortsad.wav"
            bol sad "Je veux juste en faire..."
            extend " comme tout le monde..."

           
            #TODO condition soirée
            #jump SoireeBolbPourBoire
            jump TravailFinDeJournée


label AiderMorceauxBolb:
    j "Je me faufile sur les différents sièges pour récupérer tous les morceaux que je vois et m'approche de Bolb pour le lui donner."
    play sound "ef_embarrassed.wav"
    bol embarrassed "Je te remercie..."
    bol happy "Je ne pensais pas qu'une personne pouvait être aussi gentille."
    bol "Mais il te reste un morceau ici..."
    extend " Ne bouge pas."
    j "Bolb s'approche de moi et je le sens sur le haut de ma tête."
    j "Qu'est-ce que...?"
    bol "Tu avais un morceau sur la tête."
    play sound "ef_embarrassed.wav"
    bol embarrassed "Pour m'avoir aider..."
    extend " Je te le donne."
    bol "Accepte le comme cadeau s'il te plait."
    play sound "ef_shortjoy.wav"
    bol happy "Je vais maintenant retourner à ma loge."
    j "Je te raccompagne !"
    play sound "ef_shortjoy.wav"
    bol happy "Merci..."


    jump SoireeBolbPourBoire

label LaisserMorceauxBolb:
    
    play sound "ef_shortsad.wav"
    bol sad "ma répétition..." #TODO Bolb sad
    extend " Elle est fichue..."
    j "Bolb me regarde mais je ne réagis pas. Il baisse doucement la tête."

    #TODO succès
    #TODO condition soirée
    jump SoireeBolbPourBoire
    jump TravailFinDeJournée



label SoireeBolbPourBoire:
    scene bg room with dissolve
    jump bolbNAPasDeVin


label TravailFinDeJournée:
    j "Je pense que je vais aller travailler maintenant."
    jump travailTriste



label bolbNAPasDeVin:
    show bolb:
        xalign 0.5 
        yalign 1.5
    with moveinbottom
    bol default "Ah mais en fait je n'ai rien à boire !"
    menu:
        "Lui proposer d'aller chercher quelque chose":
            jump joueurVaChercherABoire
        "Décider d'appeler Felix pour qu'il nous donne quelque chose.":
            jump joueurAppelleFelix


label joueurAppelleFelix:
    j "Ah ! Bah je vais appeler Felix dans ce cas."
    bol "Je ne suis pas sur que c'est une bonne idée... Mais demande lui s'il a du vin rouge."
    #TODO mini bulle avec Felix ?

    j "Monsieur Circoos ? êtes-vous disposé ?"

    show felix bubble:
        xalign 0.6
        yalign 0.2
    with dissolve

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
    play sound "ef_shortsad.wav"
    bol sad "Pas grave, ça m'arrive tout le temps. De toute façon, on ne me laisse jamais rien faire." #TODO Bolb sad
    bol "Si c'est comme ça, je pense que c'est mieux que tu rentres chez toi. J'ai envie de passer la soirée seul. Comme d'habitude."
    menu:
        "Bonne idée.":
            jump travailTriste
        "Malheureusement je suis encore nécessaire au boulot.":
            jump travailTriste




label joueurVaChercherABoire:
    show bolb with moveinbottom
    bol "C'est merveilleux, c'est parfait, c'est génial ! Mais il ne faut pas que mon patron sache !"
    j "Je ne savais pas qu'il était si tyrannique..."
    play sound "ef_embarrassed.wav"
    bol embarrassed "En fait, je ne supporte pas bien l'alcool, mais j'adore cette invention humaine. Surtout le vin rouge."
    j "D'accord."

    menu:
        "Prendre du vin rouge":
            jump vinRouge
        "Prendre de la Vodka":
            jump vodka

label vodka:
    #TODO Scene Baground loge
    scene bg room with dissolve
    play sound "ef_angry.wav"

    show bolb angry:
        xalign 0.5
        yalign 1.5
    with hpunch

    bol angry "De la Vodka ? Il n'y avait que ça ?"
    bol default "Bon..."
    bol "Juste un petit verre alors."
    scene bg room with dissolve
    show bolb happy:
        xalign 0.5
        yalign 1.5
    with dissolve
    play sound "ef_shortjoy.wav"
    bol happy "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?"
    menu:
        "Garder un silence gênant.":
            bol sad "..."
            play sound "ef_shortsad.wav"
            bol sad "C'est pas drôle, n'est ce pas ?"

        "Lui dire que sa blague n'est pas drôle.":
            bol sad "..."
            play sound "ef_shortsad.wav"
            bol sad "Mais..."

    play sound "ef_angry.wav"
    show bolb angry with hpunch
    bol angry "Vous êtes tous les mêmes, vous les humains."
    bol angry "Vous servez à rien."
    bol angry "Vous êtes répugnants."
    bol angry "Je vous déteste."
    bol angry "J'aurais du rester sur ma planète."
    bol angry "Et me faire exploser comme tout le monde."
    bol angry "Et pourtant je suis là."
    play sound "ef_angry.wav"
    bol angry "A vivre une vie misérable en train de m'étouffer avec vos quilles et vos balles."
    bol angry "Rien ne sert plus à rien."
    menu:
        "Il suffit ! Je ne suis pas là pour t'entendre de plaindre !":
            j "Et c'est toi qui le dis ! Tu aurais du faire comme tu dis."
            j "Toi et ton espèce de diformes décimés avez eu ce que vous méritez !"
            bol "..."
            play sound "ef_shortsad.wav"
            bol sad "Tu avais l'air pourtant d'être une personne différente..."
            bol sad "Nous pouvons en rester là. Je vais te demander de partir."
            j "Je n'ai pas besoin de ta permission, boulette."
            jump travailTriste
        "Pardon Bolb, je ne voulais pas t'offenser.":
            jump maisonHeureux


label vinRouge:
    scene bg room with dissolve
    play sound "ef_shortjoy.wav"

    show bolb happy:
        xalign 0.5
        yalign 1.5


    bol happy "Uhuhuhuh du vin !"
    bol happy "Du bordeaux en plus ! Quel régal !"
    play sound "ef_shortjoy.wav"
    bol happy "Que la fête commence !"
    #TODO Dissolve to black
    scene bg room with fade

    show bolb:
        xalign 0.5
        yalign 1.5
    with dissolve

    bol happy "... Et c'est comme ça que j'ai perdu la cuillère ! La cuillère ! T'imagines ?"
    play sound "ef_shortjoy.wav"
    bol happy "Oh regarde !"
    #TODO Dissolve bolb
    show bolb purple:
        xalign 0.5
        yalign 1.5
    with dissolve


    bol purple "Oulà ! Regarde, mon corps !"
    bol purple "Je deviens mauve hihi." 
    $ Achievement.add(achievement_name['wine'])
    bol purple "J'en connais un qui ne sera pas content demain..."
    bol purple "Je sais que je ne t'ai pas dis, mais je ne digère pas bien les boissons..."
    jump maisonHeureux

label maisonHeureux:
    bol "..."
    play sound "ef_embarrassed.wav"
    bol embarrassed "Merci."
    bol embarrassed "Je ne me suis jamais senti accueilli comme ça."
    bol embarrassed "Tu vas presque me redonner le sourire."
    scene bg finale with fade
    bol happy "Prenons encore un petit quelque chose et finissons notre soirée tranquillement."

    return



label travailTriste:

    scene bg circus with dissolve
    show bolb:
        xalign 0.6
        yalign 0.6
    with dissolve

    bol "D'accord."
    play sound "ef_shortsad.wav"
    bol sad "Moi qui pensait qu'on pourrait passer une soirée sympathique malgré tout." #TODO Bolb sad
    bol "C'est pas grave, on aura peut-être encore l'occasion de se revoir." #TODO Bolb sad
    bol "Rentre bien."
    scene bg black
    $ Achievement.add(achievement_name['lonely'])
    "" "Vous rentrez seul à la maison."
    extend "Votre aventure blobesque touche à sa fin. Une prochaine fois sera plus exitante !"
    return
