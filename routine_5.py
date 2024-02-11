import random
import time

def fut(case):
    i = 1
    while i < len(case):
        if i == 0 or case[i] >= case[i - 1]:
            i += 2
        else:
            case[i], case[i - 1] = case[i - 1], case[i]
        i -= 1
    return case


def casemaker(size):
    return [random.randint(0, 1e9) for _ in range(size)]


def timeit(casemaker_size):
    case = casemaker(casemaker_size)
    start = time.perf_counter_ns()
    fut(case)
    end = time.perf_counter_ns()
    #convert to milliseconds
    return ((end - start) / 10**6)

def average(dictionary):
    for key in dictionary:
        print(f"{key}: {sum(dictionary[key])/len(dictionary[key])}")

all_times = {12000:[],14000:[],16000:[],18000:[],20000:[],50000:[],100000:[]}
for i in all_times.keys():
    for x in range(100):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)