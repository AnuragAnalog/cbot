#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def input_data(k):
    data = [[0, 0] for i in range(k)]

    dis = "Time taken by J{} for M{}: "
    for i in range(k):
        for j in range(2):
            data[i][j] = float(input(dis.format(i+1,j+1)))
        print("")

    return np.array(data)

def johnson(k, data):
    lt = [0 for i in range(k)]
    h = 0
    t = k-1

    sdata = data
    for i in range(k):
        ind = np.where(sdata == np.min(sdata))
        if ind[1][0] == 0:
            lt[h] = np.min(sdata)
            h = h + 1
        else:
            lt[t] = np.min(sdata)
            t = t - 1
        sdata = list(sdata)
        tr = sdata.pop(ind[0][0])
        sdata = np.array(sdata)

    return lt

k = int(input("Enter the value of k: "))
data = input_data(k)
final = johnson(k, data)

plt.show(plt.plot(np.arange(k)+1, final))
