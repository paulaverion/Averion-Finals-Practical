from utils import UserManaging, GameProper, ScoreManager, Users

game = GameProper.DiceGame()
user = UserManaging.UserManager()

def main():
    print("""Welcome to Dice Roll Game
          1. Register
          2. Login
          3. Exit
          """)
    choice = int(input("Action: "))
    if choice == 1:
        user.register()
        main()
    if choice == 2:
        user.login()
    
if __name__ == "__main__":
    main()
