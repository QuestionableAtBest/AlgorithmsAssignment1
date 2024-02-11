import random
import time

def fut(case):
    h, n = case
    mp8 = 2**31 - 1
    i = 0
    while h[i] != n:
        i = (i + mp8) % len(h)
        if i == 0:
            return None
    return i


def casemaker(size):
    oof = [random.randint(0, int(1e6)) for _ in range(size)]
    for i in range(1, len(oof)):
        oof[i] += oof[i - 1]
    return [oof, oof[random.randint(1, len(oof)) - 1]]

def timeit(casemaker_size):
    case = casemaker(casemaker_size)
    start = time.perf_counter_ns()
    fut(case)
    end = time.perf_counter_ns()
    #convert to milliseconds
    return ((end - start) / 1000000)

def average(dictionary):
    for key in dictionary:
        print(f"{key}: {sum(dictionary[key])/len(dictionary[key])}")

all_times = {10:[],20:[], 40:[],80:[],90:[], 100:[],160:[],200:[],300:[],400:[],500:[],800:[],1000:[],10000:[],20000:[],30000:[],40000:[],70000:[],80000:[],90000:[],100000:[],1000000:[],2000000:[],4000000:[],7000000:[],8000000:[],9000000:[],10000000:[]}
for i in all_times.keys():
    for x in range(100):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)