class GameModel(object):
	def __init__(self, name):
		self.name = name
	def GetName(self):
		return self.name

class User(GameModel):
	def __init__(self, name, score=0, healing=0):
		self.name = name
		self.score = score
		self.healing = healing

	def Score(self):
		return score
	def Healing(self):
		return healing

class Computer(User):
	def __init__(self, name, score, healing):
		pass

class Player(User):
	def __init__(self, name, score, healing):
		pass