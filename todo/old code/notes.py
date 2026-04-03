FILE = "notes.txt"

def notes_menu():
    while True:
        print("\n--- NOTES ---")
        print("1. Ajouter")
        print("2. Lire")
        print("3. Retour")

        c = input("Choix : ")

        if c == "1":
            note = input("Note : ")
            with open(FILE, "a") as f:
                f.write(note + "\n")

        elif c == "2":
            try:
                with open(FILE, "r") as f:
                    print(f.read(),"\n")
            except:
                print("Aucune note")

        elif c == "3":
            break
