import time
import winsound  # fonctionne sur Windows

def beep(i):

    index = 0

    while (index != i):
       index += 1
       winsound.Beep(1000, 50)
       winsound.Beep(500, 50)

def lancer_timer():
    try:
        sec = int(input("Durée (secondes) : "))
        print("Timer lancé...\n")
        time.sleep(sec)

        print("Temps écoulé !")
        beep(5)

    except:
        print("Erreur")