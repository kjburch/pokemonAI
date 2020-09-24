# It kinda works
# good luck

import math
import random
from enum import Enum

# Global Variables
pokemonGeneration = 1


# Enum used to represent pokemon types
class PokemonType(Enum):
    Normal = 0
    Fire = 1
    Water = 2
    Electric = 3
    Grass = 4
    Ice = 5
    Fighting = 6
    Poison = 7
    Ground = 8
    Flying = 9
    Psychic = 10
    Bug = 11
    Rock = 12
    Ghost = 13
    Dragon = 14
    Error = 15


# Stat modifier map
# part of the attack/defense statistic multiplier system
statModifier = {0: 1, 1: 1.5, 2: 2, 3: 2.5, 4: 3, 5: 3.5, 6: 4, -1: 0.66, -2: 0.5, -3: 0.4, -4: 0.33, -5: 0.28,
                -6: 0.25}

# Pokemon type Effectiveness dictionary for Gen1
# Currently only setup to work through gen 1
# other generations not implemented
# Key is attacking pokemon, Value is defending pokemon
typeEffectivenessGen1 = {
    PokemonType.Normal: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                         PokemonType.Grass: 1, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                         PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 1,
                         PokemonType.Rock: 0.5, PokemonType.Ghost: 0, PokemonType.Dragon: 1},

    PokemonType.Fire: {PokemonType.Normal: 1, PokemonType.Fire: 0.5, PokemonType.Water: 0.5, PokemonType.Electric: 1,
                       PokemonType.Grass: 2, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                       PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 2,
                       PokemonType.Rock: 0.5, PokemonType.Ghost: 1, PokemonType.Dragon: 0.5},

    PokemonType.Water: {PokemonType.Normal: 1, PokemonType.Fire: 2, PokemonType.Water: 0.5, PokemonType.Electric: 1,
                        PokemonType.Grass: 0.5, PokemonType.Ice: 2, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                        PokemonType.Ground: 2, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 1,
                        PokemonType.Rock: 2, PokemonType.Ghost: 1, PokemonType.Dragon: 0.5},

    PokemonType.Electric: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 2, PokemonType.Electric: 0.5,
                           PokemonType.Grass: 0.5, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                           PokemonType.Ground: 0, PokemonType.Flying: 2, PokemonType.Psychic: 1, PokemonType.Bug: 1,
                           PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 0.5},

    PokemonType.Grass: {PokemonType.Normal: 1, PokemonType.Fire: 0.5, PokemonType.Water: 2, PokemonType.Electric: 1,
                        PokemonType.Grass: 0.5, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 0.5,
                        PokemonType.Ground: 2, PokemonType.Flying: 0.5, PokemonType.Psychic: 1, PokemonType.Bug: 0.5,
                        PokemonType.Rock: 2, PokemonType.Ghost: 1, PokemonType.Dragon: 0.5},

    PokemonType.Ice: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 0.5, PokemonType.Electric: 1,
                      PokemonType.Grass: 2, PokemonType.Ice: 0.5, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                      PokemonType.Ground: 2, PokemonType.Flying: 2, PokemonType.Psychic: 1, PokemonType.Bug: 1,
                      PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 2},

    PokemonType.Fighting: {PokemonType.Normal: 2, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                           PokemonType.Grass: 1, PokemonType.Ice: 2, PokemonType.Fighting: 1, PokemonType.Poison: 0.5,
                           PokemonType.Ground: 1, PokemonType.Flying: 0.5, PokemonType.Psychic: 0.5,
                           PokemonType.Bug: 0.5,
                           PokemonType.Rock: 2, PokemonType.Ghost: 0, PokemonType.Dragon: 1},

    PokemonType.Poison: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                         PokemonType.Grass: 2, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 0.5,
                         PokemonType.Ground: 0.5, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 2,
                         PokemonType.Rock: 0.5, PokemonType.Ghost: 0.5, PokemonType.Dragon: 1},

    PokemonType.Ground: {PokemonType.Normal: 1, PokemonType.Fire: 2, PokemonType.Water: 1, PokemonType.Electric: 2,
                         PokemonType.Grass: 0.5, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 2,
                         PokemonType.Ground: 2, PokemonType.Flying: 0, PokemonType.Psychic: 1, PokemonType.Bug: 0.5,
                         PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 1},

    PokemonType.Flying: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 0.5,
                         PokemonType.Grass: 2, PokemonType.Ice: 1, PokemonType.Fighting: 2, PokemonType.Poison: 1,
                         PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 2,
                         PokemonType.Rock: 0.5, PokemonType.Ghost: 1, PokemonType.Dragon: 1},

    PokemonType.Psychic: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                          PokemonType.Grass: 1, PokemonType.Ice: 1, PokemonType.Fighting: 2, PokemonType.Poison: 2,
                          PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 0.5, PokemonType.Bug: 1,
                          PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 1},

    PokemonType.Bug: {PokemonType.Normal: 1, PokemonType.Fire: 0.5, PokemonType.Water: 1, PokemonType.Electric: 1,
                      PokemonType.Grass: 2, PokemonType.Ice: 1, PokemonType.Fighting: 0.5, PokemonType.Poison: 2,
                      PokemonType.Ground: 1, PokemonType.Flying: 0.5, PokemonType.Psychic: 2, PokemonType.Bug: 1,
                      PokemonType.Rock: 1, PokemonType.Ghost: 0.5, PokemonType.Dragon: 1},

    PokemonType.Rock: {PokemonType.Normal: 1, PokemonType.Fire: 2, PokemonType.Water: 1, PokemonType.Electric: 1,
                       PokemonType.Grass: 1, PokemonType.Ice: 2, PokemonType.Fighting: 0.5, PokemonType.Poison: 1,
                       PokemonType.Ground: 0.5, PokemonType.Flying: 2, PokemonType.Psychic: 1, PokemonType.Bug: 2,
                       PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 1},

    PokemonType.Ghost: {PokemonType.Normal: 0, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                        PokemonType.Grass: 1, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                        PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 0, PokemonType.Bug: 1,
                        PokemonType.Rock: 1, PokemonType.Ghost: 2, PokemonType.Dragon: 1},

    PokemonType.Dragon: {PokemonType.Normal: 1, PokemonType.Fire: 1, PokemonType.Water: 1, PokemonType.Electric: 1,
                         PokemonType.Grass: 1, PokemonType.Ice: 1, PokemonType.Fighting: 1, PokemonType.Poison: 1,
                         PokemonType.Ground: 1, PokemonType.Flying: 1, PokemonType.Psychic: 1, PokemonType.Bug: 1,
                         PokemonType.Rock: 1, PokemonType.Ghost: 1, PokemonType.Dragon: 2}
}


# Enum used to represent the category of a pokemon's move
class MoveCategory(Enum):
    Physical = 0
    Special = 1
    Status = 2
    Error = 3


# Enum used to represent the current weather
class Weather(Enum):
    none = 0
    Rain = 1
    Sandstorm = 2
    Hail = 3
    Sun = 4
    Fog = 5


# Enum used to represent the type of pokemon battle
class BattleType(Enum):
    singles = 0
    doubles = 1
    triples = 2


# Badges for Gen 2 only


# Enum used to represent the status effect on a pokemon
class PokemonStatusEffect(Enum):
    Error = 0
    Freeze = 1
    Paralysis = 2
    Poison = 3
    BadlyPoisoned = 4
    Sleep = 5
    Bound = 6
    CannotEscape = 7
    Confusion = 8
    Curse = 9
    Embargo = 10
    HealBlock = 11
    Identified = 12
    Infatuation = 13
    Leeched = 14
    Nightmare = 15
    PerishSong = 16
    Taunt = 17
    Telekinesis = 18
    Torment = 19
    AquaRing = 20
    Bracing = 21
    ChargingTurn = 22
    CenterOfAttention = 23
    DefenseCurl = 24
    Rooting = 25
    MagneticLevitation = 26
    Minimize = 27
    Protection = 28
    Recharging = 29
    SemiInvulnerable = 30
    Substitute = 31
    TakingAim = 32
    Withdrawing = 33
    Burn = 34


# Pokemon move class, meant to represent 1 pokemon move and all its effects / attributes
class PokemonMove:
    name = ""
    type = PokemonType.Error
    category = MoveCategory.Error
    pp = 0
    power = 0
    accuracy = 0
    # plus/ minus attack, defense, special att, special def,  speed
    # for a move that causes changes in the poke stat
    status = [0, 0, 0, 0, 0]
    effect = PokemonStatusEffect.Error

    # allows the creation of a pokemon move object
    def __init__(self, Name, Type, Category, PP, Power, Accuracy, Status, Effect) -> object:
        self.name = Name
        self.type = Type
        self.category = Category
        self.pp = PP
        self.power = Power
        self.accuracy = Accuracy
        self.status = Status
        self.effect = Effect


# Pokemon Class, meant to represent a single pokemon, not a single pokemon species
class Pokemon:
    name = ""
    hp = 0
    # ev order: hp, attack, defense, sp attack, sp defense, speed
    ev = []
    ability = ""
    moves = []
    type = []
    level = 0
    # plus/ minus attack, defense, special att, special def, speed
    statusModifier = [0, 0, 0, 0, 0]
    statusEffects = []

    # allows the creation of a pokemon object
    def __init__(self, Name, HP, EV, Ability, Moves, Type, Level) -> object:
        self.name = Name
        self.hp = HP
        self.ev = EV
        self.ability = Ability
        self.moves = Moves
        self.type = Type
        self.level = Level
        self.statusModifier = [0, 0, 0, 0, 0]
        self.statusEffects = []

    # Prints the Pokemon and all of its Attributes
    def display(self):
        print("Name:", self.name, "\nHP:", self.hp, "\nEV:", self.ev, "\nAbility:", self.ability, "\nMoves:",
              self.moves, "\nType:", self.type, "\nLevel:", self.level, "Status Effects:", self.statusEffects)


# Calculates and returns Attack Damage
def calcDamage(attackingPokemon, defendingPokemon, move, targets, weather, badge, other):
    # Level modifier calc
    if pokemonGeneration != 1:
        l = 1
    # gen 1 crit based on pokemon speed
    # does not currently take into account special cases
    else:
        P = attackingPokemon.ev[5] / 512
        rTemp = random.randint(0, 100)
        if rTemp / 100 < P:
            l = attackingPokemon.level * 2
        else:
            l = attackingPokemon.level

    # Doubles or Triples battle target modifier
    if targets > 1:
        t = 0.75
    else:
        t = 1

    # Weather Calculation Modifiers
    if weather == Weather.Sun:
        if move.type == PokemonType.Fire:
            w = 1.5
        if move.type == PokemonType.Water:
            w = 0.5
    elif weather == Weather.Rain:
        if move.type == PokemonType.Fire:
            w = 0.5
        if move.type == PokemonType.Water:
            w = 1.5
    else:
        w = 1

    # Badge Multiplier, Gen 2 only
    # Not yet implemented
    if pokemonGeneration != 2:
        b = 1
    else:
        # will be implemented at some point
        b = 1

    # Critical Hit Chance
    # Refers to crit hit table
    # not fully implemented
    if pokemonGeneration != 1:
        r2 = random.randint(0, 1000)
        # After gen 5
        if pokemonGeneration > 5:
            if r2 / 1000 < 6.25:
                c = 1.5
            else:
                c = 1
        # Gen 2 through 5
        else:
            if r2 / 1000 < 6.25:
                c = 2
            else:
                c = 1
    # Does not exist in Gen 1
    else:
        c = 1

    # Random Num Generator
    r = random.randint(85, 100) / 100

    # Other Calculation
    # Not yet implemented
    o = 1

    # Stab calculation
    if move.type in attackingPokemon.type:
        s = 1.5

    # Type Effectiveness
    ty = 1
    for i in defendingPokemon.type:
        ty = ty * typeEffectivenessGen1[move.type][i]

    # Burn modifier Calculation
    if PokemonStatusEffect.Burn in attackingPokemon.statusEffects and move.category == MoveCategory.Physical:
        bu = 0.5
    else:
        bu = 1

    # Modifier Calculation
    modifier = t * w * b * c * r * s * ty * bu * o

    # Attack and Defense calc variable
    # attack or defense stat multiplied by the stat modifier
    # If the attack is physical
    if move.category == MoveCategory.Physical:
        A = attackingPokemon.ev[1] * statModifier[attackingPokemon.statusModifier[0]]
        D = defendingPokemon.ev[2] * statModifier[defendingPokemon.statusModifier[1]]
    # If the attack is special
    else:
        # Generation 1 combines special attack and special defense into 1 stat called special
        if pokemonGeneration == 1:
            A = attackingPokemon.ev[3] * statModifier[attackingPokemon.statusModifier[2]]
            D = defendingPokemon.ev[3] * statModifier[defendingPokemon.statusModifier[2]]
        else:
            A = attackingPokemon.ev[3] * statModifier[attackingPokemon.statusModifier[2]]
            D = defendingPokemon.ev[4] * statModifier[defendingPokemon.statusModifier[3]]

    # Calculates the base dam without modifiers
    base = math.floor(math.floor(math.floor(2 * l / 5+2) * move.power * A / D) / 50)+2

    # actually calculates the damage
    damage = math.floor(base * modifier)

    textOut = "Printing Damage Calculation Variables:\n\nTargets: "+str(t)+", Weather: "+str(w)+", Badge: "+str(
        b)+", Critical: "+str(c)+", Random: "+str(r)+", Stab: "+str(s)+", Type: "+str(ty)+", Burn: "+str(
        bu)+", Other: "+str(o)+"\nAttacking Pokemon Level: "+str(l)+", Move Power: "+str(
        move.power)+", Attacking Pokemon Attack Stat: "+str(A)+", Defending Pokemon Defense Stat: "+str(
        D)+"\n\nBase Damage: "+str(base)+"\nDamage Modifier: "+str(modifier)+"\n\nActual damage: "+str(damage)

    return damage, textOut


# Creates the current battlefield
class PokemonBattle:
    activePlayerPokemon = []
    playerPokemonTeam = []
    activeOpponentPokemon = []
    opponentPokemonTeam = []
    battleWeather = Weather.none
    battleFormat = BattleType.singles

    # creates the pokemon battle object
    def __init__(self, ppt, opt, w, bt) -> object:
        self.playerPokemonTeam = ppt
        self.opponentPokemonTeam = opt
        self.battleWeather = w
        self.battleFormat = bt

    # allows switching pokemon, oldPoke is always 0 unless in a team battle
    def swapPokemon(self, oldPoke, newPoke):
        if oldPoke != newPoke:
            if self.battleFormat == BattleType.singles:
                self.activePlayerPokemon[0] = self.playerPokemonTeam[newPoke]
            else:
                self.activePlayerPokemon[oldPoke] = self.playerPokemonTeam[newPoke]

    # Returns all possible outcomes of an attack and the percent chance of it happening
    # active player poke is always 0 unless in a team battle
    def attack(self, playerPoke, move):
        if self.battleFormat == BattleType.singles:
            if self.activePlayerPokemon[0].moves[move] == MoveCategory.Status:
                # not yet implemented
                print("Unimplemented")
            else:
                # calculates the accuracy based on move accuracy and opponent evade
                accuracy = self.activePlayerPokemon[0].moves[move].accuracy

                calcDamage(self.activePlayerPokemon, self.activeOpponentPokemon, self.activePlayerPokemon.moves[move],
                           1, self.battleWeather, None, 1)

        # Doubles and Triples battles
        else:
            if self.activePlayerPokemon[playerPoke].moves[move] == MoveCategory.Status:
                # not yet implemented
                print("Unimplemented")
            else:
                # not yet implemented
                print("Unimplemented")

        return accuracy


# Main------------------------------------------------------------------------------------------------------------------

thundershock = PokemonMove("thundershock", PokemonType.Electric, MoveCategory.Special, 30, 40, 100, [],
                           PokemonStatusEffect.Error)

# ev order: hp, attack, defense, sp attack, sp defense, speed
# EVs are not currently set correctly however the damage calculator does work as intended for gen 1
pikachu = Pokemon("pikachu", 35, [35, 55, 30, 10, 10, 7], "static", [thundershock], [PokemonType.Electric], 1)

squirtle = Pokemon("squirtle", 35, [44, 48, 65, 6, 6, 43], "torrent", [], [PokemonType.Water], 1)

max = -100
min = 100

dam = []

seven = 0
eight = 0
nine = 0
six = 0

d = calcDamage(pikachu, squirtle, thundershock, 1, Weather.none, 0, 0)

print(d[1])
