import time
import os, psutil
t_start = time.perf_counter()
process = psutil.Process(os.getpid())
print((process.memory_info().rss)/(1024*1024))


def calc_fib_last_digit(n):
    dig_1 = 0
    dig_2 = 1
    cur_dig = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            cur_dig = (dig_1 + dig_2) % 10
            dig_1 = dig_2
            dig_2 = cur_dig
        return cur_dig


f = open("3_input.txt")
m = open("3_output.txt", "w")
num = f.read()
m.write(str(calc_fib_last_digit(int(num))))
f.close()
m.close()
print("Time of working: %s second" % (time.perf_counter() - t_start))
print(process.memory_info().rss/(1024*1024), "mb")