import random
import time

def fut(case):
    result = 0
    trials = ["1"]
    while True:
        result += 1
        if "".join(trials) == case:
            return result
        i = len(trials) - 1
        while trials[i] == "1":
            trials[i] = "0"
            i -= 1
        if i == -1:
            trials = ["1"] + trials
        else:
            trials[i] = "1"
        if result > 1e24:
            return "WAT"


def casemaker(size):
    return "1" + "".join(random.choices("10", k=size))

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

# all_times = {5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],20:[]}
all_times = {21:[],22:[],25:[]}
for i in all_times.keys():
    for x in range(100):
        run_time = timeit(i)
        all_times[i].append(run_time)

average(all_times)