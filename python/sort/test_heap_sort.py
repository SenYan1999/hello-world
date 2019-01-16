#########################################################3
##      This is a Practice of Heap Sort
##
##########################################################

import random

#define some global variables
heap_size = 0
Left = lambda i:2*i+1
Right = lambda i:2*i+2


#To keep the maximum tree
def heapify(a,i):
    
    while True:
        l,r = Left(i),Right(i)
        largest = i

        largest = l if l < heap_size and a[l] > a[largest] else largest
        largest = r if r < heap_size and a[r] > a[largest] else largest

        if largest == i:    break

        a[i],a[largest] = a[largest],a[i]
        i = largest

#To build the maximum tree
def build_max_tree(a):
    global heap_size
    heap_size = len(a)

    for i in range(len(a)-1//2-1,-1,-1):
        heapify(a,i)

#sort function
def heap_sort(a):
    global heap_size
    heap_size = len(a)
    build_max_tree(a)

    for i in range(len(a)-1,-1,-1):
        a[i],a[0] = a[0],a[i]
        heap_size -= 1
        heapify(a,0)



###############Test code###################
data = []
for i in range(0,20):
    data.append(random.randint(0,100))
print("Before:",data)
heap_sort(data)
print("After:",data)
