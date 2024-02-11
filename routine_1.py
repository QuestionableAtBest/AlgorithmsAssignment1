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
    return [random.randint(0, 10**9) for _ in range(size)]

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

all_times = {10:[],20:[],25:[],30:[],40:[],50:[],60:[],70:[],80:[],90:[],91:[],92:[],93:[],94:[],95:[],100:[],200:[],300:[],400:[],500:[],800:[],850:[]}
for i in all_times.keys():
    #Change the range here to change how many runs per size (>30 is standard! because statistics!)
    for x in range(50):
        run_time = timeit(i)
        all_times[i].append(run_time)

#uncomment to see all individual runs
#print(all_times)
average(all_times)