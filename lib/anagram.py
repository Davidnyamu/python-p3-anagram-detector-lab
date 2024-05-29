# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, words):
        return [d for d in words if sorted(d) == self.sorted_word]
