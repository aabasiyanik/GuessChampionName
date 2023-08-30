import json
from collections import deque
from os import system, name
# from random import shuffle

def clear():
   if name == 'nt':
      _ = system('cls')

with open('champinfo.json', 'r') as json_file:
    champion_data = json.load(json_file)

champions = deque([champion for champion in champion_data])

questions = [
    "Is the champion from Noxus?",
    "Does the champion primarily use mana as their resource?",
    "Is the champion primarily a mage, using spells for most of their damage?",
    "Is the champion typically played in the mid lane?",
    "Is the voice actor of the champion female?",
    "Is your champion considered ranged?",
    "Is your champion considered Darkin?",
    "Is your champion considered Vastaya?",
    "Can the champion transform or change forms?"
    ]
# shuffle(questions)

def ask(question):
    clear()
    response = input(question + " (yes, no): ").lower()
    return response == "yes"

def quiz(champions, questions):
    for question in questions:
        filtered = []
        if question != "Is your champion considered Darkin?" and question != "Is your champion considered Vastaya?" and question != "Can the champion transform or change forms?":
            answer = ask(question)

        if question == "Does the champion primarily use mana as their resource?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["partype"] == "Mana":
                    filtered.append(champion_name)
        elif question == "Does the champion primarily use mana as their resource?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["partype"] != "Mana":
                    filtered.append(champion_name)
            
            if len(filtered) > 0:
                champions = deque(filtered)
            if len(champions) == 1:
                return champions[0]
            answer = ask("Does the champion use energy instead of mana?")
            filtered = []

            if answer:
                for champion_name in champions:
                    if champion_data[champion_name]["partype"] == "Energy":
                        filtered.append(champion_name)
            elif not answer:
                for champion_name in champions:
                    if champion_data[champion_name]["partype"] != "Energy":
                        filtered.append(champion_name)






        if question == "Is the champion from Noxus?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["Location"] == "Noxus":
                    filtered.append(champion_name)
        elif question == "Is the champion from Noxus?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["Location"] != "Noxus":
                    filtered.append(champion_name)
            
            if len(filtered) > 0:
                champions = deque(filtered)
            if len(champions) == 1:
                return champions[0]
            answer = ask("Is the champion from Demacia?")
            filtered = []

            if answer:
                for champion_name in champions:
                    if champion_data[champion_name]["Location"] == "Demacia":
                        filtered.append(champion_name)
            elif not answer:
                for champion_name in champions:
                    if champion_data[champion_name]["Location"] != "Demacia":
                        filtered.append(champion_name)


                if len(filtered) > 0:
                    champions = deque(filtered)
                if len(champions) == 1:
                    return champions[0]
                answer = ask("Is the champion from Ionia?")
                filtered = []

                if answer:
                    for champion_name in champions:
                        if champion_data[champion_name]["Location"] == "Ionia":
                            filtered.append(champion_name)
                elif not answer:
                    for champion_name in champions:
                        if champion_data[champion_name]["Location"] != "Ionia":
                            filtered.append(champion_name)


                    if len(filtered) > 0:
                        champions = deque(filtered)
                    if len(champions) == 1:
                        return champions[0]
                    answer = ask("Is the champion from Freljord?")
                    filtered = []

                    if answer:
                        for champion_name in champions:
                            if champion_data[champion_name]["Location"] == "Freljord":
                                filtered.append(champion_name)
                    elif not answer:
                        for champion_name in champions:
                            if champion_data[champion_name]["Location"] != "Freljord":
                                filtered.append(champion_name)

                        if len(filtered) > 0:
                            champions = deque(filtered)
                        if len(champions) == 1:
                            return champions[0]
                        answer = ask("Is the champion from Bilgewater?")
                        filtered = []

                        if answer:
                            for champion_name in champions:
                                if champion_data[champion_name]["Location"] == "Bilgewater":
                                    filtered.append(champion_name)
                        elif not answer:
                            for champion_name in champions:
                                if champion_data[champion_name]["Location"] != "Bilgewater":
                                    filtered.append(champion_name)

                            
                            if len(filtered) > 0:
                                champions = deque(filtered)
                            if len(champions) == 1:
                                return champions[0]
                            answer = ask("Is the champion from Zaun?")
                            filtered = []

                            if answer:
                                for champion_name in champions:
                                    if champion_data[champion_name]["Location"] == "Zaun":
                                        filtered.append(champion_name)
                            elif not answer:
                                for champion_name in champions:
                                    if champion_data[champion_name]["Location"] != "Zaun":
                                        filtered.append(champion_name)


                                if len(filtered) > 0:
                                    champions = deque(filtered)
                                if len(champions) == 1:
                                    return champions[0]
                                answer = ask("Is the champion from Shurima?")
                                filtered = []

                                if answer:
                                    for champion_name in champions:
                                        if champion_data[champion_name]["Location"] == "Shurima":
                                            filtered.append(champion_name)
                                elif not answer:
                                    for champion_name in champions:
                                        if champion_data[champion_name]["Location"] != "Shurima":
                                            filtered.append(champion_name)
                                
                                    if len(filtered) > 0:
                                        champions = deque(filtered)
                                    if len(champions) == 1:
                                        return champions[0]
                                    answer = ask("Is the champion from Targon?")
                                    filtered = []

                                    if answer:
                                        for champion_name in champions:
                                            if champion_data[champion_name]["Location"] == "Targon":
                                                filtered.append(champion_name)
                                    elif not answer:
                                        for champion_name in champions:
                                            if champion_data[champion_name]["Location"] != "Targon":
                                                filtered.append(champion_name)

                                        
                                        if len(filtered) > 0:
                                            champions = deque(filtered)
                                        if len(champions) == 1:
                                            return champions[0]
                                        answer = ask("Is the champion from Void?")
                                        filtered = []

                                        if answer:
                                            for champion_name in champions:
                                                if champion_data[champion_name]["Location"] == "Void":
                                                    filtered.append(champion_name)
                                        elif not answer:
                                            for champion_name in champions:
                                                if champion_data[champion_name]["Location"] != "Void":
                                                    filtered.append(champion_name)
                                                

                                            if len(filtered) > 0:
                                                champions = deque(filtered)
                                            if len(champions) == 1:
                                                return champions[0]
                                            answer = ask("Is the champion from Bandle City?")
                                            filtered = []

                                            if answer:
                                                for champion_name in champions:
                                                    if champion_data[champion_name]["Location"] == "Bandle City":
                                                        filtered.append(champion_name)
                                            elif not answer:
                                                for champion_name in champions:
                                                    if champion_data[champion_name]["Location"] != "Bandle City":
                                                        filtered.append(champion_name)

                                                if len(filtered) > 0:
                                                    champions = deque(filtered)
                                                if len(champions) == 1:
                                                    return champions[0]
                                                answer = ask("Is the champion from Shadow Isles?")
                                                filtered = []

                                                if answer:
                                                    for champion_name in champions:
                                                        if champion_data[champion_name]["Location"] == "Shadow Isles":
                                                            filtered.append(champion_name)
                                                elif not answer:
                                                    for champion_name in champions:
                                                        if champion_data[champion_name]["Location"] != "Shadow Isles":
                                                            filtered.append(champion_name)

                                                    if len(filtered) > 0:
                                                        champions = deque(filtered)
                                                    if len(champions) == 1:
                                                        return champions[0]
                                                    answer = ask("Is the champion from Piltover?")
                                                    filtered = []

                                                    if answer:
                                                        for champion_name in champions:
                                                            if champion_data[champion_name]["Location"] == "Piltover":
                                                                filtered.append(champion_name)
                                                    elif not answer:
                                                        for champion_name in champions:
                                                            if champion_data[champion_name]["Location"] != "Piltover":
                                                                filtered.append(champion_name)
                                                        
                                                        if len(filtered) > 0:
                                                            champions = deque(filtered)
                                                        if len(champions) == 1:
                                                            return champions[0]
                                                        answer = ask("Is the champion from Ixtal?")
                                                        filtered = []

                                                        if answer:
                                                            for champion_name in champions:
                                                                if champion_data[champion_name]["Location"] == "Ixtal":
                                                                    filtered.append(champion_name)
                                                        elif not answer:
                                                            for champion_name in champions:
                                                                if champion_data[champion_name]["Location"] != "Ixtal":
                                                                    filtered.append(champion_name)










        if question == "Is the champion typically played in the mid lane?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["Role"] == "Mid":
                    filtered.append(champion_name)
        elif question == "Is the champion typically played in the mid lane?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["Role"] != "Mid":
                    filtered.append(champion_name)
            

            if len(filtered) > 0:
                champions = deque(filtered)
            if len(champions) == 1:
                return champions[0]
            
            answer = ask("Is the champion typically played in the top lane?")
            filtered = []

            if answer:
                for champion_name in champions:
                    if champion_data[champion_name]["Role"] == "Top":
                        filtered.append(champion_name)
            elif not answer:
                for champion_name in champions:
                    if champion_data[champion_name]["Role"] != "Top":
                        filtered.append(champion_name)
                
                if len(filtered) > 0:
                    champions = deque(filtered)
                if len(champions) == 1:
                    return champions[0]
                
                answer = ask("Is the champion typically played in the jungle lane?")
                filtered = []

                if answer:
                    for champion_name in champions:
                        if champion_data[champion_name]["Role"] == "Jungle":
                            filtered.append(champion_name)
                elif not answer:
                    for champion_name in champions:
                        if champion_data[champion_name]["Role"] != "Jungle":
                            filtered.append(champion_name)

                    if len(filtered) > 0:
                        champions = deque(filtered)
                    if len(champions) == 1:
                        return champions[0]
                    

                    filtered = []
                    for champion_name in champions:
                            if champion_data[champion_name]["Source"] == "AD":
                                filtered.append(champion_name)

                    if len(filtered) > 0:
                        answer = ask("Is the champion typically played as an ADC?")
                        filtered = []

                        if answer:
                            for champion_name in champions:
                                if champion_data[champion_name]["Role"] == "ADC":
                                    filtered.append(champion_name)
                        elif not answer:
                            for champion_name in champions:
                                if champion_data[champion_name]["Role"] != "ADC":
                                    filtered.append(champion_name)




        if question == "Is the champion primarily a mage, using spells for most of their damage?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["Source"] == "AP" or champion_data[champion_name]["Source"] == "Depends":
                    filtered.append(champion_name)
        elif question == "Is the champion primarily a mage, using spells for most of their damage?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["Source"] != "AP":
                    filtered.append(champion_name)


        if question == "Is your champion considered ranged?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["attackrange"] > 349:
                    filtered.append(champion_name)
        elif question == "Is your champion considered ranged?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["attackrange"] < 350:
                    filtered.append(champion_name)


        
        if question == "Is the champion female?" and answer:
            for champion_name in champions:
                if champion_data[champion_name]["gender"] == "Female":
                    filtered.append(champion_name)
        elif question == "Is the champion female?" and not answer:
            for champion_name in champions:
                if champion_data[champion_name]["gender"] != "Female":
                    filtered.append(champion_name)
        

        if question == "Can the champion transform or change forms?":
            for champion_name in champions:
                    if champion_data[champion_name]["canTransform"]:
                        filtered.append(champion_name)
            if len(filtered) > 0:
                answer = ask(question)

                if answer:
                    break
                elif not answer:
                    filtered = []
                    for champion_name in champions:
                        if not champion_data[champion_name]["canTransform"]:
                            filtered.append(champion_name)


        if question == "Is your champion considered Vastaya?":
            for champion_name in champions:
                    if champion_data[champion_name]["IsVastaya"]:
                        filtered.append(champion_name)
            if len(filtered) > 0:
                answer = ask(question)

                if answer:
                    break
                elif not answer:
                    filtered = []
                    for champion_name in champions:
                        if not champion_data[champion_name]["IsVastaya"]:
                            filtered.append(champion_name)
        

        if question == "Is your champion considered Darkin?":
            for champion_name in champions:
                if champion_data[champion_name]["IsDarkin"]:
                    filtered.append(champion_name)
            if len(filtered) > 0:
                answer = ask(question)

                if answer:
                    break
                elif not answer:
                    filtered = []
                    for champion_name in champions:
                        if not champion_data[champion_name]["IsDarkin"]:
                            filtered.append(champion_name)


        if len(filtered) > 0:
            champions = deque(filtered)
        if len(champions) == 1:
            return champions[0]
        
        if 1 < len(champions) < 3: # 2
            special = []
            for champion_name in champions:
                special = [(champion_name, champion_data[champion_name]["title"]) for champion_name in champions]
            for key, title in special:
                answer = ask(f"Is your champion {title}?")

                if answer:
                    return key
                else:
                    return special[1][0]
        
        if len(champions) < 1:
            break

    continue_ = ask("I was not able to find the champion, would you like to try again?")
    if continue_:
        quiz(champions=champions, questions=questions)
    else:
        exit()

print(quiz(champions=champions, questions=questions))