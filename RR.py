import random


class RRProcesses:
    def __init__(self, n=900, q=1):
        self.processes = [x for x in range(1, n + 1)]
        self.bt = [random.randrange(1, 100) for x in range(1, n + 1)]
        self.n = n
        self.q = q

    def findWaitingTime(self):
        rem = [x for x in self.bt]
        t = 0
        done = False
        while not done:
            done = True
            for i in range(0, self.n):
                if (rem[i] > 0):
                    done = False
                    if (rem[i] > self.q):
                        t += self.q
                        rem[i] -= self.q
                    else:
                        t += rem[i]
                        self.wt[i] = t - self.bt[i]
                        rem[i] = 0

    def findTurnaroundTime(self):
        for i in range(0, self.n):
            self.tt[i] = self.wt[i] + self.bt[i]

    def findAvgTime(self):
        self.wt = [0 for x in range(len(self.processes))]
        self.tt = [0 for x in range(len(self.processes))]
        self.total_wait = 0
        self.total_turnaround = 0
        self.findWaitingTime()
        self.findTurnaroundTime()
        print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
        for i in range(0, self.n):
            self.total_wait += self.wt[i]
            self.total_turnaround += self.tt[i]
            print(str(self.processes[i]) + "\t\t" + str(self.bt[i]) + "\t\t" +
                  str(self.wt[i]) + "\t\t" + str(self.tt[i]))
        print("\n\nAverage waiting time:\t\t" + str(self.total_wait / self.n))
        print("Average turnaround time:\t" +
              str(self.total_turnaround / self.n))


processes = RRProcesses()
processes.findAvgTime()
