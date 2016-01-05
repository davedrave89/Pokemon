
class GameModel(object):
	"""GameModel class contains common methods and attributes that other classes share"""
	def __init__(self, name):
		self.name = name
	def GetName(self):
		return self.name

class User(GameModel):
	"""User class represents a game participant"""
	def __init__(self, name, score=0, health=0):
		self.name = name
		self.score = score
        #health attribute will store the users health
		self.health = health

	def Score(self):
		return self.score

	def Health(self):
		return self.health

class Computer(User):
	"""Computer class will be the opponent to the User"""
	def __init__(self, name, score, health):
		pass

class Player(User):
	"""Player class will represent and be controlled by the user"""
	def __init__(self, name, score, health):
		pass