import random
import os

################
# Lists/Dictionaries
################

abil_mod = ("-3",
            "-2", "-2",
            "-1", "-1", "-1",
            "0", "0", "0", "0", "0",
            "+1", "+1", "+1",
            "+2", "+2",
            "+3",)

weather_list = [
    "Lifeless grey.",
    "Hammering rain.",
    "Piercing wind.",
    "Deafening storm.",
    "Black as night.",
    "Dead quiet.",
    "Cloudburst.",
    "Soup-thick mist.",
    "Crackling frost.",
    "Irritating drizzle.",
    "Roaring thunder.",
    "Grave-like cold.",
    "Calm skies.",
]
traps_list = [
    "A well dressed corpse, booby trapped.", "Wall-holes shoot poisonous arrows.",
    "Bells and marbles on the floor.", "Scorpion filled basket poised to fall.",
    "Fish hooks hanging at eye level.", "Chest marked with explosive runes.",
    "Lock trapped with a vial of poisonous gas.", "Jewel removal leads to roof collapse.",
    "Slanted floor, translucent oil, a pit.", "Snake cages on collapsing ceiling tiles.",
    "Evil urns release cold ghost.", "Coins coated in grime and poison.", "None.",
]
occult_treasures_list = [
    "ash-grey ring", "vile flute", "famine spoon",
    "malevolent mirror", "vampiric phubra", "black pearl",
    "immortal torch", "silver bird cage", "black crown of the crippled king",
    "ancient blindfold", "none",
]
dungeon_prefix = [
    "Slaughter", "Death", "Night", "Hadean",
    "Hell", "Plague", "Sin", "Doom",
    "Dark", "Murder", "Torture", "Slave",
]
dungeon_suffix = [
    "Pit", "Church", "Temple", "Tunnels",
    "Crypt", "Grave", "Fort", "Ziggurat",
    "Den", "Maze", "House", "Waste",
]
imm_dang_list = [
    "Is slowly flooding with oil.", "Is slowly flooding with water.", "Berserkers are appearing.",
    "Is about to collapse.", "Senses are being distorted.", "Underworld emissions of toxic spores.",
    "A hunted cult intends it to be their new hideout.", "A terrible dormant curse about to be unleashed.",
    "Fire is spreading from the deepest chamber.", "The gate will shut and seal for 7 days.",
    "A lethal mechanism is about to activate.",
]
weapon_list = [
    "Battle axe | Dmg: d8 | Value: 35s",
    "Bow | Dmg: d6 | Value: 25s",
    "Club | Dmg: d6 | Value: 10s",
    "Crossbow | Dmg: d8 | Value: 40s",
    "Flail | Dmg: d8 | Value: 35s",
    "Femur | Dmg: d4 | Value: Worthless",
    "Handaxe | Dmg: d6 | Value: 15s",
    "Knife | Dmg: d4 | Value: 10s",
    "Mace | Dmg: d6 | Value: 25s",
    "Shortbow | Dmg: d4 | Value: 13s",
    "Shortsword | Dmg: d4 | Value: 20s",
    "Sling | Dmg: d4 | Value: 8s",
    "Staff | Dmg: d4 | Value: 5s",
    "Sword | Dmg: d6 | Value: 30s",
    "Warhammer | Dmg: d6 | Value: 30s",
    "Whip | Dmg: d2 | Value: 5s",
    "Zweihander | Dmg: d10 | Value: 60s",
]
service_list = [
    "Night in hospice | Cost: 3s",
    "Drink | Cost: 1s",
    "Steady meal | Cost: 2s",
    "Bribe, Guard | Cost: 20-40s",
    "Bribe, Clerk | Cost: 30-60s",
    "Bribe, Rabble | Cost: 5-15s",
    "Repair Armor | Tier 1 to 2 | Cost: 25s",
    "Repair Armor | Tier 2 to 3 | Cost: 40s",
]
armor_list = [
    "No Armor | Tier: 0",
    "Light Armor | Tier: 1 | -d2 Dmg | Value: 20s",
    "Medium Armor | Tier: 2 | -d4 Dmg | DR +2 on Defence with Agility | Value: 100s",
    "Heavy Armor | Tier: 3 | -d6 Dmg | DR +4 on Agility Check | DR +2 on Defence with Agility | Value: 200s",
    "Shield | -1 Dmg | You can ignore all damage from one attack, but shield breaks. | Value: 20s",
]
equipment_list = ["1. Backpack | Holds 7 normal-sized items | Value: 6s",
                  "2. Bear trap | Presence DR14 to spot, d8 damage | Value: 20s",
                  "3. Blanket | Value: 4s",
                  "4. Caltrops | d4 damage + infection on 1 in 6 | Value: 7s",
                  "5. Chalk | Value: 1s",
                  "6. Chewing tobacco | Value: 1s",
                  "7. Crowbar | Value: 8s",
                  "8. Silver crucifix | Value: 60s",
                  "9. Wooden crucifix | Value: 8s",
                  "10. Dried food | 1 day | Value:1 s",
                  "11. Exquisite perfume | Value: 25s",
                  "12. Firesteel | Value: 4s",
                  "13. Grappling hook | Value: 12s",
                  "14. Hammer | Value: 8s",
                  "15. Heavy chain | 15 feet. | Value: 10s",
                  "16. Iron nails | 10 nails | Value: 5s",
                  "17. Ladder | Value: 7s",
                  "18. Lantern oil | Presence + 6 hours | Value: 5s",
                  "19. Lard | May function as meal for 5 days | Value: 5s",
                  "20. Large iron hook | Value: 9s",
                  "21. Lockpick | Value: 5s",
                  "22. Magnesium strip | Value: 4s",
                  "23. Manacles | Value: 10s",
                  "24. Mattress | Value: 3s",
                  "25. Meat cleaver | Value: 15s",
                  "26. Medicine box | Stops bleeding/infection and +d6 HP. Presence + 4 uses | Value: "
                  "15s",
                  "27. Metal file | Value: 10s",
                  "28. Mirror | Value: 15s",
                  "29. Muzzle | Value: 6s",
                  "30. Noose | Value: 5s",
                  "31. Oil lamp | Value: 10s",
                  "32. Poison (black) | Toughness DR14 or d6 damage + blind for one hour. 3 doses | Value: "
                  "20s",
                  "33. Poison (red) | Toughness DR12 or d10 damage. 3 doses | Value: 20s",
                  "34. Preserved corpse | Value: 66+6ds",
                  "35. Rope | 30 feet. | Value: 4s",
                  "36. Small wagon | Value: 25s",
                  "37. Tent | Value: 12s",
                  "38. Toolbox | 10 nails, hammer, small saw, tongs. | Value: 20s",
                  "39. Torch | Value: 2s",
                  "40. Sack | Holds 10 normal sized items. | Value: 3s",
                  "41. Salt | Value: 4s",
                  "42. Scissors | Value: 9s",
                  "43. Scroll | Value: Worth at least 50s to the right buyer.",
                  "44. Sharp needle | Value: 3s",
                  "45. Waterskin | 4 days of water. | Value: 4s",
                  ]
# AltCodes: 0252/0220 for ü, 0246/0214 for ö
name_list = ["Aerg-Tval", "Agn", "Belsum", "Brint", "Börda", "Daeru", "Eldar", "Felban", "Gotven", "Graft", "Grin",
             "Gritter", "Haerü", "Hargha", "Harmug", "Jotna", "Karg", "Karva", "Katla", "Keftar", "Klort", "Kratar",
             "Kutz", "Kvetin", "Lygan", "Margar", "Merkari", "Nagl", "Niduk", "Nifehl", "Prügl", "Qillnach", "Risten",
             "Svind", "Theras", "Therg", "Torvul", "Törn", "Urm", "Urvarg", "Vagal", "Vatan", "Von", "Vrakh", "Vresi",
             "Wemut",
             ]

beast_list = [
    "Dog (trained) | Value: 25s",
    "Dog (wild) | Value: 10s",
    "Horse | Value: 80s",
    "Mule | Value: 10s",
    "Rat (tamed) | Value: 8s",
]
unclean_scroll_list = [
    "1. Palms Open the Southern Gate\n    A ball of fire hits d2 creatures dealing d8 damage per creature.",
    "2. Tongue of Eris\n    A creature of your choice is confused for 10 minutes.",
    "3. Te-le-kin-esis\n    Move an object up to d10x10 feet for d6 minutes.",
    "4. Lucy-fires Levitation\n    Hover for Presence + d10 rounds.",
    "5. Nine Violet Signs Unknot the Storm\n    Produce d2 lightning bolts dealing d6 damage each.",
    "6. Daemon of Capillaries\n    One creature suffocates for d6 rounds, losing d4 HP per round.",
    "7. Foul Psychopomp\n    Summon (d6): 1-3 d4 skeletons, 4-6 d4 zombies.",
    "8. Metzhuatl Blind Your Eye\n    A creature becomes invisible for d6 rounds or until it is damaged, "
    "attack/defend with DR6.",
    "9. Eyelid Blinds the Mind\n    d4 creatures fall asleep for one hour unless the succeed a DR14 test.",
    "10. Death\n    All creatures within 30 feet lose a total of 4d10 HP.",
]
sacred_scrolls_list = [
    "Grace of a Dead Saint | d2 creatures regain d10 HP each.",
    "Grace for a Sinner | A creature of your choice gets +d6 on one roll.",
    "Whispers Pass the Gate | Ask three questions to a deceased creature.",
    "Aegis of Sorrow | A creature of your choice gains 2d6 HP for 10 rounds.",
    "Unmet Fate | One creature, dead for no more than a week, is awakened with terrible memories.",
    "Bestial Speech | You may speak with animal for d20 minutes.",
    "False Dawn/Night's Chariot | Light or pitch black for 3d10 minutes.",
    "Hermetic Step | You find all traps in your path for 2d10 minutes.",
    "Roskoe's Consuming Glare | d4 creatures lose d8 HP each.",
    "Enochian Syntax | One creature blindly obeys a single command.",
]
terrible_traits_list = [
    "Endlessly aggravated.",
    "Inferiority complex.",
    "Problems with authority.",
    "Loud mouth.",
    "Cruel.",
    "Egocentric.",
    "Nihilistic.",
    "Prone to substance abuse.",
    "Conflicted.",
    "Vindictive",
    "Cowardly.",
    "Lazy.",
    "Suspicious",
    "Ruthless.",
    "Worried.",
    "Bitter.",
    "Deceitful.",
    "Wasteful.",
    "Arrogant.",

]
omens_list = [
    "Deal maximum damage with one attack.",
    "Reroll a dice roll (yours or somoeone else's).",
    "Lower damage deal to you by d6.",
    "Neutralize a Crit or Fumble.",
    "Lower one test's DR by -4.",
]
broken_bodies_list = [
    "Staring manic gaze.",
    "Covered in blasphemous tattoos.",
    "Rotting face. Wears a mask.",
    "Lost three toes, limps.",
    "Starved: gaunt and pale.",
    "One hand replace with rusting hook (d6 damage).",
    "Decaying teeth.",
    "Hauntingly beautiful, unnervingly clean.",
    "Hands caked with sores.",
    "Cataract slowly but surely spreading in both eyes.",
    "Long tangled hair, at least one cockroach in residence.",
    "Broken, crushed ears.",
    "Juddering and stuttering from nerve damage or stress.",
    "Corpulent, ravenous, drooling.",
    "One hand lacks thumb and index finger, grips like a lobster.",
    "Red, swollen alcoholic's nose.",
    "Resting maniac face, making friends is hard.",
    "Chronic athlete's foot. Stinks.",
    "Recently slash and stinking eye covered with a patch.",
    "Nails cracked and black, maybe about to drop off.",
]
bad_habits_list = [
    "Obsessively collect small sharp stones.",
    "Won't use a blade without testing it on your own flesh.",
    "Can't stop drinking once you start.",
    "Gambling addict. Must gamble everyday. If you lose, raise and bet again.",
    "Cannot tolerate criticism of any kind. Results in rage and weeping.",
    "Unable to get to the point. Has never actually finished a story",
    "Best friend is a skull. Carry it with you, tell it everything, you trust no one more.",
    "You pick your nose so deep it bleeds.",
    "Laugh hysterically at your own jokes. Which you explain in detail.",
    "A nihilist. You insist on telling everyone you are a nihilist and explaing why.",
    "Inveterate bug eater.",
    "Stress response is aesthetic display. The worse things get the fancier you need to be.",
    "Permanent phlegm deposit in throat. Continuously cough, snort, spit, and swallow.",
    "PYROMANIAC!",
    "Consistently lost important items and forget vital facts.",
    "Insecure shit-stirrer. Will talk about whoever just left the room.",
    "You stutter when lying.",
    "You giggle insanely at the worst possible time.",
    "You whistle while trying to hide. You deny this. Whistle when 5,7,9,11, or 13 is rolled on d20.",
    "You make jewelery from the teeth of the dead. If this can be considered a bad habit.",
]
basilisks_demands_list = [
    "A sword that has killed exactly one dozen times.",
    "A widowe's wedding ring.",
    "Silver from a sinner's grave.",
    "Eyes that have seen the Shimmering Fields.",
    "The year's first-born goat.",
    "Blutday bread.",
    "The cuticle of an executed innocent.",
    "A troll's heart valves.",
    "A dagger onto which the condemned carved their victims' name.",
    "Rare anti-obsidian from the Urilian Crypts.",
    "The forbidden brew of the hermit Terion.",
    "An orgh-maggot from the ice of Kergüs.",
    "A body mutilated bu those who loved it in life.",
    "Joy's lampoon written in blood.",
    "The gall of the Chrypt-vulture.",
    "Moss upon which a dying man has slept.",
    "A child born with a third eye.",
    "A body drowned in Lake Onda.",
    "The rear molar of the Gluttonous.",
    "Gems from overflowing pockets.",
]

################
# Variables
################
clear = lambda: os.system('cls')
# equipment_roll = (random.choice(equipment_list))
rand_unclean_scroll = (random.choice(unclean_scroll_list))
rand_sacred_scroll = (random.choice(sacred_scrolls_list))
terrible_trait = (random.choice(terrible_traits_list))
broken_bodies = (random.choice(broken_bodies_list))
bad_habit = (random.choice(bad_habits_list))
basilisks_demands = (random.choice(basilisks_demands_list))
occult_treasures = (random.choice(occult_treasures_list))


def main_menu():
    print("")
    print("++++++++++++++++MAIN MENU++++++++++++++++++++")
    print("")
    print("      1>     (N)ew Character                  ")
    print("      2>     (R)oll Dice                      ")
    print("      3>     (I)nitiative                     ")
    print("      4>     E(X)perience Calculator          ")
    print("      5>     (L)oot Tables                    ")
    print("      6>     (C)reate Dungeon                 ")
    print("      7>     (S)hops                          ")
    print("      0>     (E)nd                            ")
    print("")
    print("++++++++++++++++MAIN MENU++++++++++++++++++++")
    choice = input("Select Option:    ").lower()
    if choice in ("n", "1"):
        print("")
        create_char()
        print("")
    elif choice in ("r", "2",):
        print("")
        select_roll()
        print("")
    elif choice in ("i", "3",):
        print("")
        print("Coming soon!")
        print("")
        main_menu()
    elif choice in ("x", "4",):
        print("")
        print("Coming soon!")
        print("")
        main_menu()
    elif choice in ("l", "5",):
        print("")
        weapon_found()
        print("")
    elif choice in ("c", "6"):
        dungeon()
    elif choice in ("7", "s",):
        print("")
        clear()
        equipment()
        print("")
    elif choice in ("e", "end", "0"):
        print("")
        print("Leaving game")
        print("")
        quit()
    else:
        print('')
        print("Not an option kimosabe...")
        print("")
        main_menu()


def equipment():
    print("Equipment and Beasts:\n#############  ")
    for _ in equipment_list:
        print(_)
    for _ in beast_list:
        print(_)
    print("")
    input("Press Enter to return to Main Menu:   ")
    print("")
    clear()
    main_menu()


def dungeon():
    print("")
    dung_name()
    imm_dang()
    weather()
    trap()
    print("")
    reroll = input("Press Enter to Reroll or Q to Quit:    ")
    if reroll in ("Q", "q"):
        main_menu()
    else:
        clear()
        dungeon()


def weather():
    weather_ext = random.choice(weather_list)
    print("        Weather: ", weather_ext)


def trap():
    traps = random.choice(traps_list)
    print("        Traps:   ", traps)


def imm_dang():
    danger = random.choice(imm_dang_list)
    print("        Dangers: ", danger)


def dung_name():
    first = random.choice(dungeon_prefix)
    last = random.choice(dungeon_suffix)
    print("        Dungeon:  The", first + " " + last)


def weapon_found():
    clear()
    wep = random.choice(weapon_list)
    print("        You found:", wep)
    reroll = input("Press Enter to Reroll or Q to Quit:    ")
    if reroll in ("Q", "q"):
        main_menu()
    else:
        weapon_found()


def select_roll():
    clear()
    myroll = []
    print("")
    print("+++Select die+++\n",
          "    d(2)       \n",
          "    d(4)       \n",
          "    d(6)       \n",
          "    d(8)       \n",
          "    d(12)      \n",
          "    d(20)      \n",
          "    d(100)     \n",
          )
    print("")
    die = int(input("Enter Die:    "))
    print("")
    num_die = int(input("How many rolls?:    "))
    print("")
    while num_die > 0:
        x = random.randint(1, die)
        myroll.append(x)
        num_die = num_die - 1
    else:
        print(myroll)
        print("")
        total = sum(myroll)
        print("Total Roll:", total)
        print("")
        reroll = input("Press Enter to Reroll or Q to Quit:    ")
        if reroll in ("Q", "q"):
            main_menu()
        else:
            select_roll()


def create_char():
    global name
    clear()
    choice = input("Random Name? Y/N:\n")
    if choice in ("y", "Y"):
        name = random.choice(name_list)
        print("Welcome", name)
    else:
        name = input("Enter Name:\n")
        print("Welcome", name, "\n",)
    option = input("(C)ustom Class or (S)elect pre-made.\n")
    if option in ("C", "c",):
        option = input("(R)andom Stats?: Y/N:\n")
        if option in ("y", "Y",):
            clear()
            custom_class2()
        else:
            clear()
            main_menu()


def custom_class():
    roll = 3
    agility_tot = []
    presence_tot = []
    strength_tot = []
    toughness_tot = []
    while roll > 0:
        xagi = int(random.randint(1, 7))
        agility_tot.append(xagi)
        xpres = int(random.randint(1, 7))
        presence_tot.append(xpres)
        xstr = int(random.randint(1, 7))
        strength_tot.append(xstr)
        xtou = int(random.randint(1, 7))
        toughness_tot.append(xtou)
        roll = roll - 1
    else:
        print("\n",
              "Name:", name, "\n",
              "Agility:", sum(agility_tot), "\n",
              "Presence:", sum(presence_tot), "\n",
              "Strength:", sum(strength_tot), "\n",
              "Toughness:", sum(toughness_tot), "\n",
              "\n",
              )
        reroll = input("Press Enter to reroll or Q to Quit:    ")
        if reroll in ("Q", "q"):
            main_menu()
        else:
            custom_class()


def custom_class2():
    agility = random.choice(abil_mod)
    presence = random.choice(abil_mod)
    strength = random.choice(abil_mod)
    toughness = random.choice(abil_mod)
    print("\n",
              "Name:", name, "\n", "\n",
              "Agility:", agility, "\n",
              "Presence:", presence, "\n",
              "Strength:", strength, "\n",
              "Toughness:", toughness, "\n",
              "\n",
              )
    redo = input("Press Enter to redo or Q to Quit:    ")
    if redo in ("Q", "q"):
        main_menu()
    else:
        custom_class2()






# dnum = input("Select # of Die   ")
# dmod = input("Add Modifier?:   ")

clear()
main_menu()
