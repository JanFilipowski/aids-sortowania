from user_interface import make_interface

def shell_sort(arr):
    n = len(arr)

    gaps = []
    k = 1
    while True:
        h = 2 ** k - 1
        if h > n:
            break
        gaps.append(h)
        k += 1

    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

if __name__ == "__main__":
    print("====== SHELL SORT ======")
    make_interface(shell_sort)

