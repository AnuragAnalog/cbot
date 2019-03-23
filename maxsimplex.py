#!/usr/bin/python3

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

def display(co, indexlt, cols):
    arr = pd.DataFrame(co, columns=cols, index=indexlt)
    print(arr)
    return

def input_data(co, con, costco):
    for i in range(m):
        print("Enter Equation no.{}".format(i+1))
        for j in range(1,n+1):
            co[i][j] = float(input("Enter co-efficient of x{}: ".format(j)))
        con.append(float(input("Enter b{}: ".format(i+1))))
        print("")

    for i in range(1,n+1):
        costco[i] = float(input("Enter cost co-efficient of x{}: ".format(i)))

    return

def alternateopt(co, costco):
    tmp = costco[1:n+1]

    for i in range(m):
        if all(co[i, 1:n+1]/tmp == min(co[i, 1:n+1]/tmp)):
            print("This system has an alternate optimal\n")
            break

    return

def solution(var, val, costco, m, n):
    sol = list([[],[0 for i in range(m+n)],[0 for i in range(n+m)]])
    tmp= list()
    for i in range(n+m):
        if i < n:
            tmp.append("x"+str(i+1))
        else:
            tmp.append("s"+str(i-n+1))
    sol[0] = tmp

    for i in range(len(var)):
        for j in range(m+n):
            if var[i] == sol[0][j]:
                sol[1][j] = 1
                sol[2][j] = val[i]

    print("\nSolution is: ")
    print("Variable Status Value")
    for i in range(m+n):
        if sol[1][i] == 1:
            print("   "+sol[0][i]+"\t"+"Basic      "+str(sol[2][i]))
        else:
            print("   "+sol[0][i]+"\t"+"Non-Basic  "+str(sol[2][i]))

    Z = float(np.linalg.multi_dot((costco, sol[2])))
    print("Optimal value (Z) is ", Z)
    return

m = int(input("Enter the no. of Equations: "))
n = int(input("Enter the no. of Un-knowns: "))

co = [[0 for i in range(n+m+1)] for i in range(m)]
costco = [0 for i in range(n+m+1)]
costco = np.array(costco)
con = list()
input_data(co, con, costco)

co = np.array(co)
con = np.array(con)
co[:, 0] = list(con)
co[:, n+1:] = np.eye(m)

costcov = list()
costcov.append("b")
for i in range(1,n+1):
    costcov.append("x"+str(i))
for i in range(n+1, n+m+1):
    costcov.append("s"+str(i-n))

indexlt = list()
indexlt.append([costco[i] for i in range(n+1, n+m+1)])
indexlt.append([costcov[i] for i in range(n+1, n+m+1)])

cols = [costco, costcov]
alternateopt(co, costco)
print("Initial Simplex table:")
display(co, indexlt, cols)

zj = [0 for i in range(n+m+1)]
delj = np.array([1 for i in range(n+m+1)])

k = 0
beta = list(co[:, 0])
while any(delj[delj > 0]):
    costvals = np.array(indexlt[0]).reshape(1,m)

    for i in range(n+m+1):
        tmp = np.array(co[:, i]).reshape(m,1)
        zj[i] = int(np.linalg.multi_dot((costvals, tmp)))
        delj[i] = costco[i] - zj[i]

    delj = np.array(delj)
    if any(delj[delj > 0]):
        indi = int(np.where(delj == max(delj[1:]))[0][0])

        eta = np.where(co[:, indi] != 0, np.array(co[:, 0]/co[:, indi]), np.inf)
        eta[eta == np.inf] = 0
        eta[eta < 0] = 0
        try:
            indj = int(np.where(eta == min(eta[eta > 0]))[0][0])
        except:
            print("Optimization failed")
            print("Equations are unbounded.")
            quit()
        pivot = co[indj, indi]
    else:
        print("Optimization terminated successfully.")
        beta = list(co[:, 0])
        break

    tmp1 = list(co[:, indi])
    co[indj, :] = co[indj, :]/pivot
    tmp = co[indj, :]
    for i in range(m):
        if i == indj:
            continue
        else:
            co[i,:] = co[i,:]-(tmp*tmp1[i])
    co[indj, :] = tmp
    lt = list(co[indj])
    indexlt[0][indj] = costco[indi]
    indexlt[1][indj] = costcov[indi]
    co[indj] = lt
    print("\nIteration No.", k+1)
    display(co, indexlt, cols)
    k = k + 1

solution(indexlt[1], beta, costco[1:], m, n)
