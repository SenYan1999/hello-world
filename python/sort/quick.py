###################################################
#           Quick Sort Practice
#
###################################################
import random

def partition(a,lo,hi):

    left,right = lo,hi

    while left < right:
        
        while a[left] <= a[lo] and left < hi:
            left += 1
        while a[right] >= a[lo] and right > lo:
            right -=1
        
        if(left < right):
            a[left],a[right] = a[right],a[left]

    a[right],a[lo] = a[lo],a[right]

    return right


def quick_sort(a):
    _quick_sort(a,0,len(a)-1)


def _quick_sort(a,lo,hi):
    
    if lo < hi:
        pivot = partition(a,lo,hi)
        _quick_sort(a,lo,pivot-1)
        _quick_sort(a,pivot+1,hi)

data = []
for i in range(0,10):
    data.append(random.randint(0,10))
print("Before:",data)
quick_sort(data)
print("After:",data)
