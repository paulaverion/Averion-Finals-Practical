from .Users import *
class Score:
	def __init__(self, filename='scores.txt'):
		self.filename = filename
		self.scores = {}
		self.wins = {}

	def load_score(self):
		try:
			with open(self.filename, 'r') as f:
				for line in f:
					username, score = line.strip().split(',')
					self.scores[username] = int(score)
		except FileNotFoundError:
			print("Score file not found.")
		except Exception as e:
			print(f"Error loading scores: {e}")

	def save_score(self):
		with open(self.filename, 'w') as f:
			for username, score in self.scores.items():
				f.write(f"{username},{score}\n")

	def add_score(self, username, score):
		if username in self.scores:
			self.scores[username] += score
		else:
			self.scores[username] = score
		self.save_scores()

	def add_wins(self, username, wins):
		if username in self.wins:
			self.wins[username] += wins
		else:
			self.wins[username] = wins
		self.save_scores()
		
	def get_score(self, username):
		return self.scores.get(username, 0)
	
	def get_wins(self, username):
		return self.wins.get(username, 0)
	
	def ScorePrint(self):
		with open('rankings.txt', 'r') as f:
			print(f"{self.accounts['username']}: {self.accounts['points']} points.")

	def PrintHighScore(self):
		scores = self.accounts
		with open('rankings.txt', 'r') as f:
			SortedScore = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
			count = 1
			for key, value in SortedScore.items():
				print(f"{count}. {key}: {value} points\n")
				count += 1