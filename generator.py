import time
import random

sizes = [100, 500, 1000, 3000, 5000, 7000, 10000, 20000, 30000, 40000, 50000]
sequence_types = ["random", "increasing", "decreasing", "a_shaped", "v_shaped"]

def generate_sequence(n, sequence_type):
    if sequence_type == "random":
        return [random.randint(1, 10 * n) for _ in range(n)]
    elif sequence_type == "increasing":
        return sorted([random.randint(1, 10 * n) for _ in range(n)])
    elif sequence_type == "decreasing":
        return sorted([random.randint(1, 10 * n) for _ in range(n)], reverse=True)
    elif sequence_type == "a_shaped":
        mid = n // 2
        return sorted([random.randint(1, 10 * n) for _ in range(mid)]) + \
               sorted([random.randint(1, 10 * n) for _ in range(mid, n)], reverse=True)
    elif sequence_type == "v_shaped":
        mid = n // 2
        return sorted([random.randint(1, 10 * n) for _ in range(mid)], reverse=True) + \
               sorted([random.randint(1, 10 * n) for _ in range(mid, n)])
    else:
        raise ValueError

def test_algorithm_avg_time(sorting_algorithm, num_trials, sizes, sequence_type, log=False):
    print(f"Typ ciągu: {sequence_type}")
    for size in sizes:
        total_time = 0
        for _ in range(num_trials):
            arr = generate_sequence(size, sequence_type)
            start_time = time.time()
            sorting_algorithm(arr.copy())
            end_time = time.time()
            total_time += end_time - start_time
        avg_time = total_time / num_trials
        print(f"  n = {size}, Średni czas = {avg_time:.6f} s")

        if log:
            import csv
            from datetime import datetime
            log_entry = {
                "sorting_algorithm": sorting_algorithm.__name__,
                "num_trials": num_trials,
                "sequence_type": sequence_type,
                "size": size,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "avg_time": avg_time
            }
            with open("logs.csv", mode="a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=log_entry.keys())
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow(log_entry)
