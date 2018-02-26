import random


def findWaitingTime(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]


def findTurnaroundTime(processes, n, bt, wt, tat):
    for i in range(0, n):
        tat[i] = wt[i] + bt[i]


def findAvgTime(processes, n, bt):
    waiting_time = [0 for x in range(len(processes))]
    turnaround_time = [0 for x in range(len(processes))]
    total_wait = 0
    total_turnaround = 0
    findWaitingTime(processes, n, bt, waiting_time)
    findTurnaroundTime(processes, n, bt, waiting_time, turnaround_time)
    print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(0, n):
        total_wait += waiting_time[i]
        total_turnaround += turnaround_time[i]
        print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" +
              str(waiting_time[i]) + "\t\t" + str(turnaround_time[i]))
    print("\n\nAverage waiting time:\t\t" + str(total_wait / n))
    print("Average turnaround time:\t" + str(total_turnaround / n))


processes = [x for x in range(1, 1001)]
burst_time = [random.randrange(1, 100) for x in range(1, 1001)]
n = len(processes)
findAvgTime(processes, n, burst_time)
