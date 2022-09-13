import time
import os, psutil

t_start = time.perf_counter()
process = psutil.Process(os.getpid())

results = [0]*10000
def calc_fib(n):
    if results[n] == 0:
        if n == 1 or n == 2:
            results[n] = 1
        if n > 2:
            results[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return int(results[n])


f = open("2_input.txt")
m = open("2_output.txt", "w")
num = f.read()
m.write(str(calc_fib(int(num))))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print((process.memory_info().rss)/(1024*1024), "mb")