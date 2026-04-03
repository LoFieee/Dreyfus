from todo import *
from timer import *
from notes import *

def menu():
    print("\n=== MULTI TOOL ===")
    print("1. To-Do List")
    print("2. Timer")
    print("3. Notes")
    print("4. Quitter")

def main():
    while True:
        menu()
        choix = input("Choix : ")

        if choix == "1":
            todo_menu()
        elif choix == "2":
            lancer_timer()
        elif choix == "3":
            notes_menu()
        elif choix == "4":
            print("Bye !")
            break
        else:
            print("Choix invalide")

if __name__ == "__main__":
    main()
