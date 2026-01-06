import random

class RandomizedSet:

    def __init__(self):
        self.nummap = {}   # value -> index
        self.numlist = []  # stores values

    def insert(self, val: int) -> bool:
        if val in self.nummap:
            return False
        
        self.nummap[val] = len(self.numlist)
        self.numlist.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nummap:
            return False
        
        idx = self.nummap[val]
        lastVal = self.numlist[-1]

        # move last element to idx
        self.numlist[idx] = lastVal
        self.numlist.pop()

        # update index of moved element
        self.nummap[lastVal] = idx

        # delete removed value
        del self.nummap[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.numlist)
