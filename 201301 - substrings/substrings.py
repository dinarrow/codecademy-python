from collections import deque

class FifoSet:

    def __init__ (self):
        self._set = set()
        self._queue = deque()

    def push (self, value):
        self._set.add(value)
        self._queue.append(value)

    def pop (self):
        return self._queue.popleft()

    def __bool__ (self): return bool(self._queue)
    def __len__ (self): return len(self._set)
    def __call__ (self): return self._set

class SubstringGenerator:

    def __init__(self, word):
        self.word = word
        self._subList = self.generate()

    def generate(self):
        substrings = FifoSet()
        substrings.push(self.word)
        l=0
        
        while substrings:
            string = substrings.pop()
            l, previousL = len(string),l
            lWord, rWord = string[:-1], string[1:]
            if l!=previousL and lWord:
                substrings.push(lWord)
            if rWord:
                substrings.push(rWord)

        return substrings()

    def __str__(self): return str(self._subList)
    def __len__ (self): return len(self._subList)
    def __iter__ (self): return iter(self._subList)

subs = SubstringGenerator("abbaz")
print (*subs, sep='\n') #Enumerate subs
print ("Count: %i" % len(subs))
