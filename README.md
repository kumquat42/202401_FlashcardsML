# 202401_FlashcardsML

Editor: Beraud M. 20240109

Open a selected number of Machine Learning flashcards to train.

### Directories and Files:
**pop_quizz.py**: python3 script selecting randomly n number of cards.  
* parameters : --n (integer, default value = 1)

**Machine_Learning_Flashcards** directory:  
| all the flashcards to be called as png file.  
| flaschcard.csv: list of the flashcards files name. To be updated for added and/or custom cards.

### How to run
* Download the github file  
* Run on command line: 
```python3 pop_quizz.py --n int```, where *int* is the number of cards you want to appear.  

Requirements : python 3.1 at least, pandas, PIL, argparse, random
