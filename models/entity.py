"""
Module containing the Entity class.
"""
from constants import DescriptionType


class Entity:
    """
    This is the prototype class from which every game object will be
    derrived.
    Properties:
        name: An identifying string for the entity.
        short_description: A breif description string.
        full_description: A detailed description string.
        meta: A dictionary of optional data used by the game logic.
    """

    def __init__(self,
                 name,
                 location,
                 short_description,
                 full_description=None
                 meta={}):
        self._name = name
        self.location = location
        self._short_description = short_description
        self._full_description = full_description
        self.meta = meta

    @property
    def short_description(self):
        """
        Return the short description of this entity.
        """
        return self._short_description

    @property
    def long_description(self):
        """
        Return the long description of this entity.
        """
        return self.long_description

    def describe(self, caller, description_type):
        """
        Return the long description if specified and available; otherwise,
        return the short description.
        """
        if (self.full_description == None
                or description_type == DescriptionType.full):
            return self.short_description
        else:
            return self.full_description
