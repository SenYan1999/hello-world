from matplotlib import pyplot as pl
import math
import numpy as np

def get_k(s,d):
    return (s/0.15)**(5/3)

def get_c(s,d):
    return (s/0.15)**(2/3)

def get_y(s,d):
    return (1-s)*(s/0.15)**(2/3)

def get_ND(s,d):
    return 0.4*k**(-0.6)-0.15*k

s_list = np.arange(0,1,0.1)
k_list = []
c_list = []
y_list = []
d_list = []

for i in s_list:
    k_list.append(get_k(i,.15))
    c_list.append(get_c(i,.15))
    y_list.append(get_y(i,.15))
    d_list.append(get_y(i,.15))

print("       k          ","s          ","y          ")

for i in range(10):
    print(s_list[i],end='   ')
    print("%.2f"%k_list[i],end='        ')
    print("%.2f"%c_list[i],end='        ')
    print("%.2f"%y_list[i],end='        ')
    print("%.2f"%d_list[i],end='        ')
    print()

pl.plot(s_list,d_list)
