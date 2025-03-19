from user_interface import make_interface

def partition(a,l,h):
    piv=a[h]
    i=l-1
    for j in range(l,h):
        if a[j]>=piv:
            i+=1
            a[j],a[i]=a[i],a[j]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1

def quick_sort_iteracyjnie(t,p=0,r=-1):
    if r == -1:
        r=len(t)-1
    n = r - p + 1
    stack = [0] * n

    top = -1

    top += 1
    stack[top] = p
    top +=1
    stack[top] = r

    while top >= 0:
        r=stack[top]
        top -=1
        p=stack[top]
        top -=1

        pivot = partition(t, p, r)


        if pivot-1 > p:
            top +=1
            stack[top] = p
            top +=1
            stack[top] = pivot - 1

        if pivot+1 < r:
            top +=1
            stack[top] = pivot + 1
            top +=1
            stack[top] = r

if __name__ == "__main__":
    print("====== QUICK SORT ITERACYJNIE ======")
    make_interface(quick_sort_iteracyjnie)