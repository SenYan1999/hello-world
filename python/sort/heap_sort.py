##########################################################
#
#           To Describe the Heap Sort Virtually
#
#           Author:    Mike
#           Time:      9/27/10:13
#
##########################################################


import random
import matplotlib.pyplot as plt
import numpy as np

plt.ion()
plt.pause(0.01)

###################Virtual#####################
x = np.arange(1,N+1)

plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Virtualize the Heap Sort')

ax = plt.subplots()

#Define some global variables
Heap_size = 0
N = 30
Left = lambda i:2*i+1
Right = lambda i:2*i+2

#Keep the maximum heap
def heapify(a,i):
    
    while True:
        global Heap_size
        l,r = Left(i),Right(i)
        largest = i

        largest = l if l < Heap_size and a[l] > a[largest] else largest
        largest = r if r < Heap_size and a[r] > a[largest] else largest

        ax.bar(x[i,l,r],data[i,l,r],color='r',label='swap')

        if largest == i:    break

        a[largest],a[i] = a[i],a[largest]
        heapify(a,largest)
        plt.bar(x,data)

#Build the maximum heap
def build_max_heap(a):
    global Heap_size

    for i in range(Heap_size//2-1,-1,-1):
        heapify(a,i)

#The sort function
def heap_sort(a):
    global Heap_size
    Heap_size = len(a)
    build_max_heap(a)
    
    for i in range(len(a)-1,-1,-1):
        a[i],a[0] = a[0],a[i]
        Heap_size -= 1
        heapify(a,0)

####################Test#######################
data = []
for i in range(0,N):
    data.append(random.randint(0,100))
print("Before: ",data)
heap_sort(data)
print("After: ",data)

###################Virtual#####################
x = np.arange(0,N)

plt.bar(x,data,label='data')

plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Virtualize the Heap Sort')

plt.legend()
plt.show()






















