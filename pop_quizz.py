# open x flashcards for machine learning...
'''

Recover a number --n of ML_flashcards. Default value being 1.

'''

## Import librairies
import argparse
import random
import pandas as pd
import PIL
from PIL import Image

## Récupérer le nombre de flashcards
mon_parser = argparse.ArgumentParser(description = 'Open n number of Flashcards', argument_default=1)
mon_parser.add_argument("--n", type = int, default=1)
args = mon_parser.parse_args()
nombre = args.n

#print(args.n, type(args.n))
#print(nombre, type(nombre))


## fonction to recover the title of the flashcards:
def pop_quizz_ML(nombre):
    liste = []
    for i in range (0, nombre):
        liste.append(data.loc[random.randint(0, 299), 'card_name'])

    return liste

## Read Data
data = pd.read_csv('/home/melb/Documents/Livres_Cheatsheet/flashcard.csv', names=['card_name'])
#print(data.shape) #(299, 1)
data.head()


## Select X flashcards
liste = pop_quizz_ML(nombre)
#print(liste)

for item in liste:
    with Image.open(f'/home/melb/Documents/Livres_Cheatsheet/Machine_Learning_Flashcards/{item}') as card:
        card.show()

