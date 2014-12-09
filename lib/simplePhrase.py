from phrase import Phrase
import random

class SimplePhrase(phrase.Phrase):
    def __init__(self):
        Phrase.__init__(self, None)

    def __str__(self):
        return random.choice(['dog','cat'])
