import random

word_list = [ "camel", "baboon"]
chosen_word = random.choice(word_list)
print(f"{chosen_word}")
place_holder = ""
word = len(chosen_word)

for letter in range(word):
    place_holder += "_"
print(place_holder)

gameover = False
correct_letters = []
while not gameover:
    z = input("Guess a letter: ")

    display = ""
    for letter in chosen_word:

        if letter   == z:
         display += letter
         correct_letters.append (z)
        else:
         display += "_"
    print(display)


