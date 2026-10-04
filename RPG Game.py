#RPG GAME

import random

hp = 25
mana = 20
lvl = 1
weapon_rarity = 0
magic_mastery = 0

#Following variables will be defined properly later. They are currently set to default values for testing.
enemy_armour_class = 5
enemy_health = 2
enemy = "Abadore"

#player stats will be set based on difficulty, race, class, and can be increased throughout the game by levelling up.
stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

def lvl_up(current_stats: dict, level: int, magic_mast: int):
    level += 1
    print(f"Congratulations, you're not dead yet and you levelled up to level {level}!")
    if level == 3:
        if mc_class in magic_classes:
            magic_mast += 1
            print(f"Your magic mastery is now level {magic_mast}!", f"You now do +{magic_mast} additional damage when using spells", sep="\n")
    print("Your currents stats are: ")
    for key, value in current_stats.items():
        print(f"{key}: {value}")
    print("", "Which stat would you like to increase?", sep="\n")
    for item in current_stats.keys():
        print(f"+1 {item}")
    while True:
        stat = input("Type your option here: ").strip().upper().replace(" ", "")
        if stat not in current_stats:
            print("Sorry that is not a valid stat. Please try again.")
        else:
            current_stats[stat] += 1
            print()
            print("Great choice!", end="")
            if stat == "STR":
                print(f" Enermies are starting to tremble in your presence. +1 {stat}")
            elif stat == "DEX":
                print(f" You actions become swifter, quicker, and more refined. +1 {stat}")
            elif stat == "CON":
                print(f" You become harder to kill and begin to push beyond normal pysically limits. +1 {stat}")
            elif stat == "INT":
                print(f" You begin to understand the world differently. Complex ideas become clearer, and problems that once seemed difficult become easier to solve. +1 {stat}")
            elif stat == "WIS":
                print(f" You gain a greater awareness. Patterns start to form where there was none, and you are more intuned with the world around you. +1 {stat}")
            elif stat == "CHA":
                print(f" You presense and eloquence starts to charm the even the most unfriendly folk. +1 {stat}")
            print("Your updated stats are: ")
            for key, value in current_stats.items():
                print(f"{key}: {value}")
            break
    return current_stats, level
    

#current weapon and spell attack system
class WeaponsSpells:
    def __init__(self, hit_points):
        self.hit_points = hit_points

    def damage(self):
        if enemy_health - self.hit_points > 0:
            print(f"You do {self.hit_points} points of damage")
            print(f"{enemy} health: {enemy_health} hp")

#spells subclasses
class EmberLance(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A blazing lance erupts from your hand and tears toward your foe.")
        else:
            print("The lance pierces their guard, engulfing them in a final burst of flame.")

class CrystalTorrent(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("The air crystallises around you before a jagged spear of ice flies at your enemy.")
        else:
            print("Ice races across their body before shattering them into silence.")

class BladeOfLight(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("Thunder roars overhead as a bolt of lightning tears from your fingertips.")
        else:
            print("Lightning rips through their body, leaving only a smoking shadow behind.")

class StarfallSigil(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A glowing sigil forms beneath your enemy as fragments of starlight begin to fall.")
        else:
            print("The heavens answer your command, and a blazing star crashes down upon them.")

class GravitonSnare(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("The air bends around your enemy as an invisible force crushes them toward the earth.")
        else:
            print("Gravity doubles its grip, driving your enemy into the ground with a deafening impact.")

class Voidbind(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A black tear opens behind your enemy, and tendrils of nothingness coil around them.")
        else:
            print("The void closes around them, swallowing their final scream.")

class ArcaneLeech(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("Violet energy spills from your hands, ripping life from your enemy and drawing it into you.")
        else:
            print("Their stolen life surges through your veins as their body falls lifeless.")

class RealityFracture(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("You twist your hand, and the world around your enemy fractures like shattered glass.")
        else:
            print("Time itself splinters around them, and they collapse between one moment and the next.")

class Dawnspike(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A spear of golden light forms above your hand and shoots toward your enemy.")
        else:
            print("The light pierces their chest, and their body falls beneath its radiant glow.")

class Thunderbrand(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("You raise your hand to the heavens, calling down a thunderous mark of divine wrath.")
        else:
            print("The heavens roar, and divine thunder strikes your enemy from above.")

class HolyRuin(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("Radiant energy gathers around you before surging forward in a blinding wave.")
        else:
            print("The light consumes them completely, leaving nothing but ash beneath your feet.")

class JudgementsChain(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("Bands of golden light lash around your enemy, dragging them before your judgement.")
        else:
            print("The chains tighten until divine judgement leaves them broken and still.")

class AegisOfDawn(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A radiant shield blossoms around you, its light burning away the darkness.")
        else:
            print("REMINDER: CHANGE")

class MartyrsLight(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("You call upon a sacred flame, turning pain itself into radiant power.")
        else:
            print("Their stolen vitality returns to you as their final breath fades.")

class WrathOfTheCrown(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("A blazing crown forms above your head as divine fury pours through your body.")
        else:
            print("The crown ignites with divine wrath, and your enemy is consumed beneath its judgement.")

class MercyOrDeath(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    def cast_spell(self):
        if enemy_health - self.hit_points > 0:
            print("You extend your hand, offering your enemy one final chance to stand before judgement is passed.")
        else:
            print("Your mercy ends where their defiance begins.")


#weapons subclasses (only greatsword attack lines (balanced attack) and (precise attack) are currently completed)
class Greatsword(WeaponsSpells):
    def __init__(self, hit_points):
        super().__init__(hit_points)

    #Effect: None
    def balanced_attack(self):
        balanced_attack_lines = ["You raise your greatsword and bring it crashing down.",
        "You step forward and sweep the greatsword in a powerful arc.",
        "You tighten your grip and slash toward your enemy."]
        balanced_fatality_lines = ["Your greatsword crashes down, and the enemy collapses.",
        "One final sweeping strike ends the battle.",
        "Your blade cuts through their defence, and they fall."]
        if enemy_health - self.hit_points > 0:
            random.shuffle(balanced_attack_lines)
            print(balanced_attack_lines[0])
        else:
            random.shuffle(balanced_fatality_lines)
            print(balanced_fatality_lines[0])

    #Effect: Easier to hit (+2 attack | -1 Damage)
    def precise_attack(self):
        precise_attack_lines = ["You wait for an opening before driving your greatsword forward.",
        "You shift your stance and deliver a precise upward cut.",
        "You sidestep the attack and strike directly at their opening."]
        precise_fatality_lines = ["You find the smallest opening and deliver the final blow.",
        "Your precise strike lands, and the enemy falls.",
        "You slip past their guard and end the fight with a single cut."]
        if enemy_health - self.hit_points > 0:
            random.shuffle(precise_attack_lines)
            print(precise_attack_lines[0])
        else:
            random.shuffle(precise_fatality_lines)
            print(precise_fatality_lines[0])

    
    #Effect: Harder to hit (-1 attack | +2 Damage)
    def heavy_attack(self):
        heavy_attack_lines = ["You raise the greatsword over your head and unleash a crushing cleave.",
        "You plant your feet and swing with all your strength.",
        "You roar as you bring the enormous blade down with tremendous force."]
        heavy_fatality_lines = ["The greatsword crashes down with devastating force.",
        "Your mighty cleave breaks through their defence and ends the fight.",
        "You unleash everything you have in one final crushing strike."]
        if enemy_health - self.hit_points > 0:
            random.shuffle(heavy_attack_lines)
            print(heavy_attack_lines[0])
        else:
            random.shuffle(heavy_fatality_lines)
            print(heavy_fatality_lines[0])
    
    #Effect: If miss, vulnerable (-2 attack | +3 damage)
    def reckless_attack(self):
        reckless_attack_lines = ["You abandon defence and throw your entire weight behind an overhead strike.",
        "You draw the greatsword back and charge forward with a reckless swing.",
        "You leave yourself exposed as you unleash a devastating two-handed blow."]
        reckless_fatality_lines = ["Your reckless strike crashes down with enough force to end the fight instantly.",
        "You commit everything to the attack, and the enemy falls beneath your blade.",
        "The enormous blow connects, bringing the battle to an abrupt end."]
        if enemy_health - self.hit_points > 0:
            random.shuffle(reckless_attack_lines)
            print(reckless_attack_lines[0])
        else:
            random.shuffle(reckless_fatality_lines)
            print(reckless_fatality_lines[0])
    
    #Effect: Weapon-specific (-3 attack | +4 damage)
    def signature_attack(self):
        signature_attack_lines = ["You spin the greatsword around you before striking again.",
        "You whirl through the battlefield and slash from the opposite side.",
        "You spin into a sweeping attack, carrying your momentum into the next strike."]
        signature_fatality_lines = ["You whirl through the enemy's guard and deliver the final cut.",
        "Your spinning blade tears through their defence, and they collapse.",
        "You complete the whirlwind with one final sweeping strike."]
        if enemy_health - self.hit_points > 0:
            random.shuffle(signature_attack_lines)
            print(signature_attack_lines[0])
        else:
            random.shuffle(signature_fatality_lines)
            print(signature_fatality_lines[0])
class Battleaxe(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Shortsword(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Mace(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass
    
class Morningstar(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Halberd(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Whip(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Crossbow(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass
    
class Shortbow(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Longbow(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass
    
class ThrowingKnives(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Handaxe(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass
    
class Dagger(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

class Quarterstaff(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass
    
class Hands(WeaponsSpells):
    def __init__(self, hit_points, rarity, enemy_hp):
        pass

#main dictionary keys are what weapon user has, sub-dictionary keys are the attack they choose, sub-dictionary values are a tuple containing: attack line(used for calling weapon class function), attack modifier, damage modifier
attack_lines = {"Greatsword": {"Balanced Slash": ("balanced_attack", 0, 0), "Precise Cut": ("precise_attack", 2, -1), "Heavy Cleave": ("heavy_attack", -1, 2), "Reckless Overhead": ("reckless_attack", -2, 3), "Whirlwind": ("signature_attack", -3, 4)},
"Battleaxe": {"Balanced Chop": ("balanced_attack", 0, 0), "Hooking Strike": ("precise_attack", 2, -1), "Cleaving Chop": ("heavy_attack", -1, 2), "Berserker Swing": ("reckless_attack", -2, 3), "Double Chop": ("signature_attack", -3, 4)},
"Shortsword": {"Quick Slash": ("balanced_attack", 0, 0), "Fencing Thrust": ("precise_attack", 2, -1), "Rapid Flurry": ("heavy_attack", -1, 2), "Lunging Strike": ("reckless_attack", -2, 3), "Riposte": ("signature_attack", -3, 4)},
"Mace": {"Crushing Swing": ("balanced_attack", 0, 0), "Shieldbreaker": ("precise_attack", 2, -1), "Mighty Hammer": ("heavy_attack", -1, 2), "Full-Force Smash": ("reckless_attack", -2, 3), "Concussive Blow": ("signature_attack", -3, 4)},
"Morningstar": {"Chain Swing": ("balanced_attack", 0, 0), "Snaring Strike": ("precise_attack", 2, -1), "Spinning Strike": ("heavy_attack", -1, 2), "Reckless Chain Swing": ("reckless_attack", -2, 3), "Chain Flurry": ("signature_attack", -3, 4)},
"Halberd": {"Polearm Strike": ("balanced_attack", 0, 0), "Hook and Thrust": ("precise_attack", 2, -1), "Swinging Cleave": ("heavy_attack", -1, 2), "Vaulting Strike": ("reckless_attack", -2, 3), "Low Sweep": ("signature_attack", -3, 4)},
"Whip": {"Lash": ("balanced_attack", 0, 0), "Entangling Lash": ("precise_attack", 2, -1), "Cracking Strike": ("heavy_attack", -1, 2), "Reckless Flurry": ("reckless_attack", -2, 3), "Disarming Crack": ("signature_attack", -3, 4)},
"Crossbow": {"Quick Shot": ("balanced_attack", 0, 0), "Careful Aim": ("precise_attack", 2, -1), "Piercing Bolt": ("heavy_attack", -1, 2), "Deadly Snipe": ("reckless_attack", -2, 3), "Quick Reload": ("signature_attack", -3, 4)},
"Shortbow": {"Snap Shot": ("balanced_attack", 0, 0), "Precise Shot": ("precise_attack", 2, -1), "Power Draw": ("heavy_attack", -1, 2), "Rapid Volley": ("reckless_attack", -2, 3), "Moving Shot": ("signature_attack", -3, 4)},
"Longbow": {"Battlefield Shot": ("balanced_attack", 0, 0), "Deadeye": ("precise_attack", 2, -1), "Heavy Draw": ("heavy_attack", -1, 2), "Devastating Shot": ("reckless_attack", -2, 3), "Hunter's Mark": ("signature_attack", -3, 4)},
"Throwing Knives": {"Single Throw": ("balanced_attack", 0, 0), "Precise Throw": ("precise_attack", 2, -1), "Heavy Throw": ("heavy_attack", -1, 2), "Fan of Blades": ("reckless_attack", -2, 3), "Trick Throw": ("signature_attack", -3, 4)},
"Handaxe": {"Axe Strike": ("balanced_attack", 0, 0), "Quick Axe": ("precise_attack", 2, -1), "Hurling Axe": ("heavy_attack", -1, 2), "Reckless Chop": ("reckless_attack", -2, 3), "Returning Strike": ("signature_attack", -3, 4)},
"Dagger": {"Quick Stab": ("balanced_attack", 0, 0), "Precise Thrust": ("precise_attack", 2, -1), "Flurry": ("heavy_attack", -1, 2), "Backstab": ("reckless_attack", -2, 3), "Feint and Strike": ("signature_attack", -3, 4)},
"Quarterstaff": {"Staff Strike": ("balanced_attack", 0, 0), "Measured Form": ("precise_attack", 2, -1), "Sweep and Thrust": ("signature_attack", -3, 4)},
"Hands": {"Strikes": ("balanced_attack", 0, 0), "Precise Technique": ("precise_attack", 2, -1), "Combination": ("heavy_attack", -1, 2), "Reckless Flurry": ("reckless_attack", -2, 3), "Counterstrike": ("signature_attack", -3, 4)}}

weapons = {"Melee Weapons": {"Greatsword": Greatsword, "Battleaxe": Battleaxe, "Shortsword": Shortsword, "Mace": Mace, "Morningstar": Morningstar, "Halberd": Halberd, "Whip": Whip},
"Ranged Weapons": {"Crossbow": Crossbow, "Shortbow": Shortbow, "Longbow": Longbow, "Throwing Knives": ThrowingKnives},
"Close Range Weapons": {"Handaxe": Handaxe, "Dagger": Dagger}, "Magic Weapon": {"Quarterstaff": Quarterstaff}, "Monk Weapon": {"Hands": Hands}}

proficiency = {"Melee Weapons": 0, "Ranged Weapons": 0, "Close Range Weapons": 0, "Magic Weapon": 0, "Monk Weapon": 0}

proficiency_spells = {"Arcane": 0, "Divine": 0}

spells = {"Arcane": {"Starter": {"Ember Lance": EmberLance, "Crystal Torrent": CrystalTorrent, "Blade of Light": BladeOfLight}, "Learnable": {"Starfall Sigil": StarfallSigil, "Graviton Snare": GravitonSnare, "Voidbind": Voidbind, "Arcane Leech": ArcaneLeech, "Reality Fracture": RealityFracture}},
"Divine": {"Starter": {"Dawnspike": Dawnspike, "Thunderbrand": Thunderbrand, "Holy Ruin": HolyRuin}, "Learnable": {"Judgements Chain": JudgementsChain, "Aegis of Dawn": AegisOfDawn, "Martyr's Light": MartyrsLight, "Wrath of the Crown": WrathOfTheCrown, "Mercy or Death": MercyOrDeath}}}

spell_descriptions = {"Ember Lance": " | Deals moderate fire damage to one enemy [Mana cost = 5]", "Crystal Torrent": " | Deals moderate ice damage to one enemy [Mana cost = 5]", "Blade Of Light": " | Deals moderate lightning damage to one enemy [Mana cost = 6]",
"Starfall Sigil": " | Deals heavy damage to one enemy [Mana cost = 12]", "Graviton Snare": " | Deals damage and gives the enemy -2 Attack next turn [Mana cost = 10]", "Voidbind": " | Deals damage and prevents the enemy from acting next turn [Mana cost = 14]", 
"Arcane Leech": " | Deals damage and restores a portion of your HP [Mana cost = 11]", "Reality Fracture": " | Deals damage and gives the enemy -2 AC next turn [Mana cost = 13]",
"Dawnspike": " | Deals moderate radiant damage to one enemy [Mana cost = 5]", "Thunderbrand": " | Deals moderate lightning damage to one enemy [Mana cost = 6]", "Holy Ruin": " | Deals moderate radiant damage to one enemy [Mana cost = 6]",
"Judgements Chain": " | Deals damage and gives the enemy -2 AC next turn [Mana cost = 10]", "Aegis of Dawn": " | Grants you +3 AC for your next turn [Mana cost = 8]", "Martyrs Light": " | Deals damage and restores a portion of your HP [Mana cost = 11]",
"Wrath Of The Crown": " | Deals very heavy damage but gives you -1 AC next turn [Mana cost = 13]", "Mercy Or Death": " | Deals increased damage when the enemy is below 25% HP [Mana cost = 12]"}

races = [{"race": "Human", "description": " | versatile [+1 to all stats]", "STR": 1, "DEX": 1, "CON": 1, "INT": 1, "WIS": 1, "CHA": 1}, 
{"race": "Elf", "description": " | agile and intelligent, but less tough [+2 DEX, + 1 INT, -1 CON]", "DEX": 2, "CON": -1, "INT": 1}, 
{"race": "Dwarf", "description": " | extremely tough, but slower [+2 CON +1 STR, +1 WIS, -1 DEX]", "STR": 1, "DEX": -1, "CON": 2, "WIS": 1}, 
{"race": "Halfling", "description": " | agile and perceptive, but physically weak [+2 DEX, +1 WIS, +1 CHA, -1 STR]}", "STR": -1, "DEX": 2, "WIS": 1, "CHA": 1},
{"race": "Orc", "description": " | strong, but less intelligent [+2 STR, +1 CON, -1 INT]", "STR": 2, "CON": 1, "INT": -1},
{"race": "Gnome", "description": " | intelligent and perceptive, but physically weak [+2 INT, +1 DEX, +1 WIS, -1 STR]", "STR": -1, "DEX": 1, "INT": 2, "WIS": 1}, 
{"race": "Tiefling", "description": " | charismatic and intelligent, but less tough [+2 CHA, +1 INT, -1 CON]", "CON": -1, "INT": 1, "CHA": 2}, 
{"race": "Lizardfolk", "description": " | tough and perceptive, but less charismatic [+2 CON, +1 STR, +1 WIS, -1 CHA]", "STR": 1, "CON": 2, "WIS": 1, "CHA": -1}]

classes = [{"class": "Fighter", "description": " | strong and tough, but socially awkward [+2 STR, +1 CON, -1 CHA]", "STR": 2, "CON": 1, "CHA": -1},
{"class": "Rogue", "description": " | agile and intelligent, but physically weak [+2 DEX, +1 INT, +1 CHA, -1 STR]", "STR": -1, "DEX": 2, "INT": 1, "CHA": 1},
{"class": "Wizard", "description": " | intelligent and wise, but physically weak [+2 INT, +1 DEX, +1 WIS, -1 STR]", "STR": -1, "DEX": 1, "INT": 2, "WIS": 1},
{"class": "Cleric", "description": " | wise and charismatic, but less agile [+2 WIS, +1 CON, +1 CHA, -1 DEX]", "DEX": -1, "CON": 1, "WIS": 2, "CHA": 1},
{"class": "Paladin", "description": " | strong and tough, but less intelligent [+2 STR, +1 CON, +1 CHA, -1 INT]", "STR": 2, "CON": 1, "INT": -1, "CHA": 1},
{"class": "Ranger", "description": " | agile and perceptive, but less charismatic [+2 DEX, 1 STR, +1 WIS, -1 CHA]", "STR": 1, "DEX": 2, "WIS": 1, "CHA": -1},
{"class": "Monk", "description": " | extremely agile and wise, but sacrifices some physical toughness and charisma [+2 DEX, +2 WIS, -1 CON, -1 CHA]", "DEX": 2, "CON": -1, "WIS": 2, "CHA": -1}]

magic_classes = {"Wizard", "Cleric", "Paladin"}

#ATTACK SYSTEM (currently made for later game when user faces enemies). I have only built the attack system for users, not the enemies yet.
#stat modifier decides what the stat the user uses for melee attacks and how high that stat is decides what number gets added to attack and damage rolls.
def weapon_attack_stat_modifier(current_stats: dict, att_strat: str):
    stat = current_stats[att_strat]
    if stat < 10:
        stat = 0
    elif 10 <= stat < 12:
        stat = 1
    elif 12 <= stat < 15:
        stat = 2
    elif 15 <= stat < 18:
        stat = 3
    elif 18 <= stat < 20:
        stat = 4
    else:
        stat = 5
    return stat

#does the same as above but for magic classes
def magic_attack_stat_modifier(current_stats: dict, att_strat: str):
    stat = current_stats[att_strat]
    if stat < 10:
        stat = 0
    elif 10 <= stat < 12:
        stat = 1
    elif 12 <= stat < 15:
        stat = 2
    elif 15 <= stat < 18:
        stat = 3
    elif 18 <= stat < 20:
        stat = 4
    else:
        stat = 5
    return stat

#attack rolls decide if you are able to hit and then damage the enemy depending on the enemies AC (armour class).
#the user will get a number between 1 and 20 + modifiers.
#if number + modifiers are >= AC they hit and move onto damage roll, if not, it will be the enemies turn to attack.
def attack_roll_weapon(stat_mod: int, prof: int, rarity: int, att_mod: int, enemy_ac: int, att_strat: str):
    roll = random.randint(1, 20)
    to_hit = roll + stat_mod + prof + rarity + att_mod
    if roll == 1:
        print(f"Roll = {roll} - CRITICAL MISS")
        return False
    elif roll == 20:
        print(f"Roll = {roll} - CRITICAL HIT")
        return True
    elif to_hit >= enemy_ac:
        print("", f"Roll = {roll}", sep="\n")
        print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} weapon proficiency, +{rarity} weapon rarity, and +{att_mod} attack modifier = {to_hit}")
        print(f"You needed: {enemy_ac}", "You hit!", sep="\n")
        return True
    else:
        print("", f"Roll = {roll}", sep="\n")
        print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} weapon proficiency, +{rarity} weapon rarity, and +{att_mod} attack modifier = {to_hit}")
        print(f"You needed: {enemy_ac}", "You missed!", "", sep="\n")
        return False

def attack_roll_spell(stat_mod: int, prof: int, mastery: int, att_mod: int, enemy_ac: int, att_strat: str):
    roll = random.randint(1, 20)
    to_hit = roll + stat_mod + prof + mastery + att_mod
    if roll == 1:
        print(f"Roll = {roll} - CRITICAL MISS")
        return False
    elif roll == 20:
        print(f"Roll = {roll} - CRITICAL HIT")
        return True
    elif to_hit >= enemy_ac:
        print("", f"Roll = {roll}", sep="\n")
        print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} magic type proficiency, +{mastery} magic mastery, and +{att_mod} attack modifier = {to_hit}")
        print(f"You needed: {enemy_ac}", "You hit!", sep="\n")
        return True
    else:
        print("", f"Roll = {roll}", sep="\n")
        print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} magic type proficiency, +{mastery} magic mastery, and +{att_mod} attack modifier = {to_hit}")
        print(f"You needed: {enemy_ac}", "You missed!", "", sep="\n")
        return False
    
#damage rolls determines how much health is taken off the enemy
def damage_roll_weapon(stat_mod: int, prof: int, rarity: int, dmg_mod: int, att_strat: str):
    roll = random.randint(1, 6)
    dmg = roll + stat_mod + prof + rarity + dmg_mod
    print("", "Fate rolls a 6-sided die to determine how much damage you inflict...", sep="\n")
    print("", f"Roll = {roll}", sep="\n")
    print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} weapon proficiency, +{rarity} weapon rarity, and +{dmg_mod} attack modifier = {dmg}", "", sep="\n")
    return dmg

def damage_roll_spell(stat_mod: int, prof: int, mastery: int, dmg_mod: int, att_strat: str):
    roll = random.randint(1, 6)
    dmg = roll + stat_mod + prof + mastery + dmg_mod
    print("", "Fate rolls a 6-sided die to determine how much damage you inflict...", sep="\n")
    print(f"Roll = {roll}")
    print(f"Your roll with +{stat_mod} {att_strat} modifier, +{prof} magic type proficiency, +{mastery} magic mastery, and +{dmg_mod} attack modifier = {dmg}", "", sep="\n")
    return dmg

def find_weapon_class(weapon: str, weapons_d: dict):
    for key in weapons_d:
        if weapon in weapons_d[key]:
            weapon_chosen_class = weapons_d[key][weapon]
            weapon_chosen_category = key
            return weapon_chosen_class, weapon_chosen_category

def choose_attack(attack_lines_d: dict, weapon: str, stat_mod: int, att_strat: str, prof: int, rarity: int, enemy_ac: int):
    print("", "How do you attack?", sep="\n")
    for choice in attack_lines_d[weapon].keys():
        print(f"- {choice}")
    print("", "Fate will roll a 20-sided die to determine your fate...", sep="\n")
    print(f"Your current bonus' are: +{stat_mod} {att_strat} modifier, +{prof} weapon proficiency, +{rarity} weapon rarity.")
    while True:
        choice = input("Type the attack you want to perform here: ").strip().title()
        if choice not in attack_lines_d[weapon].keys():
            print(f"Sorry you don't know how to {choice}. Try again and quick before they attack again!")
        else:
            return choice

mc_turn_choices = {"Attack", "Attempt to hide", "Heal"}
mc_inventory = {"Healing Potion": 0}

def fight_decision_input():
    print("", "Your turn. What do you do? ", sep="\n")
    for choice in mc_turn_choices:
        print(f"- {choice}")
    print()
    while True:
        choice = input("Type your strategy here: ").strip().capitalize()
        if choice not in mc_turn_choices:
            print(f"Sorry '{choice}' isn't a viable option right now. Try again.")
        else:
            return choice

def magic_or_weapon_input():
    print("", "What would you like to use:", sep="\n")
    print("- Magic", "- Weapon", f"Remaining mana = {mana}", "", sep="\n")
    while True:
        choice = input("Type your strategy here: ").strip().capitalize()
        if choice != "Magic" and choice != "Weapon":
            print(f"Sorry '{choice}' isn't an option. Try again.")
        else:
            return choice
            
def fight_weapon_main(enemy_hp):
    stat_modifier = weapon_attack_stat_modifier(stats, melee_attack_strategy)
    weapon_class, weapon_category = find_weapon_class(mc_weapon, weapons)
    proficiency_weapon = proficiency[weapon_category]
    attack_choice = choose_attack(attack_lines, mc_weapon, stat_modifier, melee_attack_strategy, proficiency_weapon, weapon_rarity, enemy_armour_class)
    method_name = attack_lines[mc_weapon][attack_choice][0]
    attack_modifier = attack_lines[mc_weapon][attack_choice][1]
    damage_modifier = attack_lines[mc_weapon][attack_choice][2]

    attack_roll_true_false = attack_roll_weapon(stat_modifier, proficiency_weapon, weapon_rarity, attack_modifier, enemy_armour_class, melee_attack_strategy)
    if attack_roll_true_false == True:
        damage_done = damage_roll_weapon(stat_modifier, proficiency_weapon, weapon_rarity, damage_modifier, melee_attack_strategy)
        enemy_hp -= damage_done
        weapon_object = weapon_class(damage_done)
        attack = getattr(weapon_object, method_name)
        attack()
        weapon_object.damage()
    return enemy_hp
    




def spell_choice_input(mc_learned_spells: set, spell_descrip: dict):
    print("", "What spell do you use: ", sep="\n")
    for spell in mc_learned_spells:
        print(f"- {spell}{spell_descrip[spell]}")
    print()
    while True:
        spell = input("Type your spell here: ").strip().title()
        if spell not in mc_learned_spells:
            print(f"Sorry '{spell}' is not a spell you know of. Try again.")
        else:
            return spell

def find_spell_class(spell: str, spells_d: dict):
    for magic_type in spells_d:
        for starter_learn in spells_d[magic_type]:
            if spell in spells_d[magic_type][starter_learn]:
                spell_chosen_class = spells_d[magic_type][starter_learn][spell]
                spell_chosen_category = magic_type
                spell_chosen_level = starter_learn
                return spell_chosen_class, spell_chosen_category, spell_chosen_level

def spell_attack_damage_modifier(spell_lvl: str, spell: str):
    dmg_modifier = 0
    if magic_mastery == 1:
        att_modifier = 1
    elif magic_mastery == 3:
        att_modifier = 2
    else:
        att_modifier = 0
    if spell_lvl == "Starter":
        dmg_modifier = 0
    else:
        dmg_modifier = 1
    if spell == "Starfall Sigil":
        dmg_modifier += 1
    if spell == "Wrath Of The Crown":
        dmg_modifier += 2
    return att_modifier, dmg_modifier

def fight_magic_main(enemy_hp: int):
    stat_modifier = magic_attack_stat_modifier(stats, magic_attack_strategy)
    spell_choice = spell_choice_input(mc_spells, spell_descriptions)
    spell_class, spell_category, spell_level = find_spell_class(spell_choice, spells)
    proficiency_spell = proficiency_spells[spell_category]
    attack_modifier, damage_modifier = spell_attack_damage_modifier(spell_level, spell_choice)

    attack_roll_true_false = attack_roll_spell(stat_modifier, proficiency_spell, magic_mastery, attack_modifier, enemy_armour_class, magic_attack_strategy)
    if attack_roll_true_false == True:
        damage_done = damage_roll_spell(stat_modifier, proficiency_spell, magic_mastery, damage_modifier, magic_attack_strategy)
        enemy_hp -= damage_done
        spell_object = spell_class(damage_done)
        attack = getattr(spell_object, "cast_spell")
        attack()
        spell_object.damage()
    return enemy_hp





def difficulty_input():
    print("Select your difficulty:")
    print("- Easy | base stats = STR: 9, DEX: 9, CON: 9, INT: 9, WIS: 9, CHA: 9", "- Normal | base stats = STR: 8, DEX: 8, CON: 8, INT: 8, WIS: 8, CHA: 8", "- Hard | base stats = STR: 7, DEX: 7, CON: 7, INT: 7, WIS: 7, CHA: 7", "", sep="\n")
    while True:
        difficulty_lvl = input("Type your difficulty here (or type 'Guide' for what stats mean): ").strip().replace(" ", "").capitalize()
        if difficulty_lvl == "Easy":
            return 9
        elif difficulty_lvl == "Normal":
            return 8
        elif difficulty_lvl == "Hard":
            return 7
        if difficulty_lvl == "Guide":
            print("", "Guide:", "STR = Strength - your character's physical force.", "DEX = Dexterity - your charater's speed, agility, and precision.", "CON = Constitution - how tough your character is.", sep="\n")
            print("INT = Intelligence - Your character's knowledge, logic, memory, and learned information.", "WIS = Wisdom - your character's awareness, preception, instinct, and judgement.", "CHA = Charisma - your character's influence and force of personality.", "", sep="\n")
        else:
            print(f"Sorry '{difficulty_lvl}' is not a valid difficulty. Please try again.")

    print("", "Guide:", "STR = Strength - your character's physical force.", "DEX = Dexterity - your charater's speed, agility, and precision.", "CON = Constitution - how tough your character is.", sep="\n")
    print("INT = Intelligence - Your character's knowledge, logic, memory, and learned information.", "WIS = Wisdom - your character's awareness, preception, instincy, and judgement.", "CHA = Charisma - your character's influence and force of personality.", "", sep="\n")

def stats_difficulty_calc(current_stats, difficulty):
    for stat in stats.keys():
        current_stats[stat] = difficulty
    return current_stats

def name_input():
    name = input("What is your name: ").strip()
    return name
    
def age_input(name):
    while True:
        age = input(f"How old are you {name}? ").strip()
        if age.isdigit():
            age = int(age)
            if age > 99:
                print("I don't believe you are Malrec the immortal, please pick a realistic age.")
            elif age < 16:
                print("Come back when your a bit older.")
            else:
                break
        else:
            print("Sorry that is not a valid number. Please try again.")
    return age
    
def race_input(current_stats):
    print("", "What race are you?", sep="\n")
    race_valid = False
    for option in races:
        print(f"- {option["race"]}{option["description"]}")
        print()
    print("Your current stats are baseline: ", end="")
    stat_string = ""
    for key, value in current_stats.items():
        stat_string += f"{key}: {value} | "
    print(stat_string[:-3], "", sep="\n")
    while True:
        race = input("Type your option here: ").strip().capitalize().replace(" ", "")
        for option in races:
            if race == option["race"]:
                for stat in option:
                    if stat in current_stats:
                        current_stats[stat] += option[stat]
                print("", "Your updated stats are: ", sep="\n")
                for key, value in current_stats.items():
                    print(f"{key}: {value}")
                race_valid = True
                break
        if race_valid == True:
            break
        print(f"Sorry '{race}' isn't a race i've ever heard of. Please try again.")
    return race, current_stats
    
def class_input(current_stats):
    print("", "What class are you?", sep="\n")
    class_valid = False
    for option in classes:
        print(f"- {option["class"]}{option["description"]}")
        print()
    print("Your current stats are: ", end="")
    stat_string = ""
    for key, value in current_stats.items():
        stat_string += f"{key}: {value} | "
    print(stat_string[:-3], "", sep="\n")
    while True:
        cllass = input("Type your option here: ").strip().capitalize().replace(" ", "")
        for option in classes:
            if cllass == option["class"]:
                for stat in option:
                    if stat in current_stats:
                        current_stats[stat] += option[stat]
                print("", "Your updated stats are: ", sep="\n")
                for key, value in current_stats.items():
                    print(f"{key}: {value}")
                class_valid = True
                break
        if class_valid == True:
            break
        print(f"Sorry '{cllass}' is not an option. Please try again.")
    return cllass, current_stats

def melee_attack_strat_decider(cllass):
    if cllass == "Fighter" or cllass == "Paladin":
        return "STR"
    else:
        return "DEX"

def magic_attack_strat_decider(cllass):
    if cllass == "Wizard":
        return "INT"
    elif cllass == "Cleric":
        return "WIS"
    elif cllass == "Paladin":
        return "CHA"
    
def weapon_input(cllass):
    if cllass != "Wizard" and cllass != "Cleric" and cllass != "Monk":
        print("", "What weapon do you choose?", sep="\n")
        if cllass == "Fighter" or cllass == "Paladin":
            proficiency["Melee Weapons"] = 2
            print(f"As a {cllass.lower()} you have [+2 proficiency] with melee weapons:")
            for option in weapons["Melee Weapons"].keys():
                print(f"- {option}")
            print("", "Proficiency = a bonus added to dice rolls when you character is skilled in a weapon.", "", sep="\n")
            while True:
                weapon = input("Type your option here: ").strip().capitalize().replace(" ", "")
                if weapon not in weapons["Melee Weapons"]:
                    print(f"Sorry '{weapon}' is not an option. Please try again.")
                else:
                    print("done")
                    break
        if cllass == "Rogue":
            proficiency["Close Range Weapons"] = 2
            proficiency["Ranged Weapons"] = 1
            print("As a rogue you have [+2 proficiency] with following weapons:")
            for option in weapons["Close Range Weapons"].keys():
                print(f"- {option}")
            print("And [+1 proficiency] with ranged weapons:")
            for option in weapons["Ranged Weapons"].keys():
                print(f"- {option}")
            print("Proficiency = a bonus added to dice rolls when you character is skilled in a weapon.", "", sep="\n")
            while True:
                weapon = input("Type your option here: ").strip().capitalize()
                if weapon not in weapons["Close Range Weapons"] and weapon not in weapons["Ranged Weapons"]:
                    print(f"Sorry '{weapon}' is not an option. Please try again.")
                else:
                    print("done")
                    break
        if cllass == "Ranger":
            proficiency["Ranged Weapons"] = 2
            print("As an ranger you have [+2 proficiency] with ranged weapons:")
            for option in weapons["Ranged Weapons"].keys():
                print(f"- {option}")
            print("", "Proficiency = a bonus added to dice rolls when you character is skilled in a weapon.", "", sep="\n")
            while True:
                weapon = input("Type your option here: ").strip().capitalize().replace(" ", "")
                if weapon not in weapons["Ranged Weapons"]:
                    print(f"Sorry '{weapon}' is not an option. Please try again.")
                else:
                    print("done")
                    break
    else:
        if cllass == "Wizard" or cllass == "Cleric":
            proficiency["Magic Weapon"] = 2
            print(f"As a {cllass.lower()} you are wield a quarterstaff as your weapon. [+2 proficiency with Quarterstaff]",
            "", "Proficiency = a bonus added to dice rolls when you character is skilled in a weapon.", "", sep="\n")
            weapon = "Quarterstaff"
        else:
            proficiency["Monk Weapon"] = 2
            print("As a monk you wield no weapon, but instead you harness the powers within to inflict powerful attacks with your hands. [+2 proficiency with no weapon]",
            "", "Proficiency = a bonus added to dice rolls when you character is skilled in a weapon.", "", sep="\n")
            weapon = "Hands"
    return weapon

def print_spells(cllass):
    if cllass == "Wizard":
        print("As a wizard you gain +2 proficiency when using ARCANE spells, and +1 proficiency when using DIVINE spells.", "The arcane spells you currently know are: ", sep="\n")
        for spell in spells["Arcane"]["Starter"]:
            print(f"- {spell}")
        print("", "You can find and learn additional spells throughout your adventure, and grow you magic mastery as you level up!", sep="\n")
        return {"Ember Lance", "Crystal Torrent", "Blade of Light"}
    else:
        print(f"As a {cllass.lower()} you gain +2 proficiency when using DIVINE spells, and +1 proficiency when using ARCANE spells.", "The divine spells you currently know are: ", sep="\n")
        for spell in spells["Divine"]["Starter"]:
            print(f"- {spell}")
        print("", "You can find and learn additional spells throughout your adventure, and grow you magic mastery as you level up!", sep="\n")
        return {"Dawnspike", "Thunderbrand", "Holy Ruin"}



def chap_1_drink_or_dont():
    while True:
        choice = input("What do you do? You're throat feels dry, but those hairs... OPTIONS: [drink] [don't]: ").strip().lower().replace("'", "")
        if choice == "drink":
            print("You cup your lips round the tankard and down the remaining mead. You catch the sweet note of honey alongside a couple a brisles that tickle your throat.")
            break
        elif choice == "dont":
            print("You push the tankard away, your sudden thirst has vanished.")
            break
        else:
            print(f"Sorry '{choice} isn't a valid option. Please try again.")









def chap_1_tavern_introduction():
    print("","CHAPTER ONE", sep="\n")
    print("", "Deadlines...", "Traffic...", "Ads...", "You feel something on your shoulder...it feels like tapping.", sep="\n")
    print("GUIDANCE: Press the [Enter] key each time the story stops to continue the conversation")
    enter = input("")
    print("You open your weary eyes to an old man leaning over your table, staring in anticipation.")
    print("Glad to be woken up from the nightmare, but slightly startled, you manage to say 's-sorry?", "You notice some strands from his great white mane was dunking your mead.", sep="\n")
    enter = input("")
    print("You don't mind me sitting with you do you?', his wispy voice whispered.")
    print("You look around the tavern. The place has suddenly picked up since you fell asleep after wandering in mid-afteroon, and every seat seems to be taken but the one opposite you.")
    print("'If you want', you reply in a raspy voice as you clear your throat.", "You go to grab your drink, but when you look at it there seems to be a couple grey strands floating on top.", "", sep="\n")
    chap_1_drink_or_dont()
    print("You notice the old man across from you seems very agitated, biting his nails and tapping his foot.")







def chapter_1_main():
    chap_1_tavern_introduction()


# welcome message:
print(f"{'*'*72}", "*       *      ***    *  *  ****  *   *  ****      *      *     *      *", "*      * *     *  *   * *   *     **  *  *        * *     *     *      *",
"*     *****    ***    **    ****  * * *  ****    *****    *     *      *", "*    *     *   *  *   * *   *     *  **  *      *     *   *     *      *", 
"*   *       *  *   *  *  *  ****  *   *  *     *       *  ****  ****   *", f"{'*'*72}", sep="\n")
print("Hello adventurer, welcome to Arkenfall", "", sep="\n")

#"mc" = "main character"
#difficulty sets how high the MC's starting stats are)
difficulty = difficulty_input()
stats = stats_difficulty_calc(stats, difficulty)

#name of user's character
mc_name = name_input()

#age
mc_age = age_input(mc_name)

#race
mc_race, stats = race_input(stats)

#class
mc_class, stats = class_input(stats)

#what stat is used in attack and damage rolls for melee attack scenarios 
melee_attack_strategy = melee_attack_strat_decider(mc_class)
#what stat is used in attack and damage rolls for magic attack scenarios
if mc_class in magic_classes:
    magic_attack_strategy = magic_attack_strat_decider(mc_class)

#what weapon MC will have
mc_weapon = weapon_input(mc_class)

#what spells MC has IF magic class
if mc_class in magic_classes:
    mc_spells = print_spells(mc_class)

chapter_1_main()




#will eventually be a function, only included in main frame for testing and will play out after chapter 1 even with no fight. You are not fighting the old man don't worry!
#I wanted to make the fight system early so I knew how it would work as it's the most complex system.
mc_fight_choice = fight_decision_input()
if mc_fight_choice == "Attack":
    if mc_class in magic_classes:      
        if mana >= 5:
            magic_or_weapon = magic_or_weapon_input()
            if magic_or_weapon == "Magic":
                enemy_health = fight_magic_main(enemy_health)
            else:
                enemy_health = fight_weapon_main(enemy_health)
        else:
            print(f"Your mana ({mana}) is too low for any spell, so you attack with your weapon.")
            enemy_health = fight_weapon_main(enemy_health)
    else:
        enemy_health = fight_weapon_main(enemy_health)
    


#stats, lvl = lvl_up(stats, lvl)