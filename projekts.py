from random import shuffle
from sys import exit
ANON_NAME = "Nav vārda"
FILENAME = "text.txt"

print(f"Sveiks, spēlētājs, laipni lūdzu tevi savā spēlē, uzmini vārdus!")
name = input("Kā tevi sauc?")
if not name:
    name = ANON_NAME
print(f"\n{name}, šīs spēles noteikumi ir vienkārši")
print("Es izdomāju tev vārdu un uzrakstu cik burtus tas satur")
print("Tu minēsi pa vienam burtam")
print("Ja burts ir minēts, tad es tev to parādīšu")
print("Tu vari kļūdīties 10 reizes ")

words = [ ]
file = open(FILENAME, encoding="utf-8")
for line in file:
    line = line.lower().strip()
file.close()

if len(words) == 0:
    print("Faila nav neviena varda")
    input("Nospied ENTER lai beigtu spēli")
    exit()

shuffle(words)

while wants_to_play:
    if len(words) == 0:
        print("Diemžēl man beidzās vārdi")
        wants_to_play = False
    else:
        word = words.pop()
        
        current_word = "-" * len(word)
        print()
        print(f"{name}, es tev izdomāju vārdu, kurā ir {len(word)} burti.")
        mistakes = 0
        letters = " "
        
        while not(word == current_word or mistakes > 6):
            print ()
            print(f"Vārds: {current_word}")
            print(f"Kļūdas: {mistakes} no 10")
            print(f"Nosauktie burti: ", end="")
            
            if len(letters) == 0:
                print("-")
            else:
                print(*letters)
            
            letter = input("Uzraksti burtu: ").lower()
            