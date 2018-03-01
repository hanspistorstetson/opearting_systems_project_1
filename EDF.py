import random
import operator

class EDFProcesses:
    def __init__(self, n=900):
        self.processes = [x for x in range(1, n+1)]
        t = 50
        self.bt = [random.randrange(1, t) for x in range(1, n+1)]
        self.dl = [random.randrange(500, (t*(n+1))) for x in range(1, n+1)]
        self.q = list()
        self.n = n
        for i in range(0, self.n):
           self.q.append((self.dl[i], i))
        self.q.sort(key = operator.itemgetter(0))
               
        
    def findWaitingTime(self):
        self.wt[0] = 0
        for i in range(0, self.n):
            ((dlt, num)) = self.q[i]
            self.wt[i] = self.bt[num] + self.wt[i-1]
 

    def findTurnaroundTime(self):
        for i in range(0, self.n):
            ((dlt, num)) = self.q[i]
            self.tt[i] = self.wt[i] + self.bt[num]

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
            ((dlt, num)) = self.q[i]
            print(str(num) + "\t\t" + str(self.bt[num]) + "\t\t" +
                  str(self.wt[i]) + "\t\t" + str(self.tt[i]))
        print("\n\n Average waiting time:\t\t" + str(self.total_wait / self.n))
        print("Average turnaround time:\t" + str(self.total_turnaround / self.n))


processes = EDFProcesses()
processes.findAvgTime()
