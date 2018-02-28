import random
from pprint import pprint


class RRProcesses:
    def __init__(self, users=3, n=900, q=1):
        self.users = users
        self.proccesesperuser = int(n / users)
        self.processes = [0 for x in range(users)]
        for i in range(users):
            self.processes[i] = [(i, i * int(n / users) + x)
                                 for x in range(1, int(n / users) + 1)]
        self.bt = [random.randrange(1, 100) for x in range(1, n + 1)]
        self.n = n
        self.q = q

    def findWaitingTime(self):
        rem = [x for x in self.bt]
        t = 0
        done = False
        while not done:
            done = True
            for j in range(0, self.users):
                for i in range(j * self.proccesesperuser, j * self.proccesesperuser + self.proccesesperuser):
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
        self.wt = [0 for x in range(self.n)]
        self.tt = [0 for x in range(self.n)]
        self.total_wait = 0
        self.total_turnaround = 0
        self.findWaitingTime()
        self.findTurnaroundTime()
        for j in range(0, self.users):
            print("User " + str(j + 1))
            print("Process ID\tBurst Time\tWaiting Time\tTurnaround Time")
            for i in range(j * self.proccesesperuser, j * self.proccesesperuser + self.proccesesperuser):
                self.total_wait += self.wt[i]
                self.total_turnaround += self.tt[i]
                print(str(self.processes[j][i - j * self.proccesesperuser][1]) + "\t\t" + str(self.bt[i]) + "\t\t" +
                      str(self.wt[i]) + "\t\t" + str(self.tt[i]))
        print("\n\nAverage waiting time:\t\t" +
              str(self.total_wait / self.n))
        print("Average turnaround time:\t" +
              str(self.total_turnaround / self.n))


processes = RRProcesses()
processes.findAvgTime()
