import random
import time


def fut(case):
    h, n = case
    l = 0
    r = len(h)
    while r > l:
        time.sleep(0.0001)
        m = (r + l) // 2
        if h[m] == n:
            return m
        elif h[m] > n:
            r = m
        else:
            l = m


def casemaker(size):
    start = random.randint(1, 10 * size) + size
    step = random.randint(1, 10)
    oof = range(start, start + (size + 2) * step, step)
    return [oof, oof[random.randint(1, len(oof)) - 1]]

#Function that will time a run of casemaker_size and return it in milliseconds
def timeit(casemaker_size):
    case = casemaker(casemaker_size)
    start = time.perf_counter_ns()
    fut(case)
    end = time.perf_counter_ns()
    #convert to milliseconds
    return ((end - start) / 1000000)

#Takes in the dictionary of key:value being size:list of all times at this size and then finds the mean time of each size.
def average(dictionary):
    for key in dictionary:
        print(f"{key}: {sum(dictionary[key])/len(dictionary[key])}")

all_times = {10:[],20:[], 40:[],70:[],80:[],90:[],100:[],160:[],200:[],300:[],400:[],500:[],700:[],800:[],900:[],1000:[]}

for i in all_times.keys():
    for x in range(100):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)