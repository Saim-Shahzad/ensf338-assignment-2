import time
import matplotlib.pyplot as plt

def original_func(n):
    if n == 0 or n == 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

def improved_func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = improved_func(n-1, memo) + improved_func(n-2, memo)
    return memo[n]

original_times = []
improved_times = []

for i in range(36):
    start = time.time()
    original_func(i)
    end = time.time()
    original_times.append(end - start)

    start = time.time()
    improved_func(i)
    end = time.time()
    improved_times.append(end - start)

plt.plot(original_times, label='Original')
plt.plot(improved_times, label='Improved')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
