class ATM:

    def __init__(self):
        self.notes = [20, 50, 100, 200, 500]
        self.count = [0] * 5
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.notes)):
            self.count[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        tracked = [0] * 5
        
        for i in reversed(range(len(self.notes))):
            tracked[i] = min(self.count[i], amount // self.notes[i])
            amount -= tracked[i] * self.notes[i]
        
        if amount:
            return [-1]
        
        for i in range(len(tracked)):
            self.count[i] -= tracked[i]

        return tracked
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)