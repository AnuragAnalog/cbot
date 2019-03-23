#!/usr/bin/python3

import numpy as np
from scipy.optimize import linprog as lpp

def input_data(co, con, costco, m, n):
    for i in range(m):
        tmp = list()
        print("Enter equation no.{}".format(i+1))
        for j in range(n):
            tmp.append(float(input("Co-efficient of x{} is: ".format(j+1))))
        co.append(tmp)
        con.append(float(input("Value of b{} is: ".format(i+1))))
        print("")

    for i in range(n):
        costco.append(float(input("Cost co-efficient of x{} is: ".format(i+1))))

    co = np.array(co)
    con = np.array(con)
    costco = np.array(costco)
    return 

def normalize(co, con, costco):
    print("What should I do to objective function?")
    print("1) Maximize it or\n2) Minimize it")
    choice = int(input("Your choice-> "))

    if choice == 1:
        costco = -1*costco

    print("Select the type of constraint on A and b: ")
    print("1) A*x ≤ b\n2) A*x = b\n3) A*x ≥ b")
    option = int(input("Your option-> "))

    if option == 3:
        co = -1*co
        con = -1*con

    return option

m = int(input("Enter no. of Equations: "))
n = int(input("Enter no. of Un-knowns: "))

co = list()
con = list()
costco = list()

input_data(co, con, costco, m, n)
eqt = normalize(co, con, costco)

if eqt == 2:
    result = lpp(costco, A_eq=co, b_eq=con, options={"disp": True})
else:
    result = lpp(costco, A_ub=co, b_ub=con, options={"disp": True})

print(result)
