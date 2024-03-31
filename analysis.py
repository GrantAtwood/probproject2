from MonteCarlo import MonteCarlo
from statistics import fmean

if __name__ == "__main__":
    mc = MonteCarlo(1000)
    sample = mc.simulate()
    print("Examples from sample: ", sample[0:5])
    
    mean = fmean(sample)
    print("Mean of sample: ", mean)

    