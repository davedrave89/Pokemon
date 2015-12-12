from assets import GameModel

class Pokemon(GameModel):
	"""Pokemon class represents pokemon which will be used by the Player/Computer to do battle"""

	def __init__(self, name, Health, Move):
		GameModel.__init__(self, name)
		self.Health = Health
		self.Moves = Move

	def Health(self):
		return self.Health
	def Moves(self):
		return self.Move

class Move():
	"""Moves class represents the move, range damage etc that can be performed by a pokemon or player"""

	def __init__(self, Name, Damage, Range, Hitpoint):
		self.Name = Name
		self.Damage = Damage
		self.Range = Range
		self.Hitpoint = Hitpoint

	def Name(self):
		return self.Name

	def Damage(self):
		return self.Damage

	def Range(self):
		return self.Range

	def Hitpoint(self):
		return self.Hitpoint

class Message():
	def Notifications():
		pass

	def Health():
		pass