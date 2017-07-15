"""
Module containing the creature class.
"""
from entity import Entity


class Creture(Entity):
    """
    Parent class of all MOBs
    Properties:
        health_points: How much health the creature has
        ability_points: How many points the creature has to cast magic or
                        use abilities
        strength: The creature's ability to inflict physical damage
        defense: The creature's ability to resist physical damage
        agility: The creature's speed
        dexterity: The creature's ability to handle weapons and tools
        inteligence: The creature's mental capacity
    """

    def __init__(self
                 name,
                 health_points,
                 ability_points,
                 strength,
                 defense,
                 agility,
                 dexterity,
                 inteligence,
                 short_description,
                 full_description=None
                 meta={}):
        super(name, short_description, full_description, meta)
        self.health_points = health_points
        self._health_points_max = health_points
        self.ability_points = ability_points
        self._ability_points_max = ability_points
        self._strength = strength
        self._defense = defense
        self._agility = agility
        self._dexterity = dexterity
        self._inteligence = inteligence
        self.status_effects{}

        @property
        def ability_points_max(self):
            return self._ability_points_max

        @property
        def agility(self):
            return self._agility

        @property
        def defense(self):
            return self._defense

        @property
        def dexterity(self):
            return self._dexterity

        @property
        def health_ponts_max(self):
            return self._health_points_max

        @property
        def inteligence(self):
            return self._inteligence

        @property
        def strength(self):
            return self._strength

        def attack(self, target, method):
            """
            Attack another creature.
            Inputs:
                target: The creature to attack
                method: What method to attack with (callback)
            """
            return target.defend(self, method(), {})

        def defend(self, caller, damage, effects):
            """
            Method called by an attacker.
            Inputs:
                caller: The attacking creature
                damage: The ammount of damage the attacker is dealing
                effects: A dictionary with the structure
                         {name:{severity, callback, chance}...}
            Return:
                Tuple(damage dealt, dictionary of effects and severity)
            """
            damage_dealt = damage - defense
            if damage_dealt > 0:
                self.health_points -= damage_dealt
                # TODO: Status effects
                return (damage_dealt, {})
            return (0, {})

        def move(self, destination):
            """
            Move this creature to another room.
            """
            self.location = destination

        def speak(self):
            """
            Say something which will be heard by any other creatures in the
            same room.
            """
            # TODO
            return

        def die(self):
            """
            Kill this creature.
            """
            # TODO
            return

        def process_effects(self):
            """
            Deal damage from status effects and heal them.
            """
            for effect in self.status_effects:
                # TODO: Call effect['callback']
                if effect['severity'] > 1:
                    effect['severity'] -= 1
                else:
                    # TODO: Remove effect
