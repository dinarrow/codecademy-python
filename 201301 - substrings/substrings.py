from collections import deque

class SubstringGenerator:

    def __init__(self, word):
        self.word = word
        self._subList = set()
        self.count()

    def count(self):
        theList, strings = self._subList, deque()
        theList.add(self.word)
        strings.append(self.word)

        l=0
        while strings:
            string = strings.popleft()
            l, previousL = len(string),l
            lWord, rWord = string[:-1], string[1:]
            if l!=previousL and lWord:
                theList.add(lWord)
                strings.append(lWord)
            if rWord:
                theList.add(rWord)
                strings.append(rWord)            

    def __str__(self): # Invoked when you call str()
        return str(self._subList)

    def __len__ (self): # Invoked when you call len()
        return len(self._subList)

subs = SubstringGenerator("abbaz")
print ("Substrings: %s\nCount: %i" % (subs, len(subs)))
