from MonteCarlo import MonteCarlo
from mc import simulate2
from mc import generateRandomNumbers2
from statistics import fmean, quantiles, median 
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
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
    

def graph(realizations):
    # sorted_realizations = sorted(realizations, key=lambda x: x[0])
    # w = [d[0] for d in sorted_realizations]
    # p = [d[1] for d in sorted_realizations]
    # cdf = np.cumsum(p)
    # cdf_normalized = [p / cdf[-1]]
    #
    w_values = [x[0] for x in realizations]
    probabilities = [x[1] for x in realizations]

    sorted_indices = np.argsort(w_values)
    sorted_w_values = np.array(w_values)[sorted_indices]
    sorted_probabilities = np.array(probabilities)[sorted_indices]


    cdf = np.cumsum(sorted_probabilities)
    cdf_normalized = cdf / cdf[-1]

    plt.plot(sorted_w_values, cdf_normalized)
    plt.title("Cumulative Distribution Function of W")
    plt.ylabel("P(W <= w)")
    plt.xlabel("Total Time Calling One Customer, W, (seconds)")
    plt.show()

if __name__ == "__main__":
    # mc = MonteCarlo(1000)
    # rand = mc.generateRandomNumbers()
    rand = generateRandomNumbers2(1000)
    print("u51, u52, u53: ", rand[50:53])
    # sample = mc.simulate()
    realizations = simulate2(1000)
    print(realizations)
    sample = []
    prob = []
    for i in range(len(realizations)):
        sample.append(realizations[i][0])
        prob.append(realizations[i][1])
    
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
    _w_6 = probability(sample, 100, ">")
    print("P(W > 100): ", '%.6f'%(_w_6))
    _w_7 = probability(sample, 120, ">")
    print("P(W > 120): ", '%.6f'%(_w_7))

    upper = max(sample)
    lower = min(sample)
    print("The sample space of W is: ", '%.6f'%(lower), "<=  w  <=", '%.6f'%(upper))
    graph(realizations)