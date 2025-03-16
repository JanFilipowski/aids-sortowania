from generator import test_algorithm_avg_time

def make_interface(sort_function):
    while True:
        print("Wprowadź maksymalnie dziesięcioelementowy ciąg liczb naturalnych do posortowania oddzielając elementy spacjami lub podaj pusty ciąg aby wygenerować dane losowo")
        try:
            sequence = input("Ciąg: ")
            if sequence == "":
                sizes = [100, 500, 1000, 3000, 5000, 7000, 10000, 20000, 30000, 40000, 50000]
                num_trials = 10

                sequence_types = ["random", "increasing", "decreasing", "a_shaped", "v_shaped"]
                for sequence_type in sequence_types:
                    test_algorithm_avg_time(sort_function, num_trials, sizes, sequence_type, log=True)
                break
            else:
                def to_natural(x):
                    a = int(x)
                    if a < 0:
                        raise ValueError
                    return a

                sequence = list(map(to_natural, sequence.split()))
                if len(sequence) > 10:
                    raise ValueError

                sort_function(sequence)
                print("Posortowany ciąg:", sequence)
                break
        except ValueError:
            print("Błąd danych. Spróbuj ponownie.\n")