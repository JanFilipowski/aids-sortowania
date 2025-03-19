from user_interface import make_interface

def tworzenie_kopca(t, n, i):
    najmniejszy=i
    #sprawdzamy czy lewa gałąź istnieje i czy jest mniejsza od korzenia
    if i * 2 + 1 <n and t[i * 2 + 1] < t[najmniejszy]:
        najmniejszy = i * 2 +1

    # sprawdzamy czy lewa gałąź istnieje i czy jest mniejsza od korzenia
    if i * 2 + 2 < n and t[i * 2 + 2] < t[najmniejszy]:
        najmniejszy = i * 2 + 2

    if najmniejszy != i:
        t[i],t[najmniejszy] = t[najmniejszy],t[i]
        # sprawdzamy ponowonie miejsce z ktorym zamienilismy wartosci
        tworzenie_kopca(t,n,najmniejszy)

def heap_sort(t):
    # za pomoca petli i funkcji tworzymy pelny kopiec
    # zaczynyamy od pierwszego rodzica czyli n//2
    for i in range(len(t)//2,-1,-1):
        tworzenie_kopca(t,len(t),i)

    #zaczynamy wlasciwe sortowanie
    for i in range(len(t) - 1, 0, -1):
        t[i],t[0] = t[0],t[i]
        tworzenie_kopca(t,i,0)
    return t;

if __name__ == "__main__":
    print("====== HEAP SORT ======")
    make_interface(heap_sort)