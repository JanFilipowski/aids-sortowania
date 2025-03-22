# aids-sortowania
Mega fajne repozytorium do sortowania - Projekt nr 1 na AIDS

1. generator.py - moduł generowania losowych testów i zapisywania wyników do logs.csv, 
2. user_interface.py - moduł tworzenia interfejsu użytkownika dla wybranej funkcji sortowania,
3. chart.py - program generujący wykresy na podstawie pliku logs.csv,
4. merge_sort.py, shell_sort.py, heap_sort.py, quick_sort.py, quick_sort_iteracyjnie.py - programy z wskazanymi w nazwie algorytmami sortowania, zawierający interfejs użytkownika z modułu user_interface oraz możliwość testowania przy użyciu danych losowych przy użyciu modułu generator.

Specyfikacja komputera wykorzystanego do wykonania przykładowych testów (zapisanych w pliku logs.csv i folderze charts):
Architecture:                         x86_64
CPU op-mode(s):                       32-bit, 64-bit
Byte Order:                           Little Endian
Address sizes:                        46 bits physical, 57 bits virtual
CPU(s):                               2
Thread(s) per core:                   2
Core(s) per socket:                   1
Socket(s):                            1
NUMA node(s):                         1
Vendor ID:                            GenuineIntel
CPU family:                           6
Model:                                106
Model name:                           Intel(R) Xeon(R) Platinum 8370C CPU @ 2.80GHz
Stepping:                             6
CPU MHz:                              3413.669
CPU max MHz:                          2800.0000
CPU min MHz:                          800.0000
BogoMIPS:                             5586.87
Virtualization:                       VT-x
Hypervisor vendor:                    Microsoft
Virtualization type:                  full
L1d cache:                            48 KiB
L1i cache:                            32 KiB
L2 cache:                             1.3 MiB
L3 cache:                             48 MiB