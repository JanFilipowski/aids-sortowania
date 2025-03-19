from user_interface import make_interface
import sys
sys.setrecursionlimit(10**6)

def partition(a,l,h):
    piv=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]>=piv:
            i+=1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1

def quick_sort(t,l=0,h=-1):
    if h == -1:
        h=len(t) - 1
    n=len(t)
    if l<h:
        p=partition(t,l,h)
        quick_sort(t,l,p-1)
        quick_sort(t,p+1,h)
        
def quick_step(a,l,h):
    piv=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<=piv:
            i+=1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1

def quick(t,l,h):
    n=len(t)
    if l<h:
        p=quick_step(t,l,h)
        quick(t,l,p-1)
        quick(t,p+1,h)

if __name__ == "__main__":
    print("====== QUICK SORT ======")
    make_interface(quick_sort)
