import random
import time

def fut(case):
    fut2(case, 0, len(case) - 1)
    return case


def fut2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut2(case, s, t - q)
        fut2(case, s + q, t)
        fut2(case, s, t - q)


def casemaker(size):
    return [random.randint(0, 1**9) for _ in range(size)]


def timeit(casemaker_size):
    start = time.perf_counter_ns()
    fut(casemaker(casemaker_size))
    end = time.perf_counter_ns()
    #convert to milliseconds
    return ((end - start) / 1**6)

def average(dictionary):
    for key in dictionary:
        print(f"{key}: {sum(dictionary[key])/len(dictionary[key])}")

all_times = {10:[],20:[], 40:[],80:[],90:[], 100:[],160:[],200:[]}

for i in all_times.keys():
    for x in range(150):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)