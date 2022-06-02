# import la librairie random
import random

# choisi un nombre aléatoire
choise = random.randint(0, 100)

# écrie le nombre et change la couleur
print("\x1b[38;5;160m\x1b[1m", choise)