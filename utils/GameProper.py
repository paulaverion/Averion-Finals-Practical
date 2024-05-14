import random
from ScoreManager import*

class DiceGame:
	def __init__(self):
		pass

	def load_scores():
		pass

	def save_scores():
		pass

	def play_game():
		pass

	def show_top_scores():
		pass

	def logout():
		pass

	def menu(username):
		print(f"Welcome, {username}!")
		print("""
		Menu: 
		1. Start Game
		2. Show Top Scores
		3. Log Out
		""")
		
		try:
			choice = input("Enter your choice, or leave blank to cancel: ")
			if choice == 1:
				print(f"Starting game as {username}...\n")
				DiceGame.play_game()
			elif choice == 2:
				DiceGame.show_top_scores()
			elif choice == 3:
				return
			else:
				return

		except ValueError:
			print("Invalid choice.")