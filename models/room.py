"""
Module containing the Room class
"""
from collections import namedtuple

from entity import Entity


"""
Exit is a namedtuple which describes a unidirectional connection between rooms.
Properties:
    direction: Short name string
    destination: Room refrence
"""
Exit = namedtuple("Exit", ['direction', 'destination'])


class Room(Entity):
    """
    Class representing locations in the game world.
    Properties:
        exits: List of Exit namedtuples
    """

    def __init__(self,
                 name,
                 short_description,
                 full_description=None,
                 exits=[]
                 meta={}):
        super(name, location, short_description, full_description, meta)
        self._exits = exits

    @property
    def exits(self):
        """
        Return the list of exits.
        """
        return self._exits

    @property
    def short_description(self):
        """
        Return the short description of this room.
        Exits are appended to the end.
        """

        description = self._short_description + "\n\nThe exits are "
        for exit in exits:
            description += "{}, ".formatexit.direction)
        return description

    @property
    def full_description(self):
        """
        Return the short description of this room.
        Exits are appended to the end.
        """

        description = self._full_description + "\n\nThe exits are "
        for exit in exits:
            description += "{}, ".format(exit.direction)
        return description
