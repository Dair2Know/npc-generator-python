import json
import random
import math

# Load JSON files
with open('Firstnames.json') as f:
    Firstnames = {str(i): name for i, name in enumerate(json.load(f))}
with open('Lastnames.json') as f:
    Lastnames = {str(i): name for i, name in enumerate(json.load(f))}
with open('NPCClasses.json') as f:
    NPCClasses = json.load(f)
with open('Classes.json') as f:
    Classes = json.load(f)
with open('profession.json') as f:
    Professions = dict((i, profession) for i, profession in enumerate(json.load(f)))
with open('quirks.json') as f:
    Quirks = dict((i, quirk) for i, quirk in enumerate(json.load(f)))
with open('goals.json') as f:
    Goals = dict((i, goal) for i, goal in enumerate(json.load(f)))
with open('religion.json') as f:
    Religions = dict((i, religion) for i, religion in enumerate(json.load(f)))
with open('races.json') as f:
    Races = dict((i, race) for i, race in enumerate(json.load(f)))
with open('appearances.json') as f:
    Appearance = dict((i, appearance) for i, appearance in enumerate(json.load(f)))
with open('backstories.json') as f:
    Backstorys = {str(i): backstory for i, backstory in enumerate(json.load(f))}
with open('rumors.json', 'r') as f:
    rumors = [line.strip() for line in f.readlines()]

# Function to generate random NPC
def generate_npc():
    npc = {
        "FullName": f"{random.choice(list(Firstnames.values()))} {random.choice(list(Lastnames.values()))}",
        "Level": int(math.floor(random.triangular(2, 5, 10))) if random.random() < 0.75 else 1,
        "Age": int(math.floor(random.triangular(20, 30, 120))),
        "Class": random.choice(list(NPCClasses)) if random.random() < 0.25 else random.choice(list(Classes)),
        "Profession": random.choice(list(Professions.values())),
        "Quirk": random.choice(list(Quirks.values())),
        "Goal": random.choice(list(Goals.values())),
        "Religion": random.choice(list(Religions.values())),
        "Rumor": random.choice(list(rumors)),        
        "Race": random.choice(list(Races.values())),
        "Appearance": random.choice(list(Appearance.values())),
        "Backstory": random.choice(list(Backstorys.values()))
    }
    return npc

# Generate and output 10 NPCs
npcs = [generate_npc() for _ in range(10)]

try:
    with open('GeneratedNPCs.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []
with open('GeneratedNPCs.json', 'w') as f:
    for npc in npcs:
        if not isinstance(npc, dict):
            raise TypeError("NPC must be a dictionary")
        data.append(npc)
    json.dump(data, f, indent=4)