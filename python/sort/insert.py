#############################################
#           Vurtually Insert Sort
#
#############################################

import matplotlib.pyplot as plt

def sort(a):
    for i in range(len(a)-1):
        j = i+1
        
        while a[j] < a[j-1] and j > 0:
            a[j],a[j-1] = a[j-1],a[j]
            j -= 1

data = [1,3,2,34,32,324,32,1,3]
print("Before:",data)
sort(data)
print("After:",data)
