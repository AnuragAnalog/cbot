#!/usr/bin/python3

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

def rules():
    title = ["Constraints", " Variables "]
    arr1 = [['≥','≤ 0'],['≤','≥ 0'],['=','Unrestricted']]
    arr2 = [['≥ 0','≥'],['≤ 0','≤'],['Unrestricted', '=']]

    print("Maximization".center(14),"Minimization".center(14))
    tmp= pd.DataFrame(arr1,columns=title).stack().str.center(12).unstack()
    tmp.index = [""]*3
    print(tmp)
    tmp= pd.DataFrame(arr2,columns=title[::-1]).stack().str.center(12).unstack()
    tmp.index = [""]*3
    print(tmp)

def input_data(n, m):
    co = [[0 for i in range(n)] for j in range(m)]
    var_inequ = list()
    constraint_inequ = list()
    costco = list()
    con = list()

    for row in range(m):
        for col in range(n):
            co[row][col] = float(input("Value of x{}: ".format(col+1)))
        print("Constriant inequality?\n1) ≤  2) ≥  3) =")
        constraint_inequ.append(int(input("Your choice-> ")))
        if constraint_inequ[-1] not in range(1,4):
            print("Invalid choice")
            quit()
        con.append(float(input("Enter the value of b{}: ".format(row+1))))
        print("")

    for i in range(n):
        costco.append(float(input("Cost-coefficient of x{}: ".format(i+1))))
    for i in range(n):
        print("Is x{}\n1) ≥ 0  2) ≤ 0  3) Unrestricted".format(i+1))
        var_inequ.append(int(input("Your choice-> ")))
        if var_inequ[-1] not in range(1,4):
            print("Invalid choice")
            quit()
    return co, con, costco, constraint_inequ, var_inequ

def display_table(n, m, co, con, costco, constraint, var, option, s):
    if option == 1:
        print("Maximize")
    else:
        print("Minimize")

    for i in range(n-1):
        print(str(costco[i])+s+str(i+1)+" + ", end="")
    print(str(costco[-1])+s+str(i+2))
    print("Subject to:")
    for i in range(m):
        for j in range(n-1):
            print(str(co[i][j])+s+str(j+1)+" + ", end="")
        print(str(co[i][j+1])+s+str(j+2), end="")
        if constraint[i] == 1:
            print(" ≤ ", end="")
        elif constraint[i] == 2:
            print(" ≥ ", end="")
        else:
            print(" = ", end="")
        print(str(con[i]))
    for i in range(n):
        if var[i] == 1:
            print(s+str(i+1)+" ≥ 0")
        elif var[i] == 2:
            print(s+str(i+1)+" ≤ 0")
        else:
            print(s+str(i+1)+" is unrestricted")

def primal2dual(co, con, costco, constraint, var, option):
    print("\n================\n     Primal     \n================")
    display_table(n, m, co, con, costco, constraint, var, opt, "x")
    co = np.array(co).transpose()
    con, costco = costco, con

    var1 = list()
    constraint1 = list()
    print("\n================\n      Dual      \n================")
    if option == 1:
        for i in range(n):
            if var[i] == 1:
                constraint1.append(2)
            elif var[i] == 2:
                constraint1.append(1)
            else:
                constraint1.append(3)
        for i in range(m):
            if constraint[i] == 1:
                var1.append(1)
            elif constraint[i] == 2:
                var1.append(2)
            else:
                var1.append(3)
        display_table(m,n,co, con, costco, constraint1, var1, 2, "y")
    else:
        for i in range(n):
            if var[i] == 1:
                constraint1.append(1)
            elif var[i] == 2:
                constraint1.append(2)
            else:
                constraint1.append(3)
        for i in range(m):
            if constraint[i] == 1:
                var1.append(2)
            elif constraint[i] == 2:
                var1.append(1)
            else:
                var1.append(3)
        display_table(m,n,co, con, costco, constraint1, var1, 1, "y")

n = int(input("Enter no. of variables: "))
m = int(input("Enter no. of constraints: "))

co, con, costco, constraint_inequ, var_inequ = input_data(n, m)
print("\nObjective function of primal\n1) Maximize\n2) Minimize")
opt = int(input("Your choice-> "))

primal2dual(co, con, costco, constraint_inequ, var_inequ, opt)
print("\nConversion is based on the below rules:- ")
rules()

