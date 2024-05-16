from utils import UserManaging, GameProper

game = GameProper.DiceGame()
user = UserManaging.UserManager()

def main():
    while True:
        game.load_scores()
        user.load_users()
        print("Welcome to Dice Roll Game\n")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Action: "))
        if choice == 1:
            user.register()
            main()
        elif choice == 2:
            user.login()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
