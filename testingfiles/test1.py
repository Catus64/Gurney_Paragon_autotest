something = "words"

class foo():
    def __init__(self,smtg):
        self.something = smtg

    def printsmtg(self):
        self.something.replace("w","d")
        print(self.something)

foo1 = foo(something)
foo1.printsmtg()
print(something)