import random
import webbrowser
import os
import json

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
    "Lotso": "https://static.wikia.nocookie.net/disney-villainous/images/6/6d/Lotso.png/revision/latest?cb=20230116215710",
    "Madam Mim": "https://static.wikia.nocookie.net/disney-villainous/images/7/7a/Madam_Mim.png/revision/latest?cb=20230116215808",
    "Oogie Boogie": "https://static.wikia.nocookie.net/disney-villainous/images/b/b3/Syndrome.png/revision/latest?cb=20230116215921",
    "King Candy": "https://static.wikia.nocookie.net/disney-villainous/images/5/57/King_Candy.png/revision/latest?cb=20240610183537",
    "Shere Khan": "https://static.wikia.nocookie.net/disney-villainous/images/8/8e/Shere_Khan.png/revision/latest?cb=20240610183454"
}

# Generate the HTML content with JavaScript for dynamic player input and assignment
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Disney Villainous Character Assignments</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding: 20px;
            flex-wrap: wrap;
        }
        .character {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 10px;
            cursor: pointer;
        }
        img {
            max-width: 200px;
            border-radius: 10px;
        }
        h2 {
            margin: 10px 0;
        }
        button {
            font-size: 20px;
            padding: 10px 20px;
            margin: 20px;
            cursor: pointer;
        }
        input {
            font-size: 20px;
            padding: 10px;
            margin: 5px;
            text-align: center;
        }
    </style>
    <script>
        let characters = """ + json.dumps(characters) + """;
        let assignments = {};
        let players = [];

        function addPlayers() {
            const playerContainer = document.querySelector('.player-container');
            playerContainer.innerHTML = '';
            for (let i = 1; i <= 6; i++) {
                const playerInput = document.createElement('input');
                playerInput.type = 'text';
                playerInput.placeholder = 'Player ' + i;
                playerInput.id = 'player' + i;
                playerContainer.appendChild(playerInput);
            }
        }

        function chooseVillains() {
            players = [];
            for (let i = 1; i <= 6; i++) {
                const playerName = document.getElementById('player' + i).value.trim();
                if (playerName) {
                    players.push(playerName);
                }
            }
            if (players.length === 0) {
                alert('Please add at least one player.');
                return;
            }

            assignments = assignCharactersToPlayers(players, characters);
            const container = document.querySelector('.container');
            container.innerHTML = '';
            for (const [player, [character, image]] of Object.entries(assignments)) {
                const characterDiv = document.createElement('div');
                characterDiv.className = 'character';
                characterDiv.id = player;
                characterDiv.innerHTML = `
                    <img src="${image}" alt="${character}" onclick="reassignCharacter('${player}')">
                    <h2>${player}</h2>
                `;
                container.appendChild(characterDiv);
            }

            // Remove player input fields after choosing villains
            const playerContainer = document.querySelector('.player-container');
            playerContainer.innerHTML = '';
        }

        function reassignCharacter(player) {
            const characterKeys = Object.keys(characters);
            const newCharacterKey = characterKeys[Math.floor(Math.random() * characterKeys.length)];
            const newCharacter = [newCharacterKey, characters[newCharacterKey]];
            assignments[player] = newCharacter;
            const playerDiv = document.getElementById(player);
            playerDiv.innerHTML = `
                <img src="${newCharacter[1]}" alt="${newCharacter[0]}" onclick="reassignCharacter('${player}')">
                <h2>${player}</h2>
            `;
        }

        function assignCharactersToPlayers(players, characters) {
            let assignments = {};
            let characterList = Object.keys(characters);
            randomShuffle(characterList);
            for (let player of players) {
                let character = characterList.pop();
                let image = characters[character];
                assignments[player] = [character, image];
            }
            return assignments;
        }

        function randomShuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }
    </script>
</head>
<body>
    <h1>Disney Villainous Character Assignments</h1>
    <button onclick="addPlayers()">Add Players</button>
    <div class="player-container"></div>
    <button onclick="chooseVillains()">Let's Choose Your Villains</button>
    <div class="container"></div>
</body>
</html>
"""

# Save the HTML content to a file
html_file = 'character_assignments.html'
with open(html_file, 'w') as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath(html_file))
