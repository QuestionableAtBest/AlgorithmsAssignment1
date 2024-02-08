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
    start = time.perf_counter_ns()
    fut(casemaker(casemaker_size))
    end = time.perf_counter_ns()
    #convert to milliseconds
    return ((end - start) / 1**6)

def average(dictionary):
    for key in dictionary:
        print(f"{key}: {sum(dictionary[key])/len(dictionary[key])}")

all_times = {10:[],20:[], 40:[],80:[],90:[], 100:[],160:[],200:[],300:[],400:[],500:[],800:[],1000:[],10000:[]}
for i in all_times.keys():
    for x in range(100):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)