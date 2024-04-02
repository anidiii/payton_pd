from random import shuffle
from sys import exit
ANON_NAME = "Nav vārda"
FILENAME = "projekt\\text.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MIN_LENGHT = 3

wants_to_play = True
hit = 0
miss = 0

print(f"Sveiks, spēlētājs, laipni lūdzu tevi savā spēlē, uzmini vārdus!")

name = input("Kā tevi sauc?")
if not name:
    name = ANON_NAME

print(f"\n{name}, šīs spēles noteikumi ir vienkārši.")
print("Es izdomāju tev vārdu un uzrakstu cik burtus tas satur")
print("Tu minēsi pa vienam burtam")
print("Ja burts ir minēts, tad es tev to parādīšu")
print("Tu vari kļūdīties 10 reizes. ")
print("Spēles tēma ir automašinu markas!")

words = []
file = open(FILENAME, encoding="utf-8")
for line in file:
    line = line.lower().strip()
    if len(line) >= MIN_LENGHT:
        english_word = True
        for letter in line:
            if letter not in ALPHABET:
                english_word = False
        if english_word:
            words.append(line)
file.close()

if len(words) == 0:
    print("Faila nav neviena vārda.")
    input("Nospied ENTER lai beigtu spēli.")
    exit()

shuffle(words)

while wants_to_play:
    if len(words) == 0:
        print("\nDiemžēl man beidzās vārdi.")
        wants_to_play = False
    else:
        word = words.pop()
        current_word = "-" * len(word)
        print()
        print(f"{name}, es tev izdomāju vārdu, kurā ir {len(word)} burti.")
        mistakes = 0
        letters = ""

        while not(word == current_word or mistakes > 9):
            print ()
            print(f"Vārds: {current_word}")
            print(f"Kļūdas: {mistakes} no 10")
            print(f"Nosauktie burti: ", end="")

            if len(letters) == 0:
                print("-")
            else:
                print(*letters)

            letter = input("Uzraksti burtu: ").lower()
            while not(len(letter) == 1 and letter in ALPHABET):
                letter = input("Uzraksti burtu no angļu alfabēta: ").lower()

            letter_in_word = False
            for i in range(len(word)):
                if letter == word[i]:
                    current_word = current_word[:i] + letter + current_word[i + 1:]
                    letter_in_word = True
            if not letter_in_word:
                    mistakes += 1
            if not letter in letters:
                    letters += letter    
        print()
        print(f"Vārdi: {current_word}")
        print(f"Kļūdas: {mistakes} no 10")
        print(f"Nosauktie burti: ", end="")

        if len(letters) == 0:
            print("-")
        else:
            print(*letters)
        print()

        if word == current_word:
            print(f"{name}, tu uzminēji vārdu!")
            hit += 1
        else:
            print(f"{name}, diemžēl, tu neuzminēji vārdu...")
            miss += 1
        print(f"Pareizs vārds: \"{word}\".")

        print()
        again = input("Vai gribi nospēlēt vēl vienu reizi (jā/nē)? ").lower()
        while not(again == "jā" or again == "nē"):
            again = input("Vienkārši uzraksti \"jā\" vai \"nē\": ").lower()
        if again == "nē":
            wants_to_play = False
print()
print(f"{name}, paldies par spēli, zemāk tavi spēles rezultāti:")
print(f"Uzminēti vārdi: {hit}, neuzminēti vārdi: {miss}.")
print("Visu labu!")
print()
input("Uzspied ENTER lai beigtu spēli.")


            

            