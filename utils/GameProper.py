import random
from .ScoreManager import *
scores = []

class DiceGame:
	points = 0
	wins = 0
	def load_scores(self):
		pass

	def save_scores(self):
		with open('data.txt', 'w') as f:
			for i in range(len(scores)):
				f.write(f"{scores[i].username}, {scores[i].score}, {scores[i].wins}, {scores[i].game_ID}\n")

	def play_game(self, username):
		while True:
			if self.rolls(username) == True:
				choice = int(input("Do you want to continue to the next stage? (1 for Yes, 0 for No): "))
				if choice == 1:
					continue
				elif choice == 0:
					self.save_scores()
					self.points = 0
					self.win = 0
					return
				else:
					print("Invalid choice. Please enter 1 or 0.")
			else:
				return

	def show_top_scores(self):
		pass

	def menu(self, username):
		self.load_scores()
		while True:	
			print(f"Welcome, {username}!")
			print("""
		Menu: 
			1. Start Game
			2. Show Top Scores
			3. Log Out
				""")
			choice = input("Enter your choice, or leave blank to cancel: ")
			if choice == '1':
				print(f"Starting game as {username}...\n")
				self.play_game(username)
			elif choice == '2':
				self.show_top_scores()
			elif choice == '3':
				return
			elif choice == "":
				continue
			else:
				print("Invalid choice. Please enter 1, 2, or 3.")

	def rolls(self, username):
			global points
			global wins
			RoundWin = 0
			RoundLose = 0
			while RoundWin < 2 and RoundLose < 2:
				RollUser = random.randint(1, 6)
				RollCPU = random.randint(1, 6)
				print(f"{username} rolled: {RollUser}\n")
				print(f"CPU rolled: {RollCPU}\n")
				if RollUser > RollCPU:
					print(f"You win this round! {username}")
					RoundWin += 1
					self.points += 1
				elif RollCPU > RollUser:
					print(f"CPU wins this round!")
					RoundLose += 1
				elif RollCPU == RollUser:
					print("It's a tie!")
			else:
				if RoundWin == 2:
						print(f"You won this stage {username}!\n")
						self.points += 3
						self.wins += 1
						print(f"""{username}
Total points: {self.points}, Stages Won: {self.wins}""")
						print(f"Game over. You won {self.wins} stage(s) with a total of {self.points} points.")
						return True
				elif RoundLose == 2:
						print(f"You lost this stage {username}.\n")
						if self.wins == 0:
							print("Game over. You didn't win any stages.")
							return False
						elif self.wins >= 1:
							scores.append(Score(username, self.points, self.wins, 5 ))
							print(f"Game over. You won {self.wins} stage(s).")
							self.save_scores()
							self.points = 0
							self.wins = 0
							return False