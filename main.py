import random
import time
import sys

liste = ["Ja, sehr warscheinlich!", "Die Chancen sind gross!", "Nicht so...", "Naja, koennte sein",
        "Du hast ueberhaupt keine Chance.", "Versuch es einfach!", "Joa, so 23% kann es sein", "Die Chancen stehen gerade 99%",
        "Omg, ja!", "Das weiss ich nicht" "Frag nachher nach", "Frag es besser nachher",
        "Kann es gerade nicht sagen", "Hmmmm", "Nein, leider nein", "Denkst du ueberhaupt nach?", "Ja, ja und ja", "Nein, nein, und nein"
        ]


def userinput():
    question = 'Gebe deine Frage mal hier ein:'
    print(question)
    stuff = input("> ")

    print("\nDenke gerade nach..\n")
    time.sleep(3)
    print(random.choice(liste))

    final()


def final():
    print("Willst du noch eine andere Frage fragen? (y)")
    user_reply = input('> ')
    while (input):
        if user_reply == "y":
            userinput()
        else:
            print("Danke für das spielen!")
            sys.exit(0)


print("Wilkommen im Magic 8 Ball!")
userinput()