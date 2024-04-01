from math import log as ln

def generateRandomNumbers2(count):
        x = 1000
        a = 24693
        c = 3517
        K = 2 ** 17
        nums = []

        for i in range(count):
            xi = (a * x + c) % K
            ui = xi / K
            x = xi
            nums.append(ui)

        return nums

def generateRandomVariable2(u):
        # Inverse CDF of the exponential distribution
    x = -12 * ln(1 - u)
    return x

def simulate2(count):
        realizations = []
        increment = 1
        for i in range(count):
            w = 0
            p = 1
            for a in range(4):
                rand = generateRandomNumbers2(i+increment)[-1]
                w += 6
                if rand <= 0.2:
                    p *= 0.2
                    w += 4
                elif 0.2 < rand <= 0.5:
                    w += 26
                    p *= 0.3
                else:
                    rand = (rand-0.5)*2
                    time = generateRandomVariable2(rand)
                    p *= 0.5*rand
                    if time >= 25:
                        w += 26
                    else:
                        w += time
                        break
                increment += 1
            realizations.append((w,p))
        return realizations

