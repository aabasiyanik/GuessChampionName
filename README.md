# GuessChampionName

## Purpose and Inspiration
'League of Legends Champion Guessing Game' is a manifestation of my childhood fascination with Akinator and my ongoing passion for programming and gaming. I like coding and I love League of Legends, so this project was super fun for me. It's a game where you think of a champion from the game, and then the program asks you questions to figure out which champion you're thinking of.

## Technologies
I used Python to make this program. It starts by asking simple questions to narrow down the options, like what role the champion plays or the source they use. As you answer, the program gets smarter and starts asking more specific questions based on what you say.

## Data & API

When I was thinking of this project, first I needed data. A JSON file where I will have all the uniqueness about the specific champion. Thanks to the Riot Games developer I was easily able to use the RIOT GAMES API. What I did was extract all the information that was needed for my project into a file called 'champinfo.json'. I made my own JSON file by specifically creating new items.
Sample Code:
```python
import json

with open('location.json', 'r', encoding='utf-8') as location_file:
    location_data = json.load(location_file)

with open('champinfo.json', 'r', encoding='utf-8') as champinfo_file:
    champinfo_data = json.load(champinfo_file)

for location, champions in location_data.items():
    for champion_name in champions:
        if champion_name in champinfo_data:
            champion_info = champinfo_data[champion_name]
            magic_attack = champion_info['info']
            if magic_attack['magic'] > magic_attack['attack']:
                source = 'AP'
            else:
                source = 'AD'
            champion_info['Source'] = source
            champion_info['Location'] = location

with open('champinfo.json', 'w') as champinfo_file:
    json.dump(champinfo_data, champinfo_file, indent=4)
```

## Disclaimer
GuessChampionName was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games.  Riot Games does not endorse or sponsor this project.

## Sources

To determine where each champion was from I used the official League of Legends website: https://universe.leagueoflegends.com/en_US/regions/

