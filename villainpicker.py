import random
import webbrowser

# Define the players
players = ["Todd", "Toby", "Paul"]
image = "https://www.ravensburger.us/content/wcm/mediadata/images/Discover/Theme_Specials/03_Games/2021/Villainous%20Page/05_21_Discover_03Games_DisneyVillainous_WTCGame_Desktop_1045x1045.jpg"

# Define the characters and their corresponding image URLs
characters = {
    "Maleficent": "https://static.wikia.nocookie.net/disney-villainous/images/e/e8/Maleficent.png/revision/latest/scale-to-width-down/1000?cb=20210503154728",
    "Jafar": "https://static.wikia.nocookie.net/disney-villainous/images/0/00/Captain_Hook.png/revision/latest?cb=20210503154529",
    "Ursula": "https://static.wikia.nocookie.net/disney-villainous/images/a/a4/Ursula.png/revision/latest?cb=20210503155134",
    "Captain Hook": "https://static.wikia.nocookie.net/disney-villainous/images/0/00/Captain_Hook.png/revision/latest?cb=20210503154529",
    "Queen of Hearts": "https://static.wikia.nocookie.net/disney-villainous/images/d/da/Queen_of_Hearts.png/revision/latest?cb=20210503154821",
    "Prince John": "https://static.wikia.nocookie.net/disney-villainous/images/4/4a/Prince_John.png/revision/latest?cb=20210503154958",
    "Hades": "https://static.wikia.nocookie.net/disney-villainous/images/6/64/Hades.png/revision/latest?cb=20210503155317",
    "Dr Facilier": "https://static.wikia.nocookie.net/disney-villainous/images/4/49/Dr_Facilier.png/revision/latest?cb=20210503155211",
    "Evil Queen": "https://static.wikia.nocookie.net/disney-villainous/images/d/d5/Evil_Queen.png/revision/latest?cb=20210503155250",
    "Scar": "https://static.wikia.nocookie.net/disney-villainous/images/c/c7/Scar.png/revision/latest?cb=20210503155351",
    "Yizma": "https://static.wikia.nocookie.net/disney-villainous/images/7/71/Yzma.png/revision/latest?cb=20210503155405",
    "Ratigan": "https://static.wikia.nocookie.net/disney-villainous/images/3/36/Ratigan.png/revision/latest?cb=20210503155340",
    "Cruela Deville": "https://static.wikia.nocookie.net/disney-villainous/images/d/de/Cruella_De_Vil.png/revision/latest?cb=20210503155419",
    "Mother Gothel": "https://static.wikia.nocookie.net/disney-villainous/images/0/02/Mother_Gothel.png/revision/latest?cb=20210503155433",
    "Pete": "https://static.wikia.nocookie.net/disney-villainous/images/8/89/Pete.png/revision/latest?cb=20210503155447",
    "Gaston": "https://static.wikia.nocookie.net/disney-villainous/images/d/de/Gaston.png/revision/latest?cb=20210503155502",
    "Lady Tremane": "https://static.wikia.nocookie.net/disney-villainous/images/1/15/Lady_Tremaine.png/revision/latest?cb=20210503155614",
    "Horned King": "https://static.wikia.nocookie.net/disney-villainous/images/8/82/Horned_King.png/revision/latest?cb=20210503155609",
    "Syndrome": "https://static.wikia.nocookie.net/disney-villainous/images/b/b3/Syndrome.png/revision/latest?cb=20230116215921",
    "Lostso": "https://static.wikia.nocookie.net/disney-villainous/images/6/6d/Lotso.png/revision/latest?cb=20230116215710",
    "Madam Mim": "https://static.wikia.nocookie.net/disney-villainous/images/7/7a/Madam_Mim.png/revision/latest?cb=20230116215808",
    "Oogie Boogie": "https://static.wikia.nocookie.net/disney-villainous/images/b/b3/Syndrome.png/revision/latest?cb=20230116215921",
    "King Candy": "https://static.wikia.nocookie.net/disney-villainous/images/5/57/King_Candy.png/revision/latest?cb=20240610183537",
    "Shere Khan": "https://static.wikia.nocookie.net/disney-villainous/images/8/8e/Shere_Khan.png/revision/latest?cb=20240610183454"
}

# Randomly assign a character to each player
for player in players:
    character, url = random.choice(list(characters.items()))
    print(f"{player} has been assigned {character}")
    webbrowser.open(url)

# randomly pick a player to go first
first_player = random.choice(players)
print(f"{first_player} goes first!")
