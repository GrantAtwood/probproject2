from math import log as ln
from random import choices

class MonteCarlo:

    def __init__(self, n):
        self.n = n

    def generateRandomNumbers(self):
        x = 1000
        a = 24693
        c = 3517
        K = 2**17
        nums = []

        for i in range(self.n):
            xi = (a * x + c) % K
            ui = xi/K
            x = xi
            nums.append(ui)

        return nums
    
    
    def generateRandomVariable(self, u):
        # Inverse CDF of the exponential distribution
        x = -12 * ln(1 - u)
        return x
    

    def simulate(self):
        randNums = self.generateRandomNumbers()
        callOutcomes = ["Available", "Unavailable", "Busy Tone"]   
        answerOutcomes = ["Answer", "No Answer"]
        realizations = []

        for iteration in range(self.n):
            w = 0

            for a in range(4):
                w += 6 
                outcome = choices(callOutcomes, [0.5, 0.3, 0.2], k=1)[0]

                if outcome == "Available":
                    answer = choices(answerOutcomes, [0.8755, 0.1245], k=1)[0]
                    if answer == "Answer":
                        x = self.generateRandomVariable(randNums[iteration])
                        w += x
                        break
                    elif answer == "No Answer":
                        w += 26
                elif outcome == "Unavailable":
                    w += 26
                elif outcome == "Busy Tone":
                    w += 4

            realizations.append(w)

        return realizations
    
