from .GameProper import *
game = DiceGame()

class UserManager:
	accounts = {}
	
	def load_users(self):
		try:
			with open('users.txt', 'r') as f:
				for line in f:
					user = line.strip().split(",")
					self.accounts[user[0]] = User(user[0], user[1])
		except FileNotFoundError:
			print("User file not found.")
		except Exception as e:
			print(f"Error loading users: {e}")

	def save_users(self):
		with open('users.txt', 'w') as f:
			for username, user in self.accounts.items():
				f.write(f"{username},{user.password}\n")
	
	def validate_username(self, username):
		if len(username) < 4:
			print("Username must be atleast 4 characters long.")
			return False
		else:
			if username in self.accounts:
				print("Username already exists.")
				return False
			else:
				return True
			
	def validate_password(self, password):
		if len(password) < 8:
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
				return
			else:
				self.validate_password(password)
				print("Registration Successful.")
				self.accounts[username] = User(username, password)
				self.save_users()
				game.menu(username)
		
	def login(self):
		username = input("Enter username, or leave blank to cancel: ")
		if username in self.accounts:
			password = input("Enter password, or leave blank to cancel: ")
			if password == self.accounts[username].password:
				game.menu(username)
			else:
				print("Incorrect password.")
				self.login()
		else:
			print("Username does not exist.")
			return