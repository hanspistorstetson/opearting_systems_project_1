import random


def findWaitingTime(processes, n, bt, wt, q):
    rem = [x for x in bt]
    t = 0
    done = False
    while not done:
        done = True
        for i in range(0, n):
            if (rem[i] > 0):
                done = False
                if (rem[i] > q):
                    t += q
                    rem[i] -= q
                else:
                    t += rem[i]
                    wt[i] = t - bt[i]
                    rem[i] = 0


def findTurnaroundTime(processes, n, bt, wt, tat):
    for i in range(0, n):
        tat[i] = wt[i] + bt[i]


def findAvgTime(p, n, bt, q):
    wt = [0 for x in range(len(processes))]
    tt = [0 for x in range(len(processes))]
    total_wait = 0
    total_turnaround = 0
    findWaitingTime(processes, n, bt, wt, q)
    findTurnaroundTime(processes, n, bt, wt, tt)
    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(0, n):
        total_wait += wt[i]
        total_turnaround += tt[i]
        print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" +
              str(wt[i]) + "\t\t" + str(tt[i]))
    print("\n\nAverage waiting time:\t\t" + str(total_wait / n))
    print("Average turnaround time:\t" + str(total_turnaround / n))


processes = [x for x in range(1, 1001)]
burst_time = [random.randrange(1, 100) for x in range(1, 1001)]
n = len(processes)
quantum = 2
findAvgTime(processes, n, burst_time, quantum)
