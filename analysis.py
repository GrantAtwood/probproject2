from MonteCarlo import MonteCarlo
from statistics import fmean, quantiles, median 
import matplotlib.pyplot as plt
from math import exp

def probability(W, bound, dir="<="):
    count = 0

    for w in W:
        if w <= bound:
            count += 1
    
    if dir == "<=":
        return count / len(W)
    elif dir == ">":
        return 1 - count / len(W)
    

def graph(sample, mean):
    
    v = 1/mean 
    P = []
    w = sorted(sample)

    for i in range(len(w)):
        p = 1 - exp(-v * w[i])
        P.append(p)
    
    plt.plot(w, P)
    plt.title("Cumulative Distribution Function of W")
    plt.ylabel("P(W <= w)")
    plt.xlabel("Total Time Calling One Customer, W, (seconds)")
    plt.show()

if __name__ == "__main__":
    mc = MonteCarlo(1000)
    sample = mc.simulate()
    print("Examples from sample: ", sample[0:5])
    
    mean = fmean(sample)
    print("Mean of sample: ", '%.6f'%(mean))

    quartiles = quantiles(sample, n=4)
    print("First quartile: ", '%.6f'%(quartiles[0])) 
    print("Third quartile: ", '%.6f'%(quartiles[2]))

    median = median(sample)
    print("Median of sample: ", '%.6f'%(median))

    w_15 = probability(sample, 15)
    print("P(W <= 15): ", w_15)
    w_20 = probability(sample, 20)
    print("P(W <= 20): ", w_20)
    w_30 = probability(sample, 30)
    print("P(W <= 30): ", w_30)
    w_40 = probability(sample, 40, ">")
    print("P(W > 40): ", '%.6f'%(w_40))

    _w_5 = probability(sample, 80, ">")
    print("P(W > 80): ", '%.6f'%(_w_5))
    _w_6 = probability(sample, 115, ">")
    print("P(W > 115): ", '%.6f'%(_w_6))
    _w_7 = probability(sample, 135, ">")
    print("P(W > 135): ", '%.6f'%(_w_7))

    upper = max(sample)
    lower = min(sample)
    print("The sample space of W is: ", '%.6f'%(lower), "<=  w  <=", '%.6f'%(upper))

    graph(sample, mean)