
from classes.game import Person, bcolours

magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 10, "dmg": 85},
    {"name": "Storm", "cost": 10, "dmg": 60}
]

player = Person(465, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_spell_damage(1))