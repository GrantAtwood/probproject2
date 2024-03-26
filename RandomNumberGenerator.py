def main():
    print(RandomNumberGenerator(3))
def RandomNumberGenerator(n):
    x0 = 1000
    a = 24693
    c = 3517
    K = 2**17
    nums = []
    for i in range(n):
        iteration = i + 1
        x1 = (a * x0 + c) % K
        x0 = x1
        ui = x1/K
        nums.append(ui)
    return nums

if __name__ == "__main__":
    main()
