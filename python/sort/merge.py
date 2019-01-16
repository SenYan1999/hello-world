#This python file is used to practice the sort function merge sort
#Time:      2018/9/22 16:03
#Author:    Mike
############################################################################


def merge(a,lo,mid,hi):
    i,j = lo,hi
    aux = []

    while i<=mid and j<=hi:
        if a[i] < a[j]:
            aux.append(a[i])
            i = i+1
        else:
            aux.append(a[j])
            j = j+1
    
    while i>mid and j<=hi:
        aux.append(a[j])
        j = j+1
    
    while i<=mid and j>hi:
        aux.append(a[i])
        i = i+1
    print(aux," ",hi-lo+1)
    
"""
    k = 0
    for i in range(lo,hi+1):
    a[i] = aux[k]
    k += 1
"""

def merge_sort(a,lo,hi):
    if lo >= hi:return

    mid = int((lo+hi)/2)
    merge_sort(a,lo,mid)
    merge_sort(a,mid+1,hi)
    merge(a,lo,mid,hi)

data = [1,2,45,34,23,4,5,7,12,4] 
print('Before',data)
merge_sort(data,0,9)
print('After',data)
