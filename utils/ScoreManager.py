from Users import *
class Score:
	def __init__(self, users):
		self.users = users

	def add_score(self, username, score):
		self.users.add_score(username, score)