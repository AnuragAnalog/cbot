#!/usr/bin/python3

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

def input_data(k, m):
    data = [[0 for i in range(m)] for i in range(k)]

    dis = "Time taken by J{} for M{}: "
    for i in range(k):
        for j in range(m):
            data[i][j] = float(input(dis.format(i+1,j+1)))
        print("")

    return np.array(data)

def makespan(k, m, data):
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

    return np.array(fdata)

def display(k, m, fdata):
    tmp = [[0 for i in range(m)] for i in range(k)]

    cols = list()
    rows = list()

    for i in range(m):
        cols.append("M"+str(i+1))

    for i in range(k):
        rows.append("J"+str(i+1))
        for j in range(m):
            tmp[i][j] = str(fdata[i][j][0])+"-"+str(fdata[i][j][1])

    print(pd.DataFrame(tmp, index=rows, columns=cols))
    print("Makespan is:", fdata[k-1][m-1][1])

k = int(input("No. of Jobs are: "))
m = int(input("No. of Machines(processes) are: "))

data = input_data(k, m)
fdata = makespan(k, m, data)
display(k, m, fdata)
