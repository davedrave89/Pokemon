
class GameModel(object):
    """GameModel class contains common methods and attributes that other classes share"""
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

class User(GameModel):
    """User class represents a game participant"""
    def __init__(self, name, score=0, health=0):
        self.name = name
        self.score = score
        #health attribute will store the users health
        self.health = health

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def health(self):
		return self.__health

    @health.setter
    def health(self, health):
        self.__health = health

class Computer(User):
	"""Computer class will be the opponent to the User"""
	def __init__(self, name, score, health):
		pass

class Player(User):
	"""Player class will represent and be controlled by the user"""
	def __init__(self, name, score, health, pokemon):
		self.name = name
		self.score = score
		self.health = health
		# Allows for instatiation of Pokemon object
		self.pokemon = pokemon
		
