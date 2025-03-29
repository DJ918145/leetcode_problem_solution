import random as rd

class RandomizedSet(object):
    def __init__(self):
        self.arr = []

    def insert(self, val):
        if val in self.arr:
            return False
        else:
            self.arr.append(val)
            return True

    def remove(self, val):
        if val in self.arr:
            self.arr.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        return self.arr[rd.randint(0, len(self.arr) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()