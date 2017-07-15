"""
Module containing the Exit class.
"""
from entity import Entity


class Exit(Entity):
    """
    Exit represents a unidirectional connection between rooms.
    Properties:
        direction: Short name string
        destination: Room refrence
    """

    def __init__(self,
                 name,
                 destination,
                 short_description,
                 full_description=None,
                 meta={}):
        super(name, location, short_description, full_description, meta)
        self.destination = destination
