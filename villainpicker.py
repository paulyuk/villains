import random
import webbrowser

# Define the players
players = ["Todd", "Toby", "Paul"]
image = "https://www.ravensburger.us/content/wcm/mediadata/images/Discover/Theme_Specials/03_Games/2021/Villainous%20Page/05_21_Discover_03Games_DisneyVillainous_WTCGame_Desktop_1045x1045.jpg"

# Define the characters and their corresponding image URLs
characters = {
    "Maleficent": "https://static.wikia.nocookie.net/disney/images/0/05/Profile_-_Maleficent.jpeg/revision/latest?cb=20190312020410",
    "Jafar": image,
    "Ursula": image,
    "Captain Hook": image,
    "Queen of Hearts": image,
    "Prince John": image,
    "Hades": image,
    "Dr Facilier": image,
    "Evil Queen": image,
    "Scar": image,
    "Yizma": image,
    "Ratigan": image,
    "Cruela Deville": image,
    "Mother Gothel": image,
    "Pete": image,
    "Gaston": image,
    "Lady Tremane": image,
    "Horned King": image,
    "Syndrome": image,
    "Lostso": image,
    "Madam Mim": image,
    "Oogie Boogie": image,
    "King Candy": image,
    "Shere Khan": image
}

# Randomly assign a character to each player, and do not allow duplicate characters
for player in players:
    character, url = random.choice(list(characters.items()))
    print(f"{player} has been assigned {character}")
    del characters[character]
    webbrowser.open(url)

# randomly pick a player to go first
first_player = random.choice(players)
print(f"{first_player} goes first!")
