import json

FILE = "tasks.json"

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def todo_menu():
    tasks = load()
    while True:
        print("\n--- TO DO ---")
        print("1. Ajouter")
        print("2. Voir")
        print("3. Supprimer")
        print("4. Retour")

        c = input("Choix : ")

        if c == "1":
            t = input("Tâche : ")
            tasks.append({"titre": t})
            save(tasks)

        elif c == "2":
            for i, t in enumerate(tasks):
                print(i+1, t["titre"])

        elif c == "3":
            i = int(input("Numéro : ")) - 1
            if 0 <= i < len(tasks):
                tasks.pop(i)
                save(tasks)

        elif c == "4":
            break
