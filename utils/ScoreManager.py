from .Users import *
class Score:
	def __init__(self, username, points, wins, game_ID):
		self.username = username
		self.score = points
		self.wins = wins
		self.game_ID = game_ID