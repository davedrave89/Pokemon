from assets import GameModel

class Pokemon(GameModel):
    """Pokemon class represents pokemon which will be used by the Player/Computer to do battle"""

    def __init__(self, name, health, moves):
        self.health = health
        self.moves = moves
        GameModel.__init__(self, name)

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self,health):
        self.__health = health

    @property
    def moves(self):
        return self.__moves

    @moves.setter
    def moves(self,moves):
        self.__moves = moves

class Move():
    """Moves class represents the move, range damage etc that can be performed by a pokemon or player"""

    def __init__(self, name, damage, range, hitpoint):
        self.name = name
        self.damage = damage
        self.range = range
        self.hit_point = hitpoint

    @property
    def name(self):
		return self.__name

    @property
    def Damage(self):
		return self.Damage

    #range specifies the lowest and highest amount of damage that a move can deal.
    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, range):
        self.__range = range

    @property
    def Hitpoint(self):
        return self.Hitpoint

class Message():
    def Notifications():
        pass

    def Health():
        pass