from GameProper import *
game = DiceGame()

class UserManager:
	accounts = {}
	
	def load_users(self):
		try:
			with open('users.txt', 'r') as f:
				self.accounts = eval(f.read())
		except FileNotFoundError:
			self.accounts = {}

	def save_users(self):
		with open('users.txt', 'w') as f:
			print(self.accounts, file=f)
	
	def validate_username(self):
		if len(self) < 4:
			print("Username must be atleast 4 characters long.")
			return False
		else:
			if self in self.accounts:
				print("Username already exists.")
				return False
			else:
				return True


	def validate_password(self):
		if len(self) < 8:
			print("Password must be atleast 8 characters long.")
			return False
		else:
			return True

	def register(self):
		username = input("Enter username (atleast 4 characters), or leave blank to cancel: ")
		if username == "":
			return
		elif self.validate_username(username):
			
			password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
			if password == "":
				return self.register(username)
			else:
				self.validate_password(password)
		else:
			print("Registration Successful.")
			self.accounts[username] = {"username": username, "password": password, "points": 0, "wins": 0}
			self.login(username)
		
	def login(self):
		username = input("Enter username, or leave blank to cancel: ")
		if username in self.accounts:
			password = input("Enter password, or leave blank to cancel: ")
			if password == self.accounts[username]["password"]:
				game.menu(username)