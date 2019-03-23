#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
from itertools import permutations

def input_data(k, m):
    data = [[0 for i in range(m)] for i in range(k)]

    dis = "Time taken by J{} for M{}: "
    for i in range(k):
        for j in range(m):
            data[i][j] = float(input(dis.format(i+1,j+1)))
        print("")

    return np.array(data)

def makespan(tup, k, m, data):
    fdata = [[[0, 0] for i in range(m)] for i in range(k)]

    for i in range(k):
        for j in range(m):
            if i == 0 and j == 0:
                fdata[i][j][0] = 0
            elif i == 0 and j != 0:
                fdata[i][j][0] = fdata[i][j-1][1]
            elif i != 0 and j == 0:
                fdata[i][j][0] = fdata[i-1][j][1]
            else:
                fdata[i][j][0] = max(fdata[i-1][j][1], fdata[i][j-1][1])
            fdata[i][j][1] = fdata[i][j][0] + data[i][j]

    display(tup, k, m, fdata)
    return fdata[k-1][m-1][1]

def display(tup, k, m, fdata):
    tmp = [[0 for i in range(m)] for i in range(k)]

    cols = list()
    rows = list()

    for i in range(m):
        cols.append("M"+str(i+1))

    for i in range(k):
        rows.append("J"+str(tup[i]+1))
        for j in range(m):
            tmp[i][j] = str(fdata[i][j][0])+"-"+str(fdata[i][j][1])

    print(pd.DataFrame(tmp, index=rows, columns=cols))
    print("Makespan for sequence", tuple(rows),"is", fdata[k-1][m-1][1])
    print("")

def minmakespan(k, m, data):
    permuts = permutations([i for i in range(k)])

    mslist = list()
    seqlist = list()
    mini = None
    minseq = tuple([i for i in range(k)])
    for seq in permuts:
        tmp1 = "("
        for i in range(k):
           tmp1 = tmp1 + "J"+str(seq[i]+1)
        seqlist.append(tmp1+")")
        tmpdata = data[list(seq)]
        tmp = makespan(seq, k, m, tmpdata)
        mslist.append(tmp)

        if mini == None:
            mini = tmp
            miniseq = seq
        elif mini > tmp:
            mini = tmp
            miniseq = seq

    tmp = list()
    for j in range(k):
        tmp.append("J"+str(miniseq[j]+1))
    print("Minimum Makespan is", mini, "for the sequence",tuple(tmp))

    return (mslist, seqlist)

k = int(input("No. of Jobs are: "))
m = int(input("No. of Machines(processes) are: "))

data = input_data(k, m)
(mslist, seqlist) = minmakespan(k, m, data)

permut = permutations([i for i in range(k)])
n = len(list(map(tuple, permut)))

"""fig, ax = plt.subplots()
width = 0.5
ax.bar(np.arange(n), mslist, width)
ax.set_xlabel("sequence of jobs")
ax.set_ylabel("Makespan")
ax.set_title("Makespan for different sequence of jobs")
ax.set_xticks(np.arange(n)+width, rotation=90)
ax.set_xticklabels(seqlist)"""

plt.bar(range(n), mslist)
plt.xlabel("sequence of jobs")
plt.ylabel("Makespan")
plt.title("Makespan for different sequence of jobs")
plt.xticks(range(n), seqlist, rotation=45)
plt.show()
