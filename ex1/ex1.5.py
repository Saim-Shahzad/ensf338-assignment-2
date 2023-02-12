import timeit
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
    original_time = timeit.timeit(lambda: original_func(i), number=10)
    original_times.append(original_time)

    improved_time = timeit.timeit(lambda: improved_func(i), number=10)
    improved_times.append(improved_time)

plt.plot(original_times, label='Original')
plt.plot(improved_times, label='Improved')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
