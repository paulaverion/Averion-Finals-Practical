from .Users import *
class Score:
	def __init__(self, users):
		self.users = users

	def add_score(self, username, score):
		self.users.add_score(username, score)

	def add_wins(self, username, wins):
		self.users.add_wins(username, wins)