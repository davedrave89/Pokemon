
class GameModel(object):
	"""GameModel class contains common methods and attributes that other classes share"""
	def __init__(self, name):
		self.name = name
	def GetName(self):
		return self.name

class User(GameModel):
	"""User class represents a game participant"""
	def __init__(self, name, score=0, healing=0):
		self.name = name
		self.score = score
		self.healing = healing

	def Score(self):
		return score
	def Healing(self):
		return healing

class Computer(User):
	"""Computer class will be the opponent to the User"""
	def __init__(self, name, score, healing):
		pass

class Player(User):
	"""Player class will represent and be controlled by the user"""
	def __init__(self, name, score, healing):
		pass