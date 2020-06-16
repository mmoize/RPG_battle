
from classes.game import Person, bcolours
from classes.magic import Spell

# Create black damage
fire = Spell ("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 15, 120, "black")

# Create white magic

cure = Spell("cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Instantiate Magic
player = Person(465, 65, 60, 34,[fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 48, 26, [])

magic = [
    {"name": "Fire", "cost": 10, "dmg": 100},
    {"name": "Thunder", "cost": 10, "dmg": 130},
    {"name": "Storm", "cost": 10, "dmg": 60}
]



running = True
i = 0

print(bcolours.FAIL + bcolours.BOLD + "An ENEMY ATTACKS!" + bcolours.ENDC)
print("this is normal text")
while running:
    print("=======================")
    player.choose_action()
    choice = int(input("Choose action: ")) 
    index = choice - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damge(dmg)
        print("you attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolours.FAIL + "\nNot Enough MP\n" + bcolours.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damge(magic_dmg)
        print(bcolours.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damge" + bcolours.ENDC)
    

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damge(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())
    
    print("==========================================")
    print("Enemy HP:", bcolours.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolours.ENDC + "\n")
     
    print("Your Hp:", bcolours.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolours.ENDC)
    print("Your MP:", bcolours.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolours.ENDC)


    if enemy.get_hp() == 0:
        print(bcolours.OKBLUE + "You win" + bcolours.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(bcolours.FAIL + "Your Enemy has defeated you!" + bcolours.ENDC)
        running = False

