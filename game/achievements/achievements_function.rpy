python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', priority=None, **kwargs):
            ## The name of the achievement.
            self.name = name

            ## The image of the achievement.
            if image == '':
                ## If image is None, a default image will be used.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')

            ## The message associated with the achievement.
            self.message = message

            ## Set the priority of the achievement.
            ##            None = default (greyed out and can see the name and description of the achievement.)
            ##        'hidden' = Achievements with this tag will be displayed as 'hidden'.
            ##      'platinum' = The final achievement to be granted once all other achievements have been granted.
            self.priority = priority

        def __eq__(self, value):
            ## Since we are using a persistent list we need to do an equality check.
            ## Below we are simply checking 'self.name == value.name, self.message == value.message'
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            ## Add/Grant Trophies/Achievements to the list.
            ## As a standard python expression  ::  Achievement.add( <trophy> )
            ## As a screen action  ::  Function( Achievement.add, <trophy> )
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_is_done = False
                store.achievement_notification_timer = 3.0
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)
            achievement.sync()

        def purge(self):
            ## This will clear the achievements AND persistent list.
            ## As a standard python expression  ::  achievements.purge()
            ## As a screen action  ::  Function( achievements.purge )
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    ## Note - This has not been implemented to work with Steam.
    ##        You'll have to work that out on your own if you want it to work with steam.
    ##        I have left some Steam stuff in place, but these haven't been elaborated upon.
    achievement.steam_position = "bottom right"

    achievement_name = {

        ## -------------------------- IMPORTANT (1) --------------------------
        ## 
        ## How to set up achievements
        ## "achievement_key": Achievement(name=_("Name of Achievement"), message=_("Description"), image='<image_path_here>', priority='<type>'),

        ## -------------------------- IMPORTANT (2) --------------------------
        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## -------------------------- EXAMPLES -------------------------- 
        "strike": Achievement(name=_("Strike !"), message=_("Obtenir une quille."), image='gui/ACH/ACH_strike.png', priority=None),
        "wine": Achievement(name=_("Red Red Wine"), message=_("Bleu et rouge fait un beau mélange."), image='gui/ACH/ACH_wine.png', priority=None),
        "blobsolo": Achievement(name=_("Mieux vaux être seul que blob accompagné"), message=_("Laisser Bolb dans sa morve."), image='gui/ACH/ACH_blobsolo.png', priority=None),
        "sparta": Achievement(name=_("THIS. IS. SPARTA!"), message=_("Du calme, c'est juste une porte."), image='gui/ACH/ACH_sparta.png', priority=None),
        "lonely": Achievement(name=_("L'argent ne fait pas le bonheur"), message=_("Vous êtes riches mais seul."), image='gui/ACH/ACH_lonely.png', priority=None),
        "4554": Achievement(name=_("4554"), message=_("C'est une perte importante pour le jeu, mais meilleur pour ta santé."), image='gui/ACH/ACH_4554.png', priority=None),
        "unknown": Achievement(name=_("Metamorph"), message=_("On ne peut plus faire la différence."), image='gui/ACH/ACH_unknown.png', priority=None),



        ## The prio, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the types of achievements;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as 'hidden'.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        #"secret": Achievement(name=_("Shh... It's a secret."), message=_("Discover the secret."), image='gui/trophy_icon.png', priority='hidden'),
        "wow": Achievement(name=_("La star"), message=_("Obtenir tous les achievements."), image='gui/trophy_icon.png', priority='platinum'),

        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

