import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os

# Wczytanie danych
df = pd.read_csv("logs.csv")

# Utwórz folder na wykresy jeśli nie istnieje
os.makedirs("charts", exist_ok=True)

# Generuj wykresy dla każdego algorytmu
for algorithm in df["sorting_algorithm"].unique():
    plt.figure(figsize=(12, 7))

    # Filtruj dane dla danego algorytmu
    algorithm_data = df[df["sorting_algorithm"] == algorithm]

    # Lista unikalnych typów sekwencji
    sequence_types = algorithm_data["sequence_type"].unique()

    # Generuj kolory dla każdego typu sekwencji
    colors = cm.get_cmap("tab10", len(sequence_types))

    for i, seq_type in enumerate(sequence_types):
        # Filtruj dane dla danego typu sekwencji
        data = algorithm_data[algorithm_data["sequence_type"] == seq_type]
        data = data.sort_values("size")

        # Rysuj wykres z łaczonymi punktami
        plt.plot(data["size"], data["avg_time"],
                 marker="o",
                 linestyle="-",
                 color=colors(i),
                 label=seq_type)

    plt.title(f"Wydajność algorytmu {algorithm.replace("_"," ")} według rodzaju ciągu")
    plt.xlabel("Liczba Elementów")
    plt.ylabel("Średni czas [s]")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"charts/{algorithm}_performance.png")
    plt.close()

# Generuj wykresy dla każdego typu sekwencji
for seq_type in df["sequence_type"].unique():
    plt.figure(figsize=(12, 7))

    # Filtruj dane dla danego typu sekwencji
    seq_data = df[df["sequence_type"] == seq_type]

    # Lista unikalnych algorytmów
    algorithms = seq_data["sorting_algorithm"].unique()

    # Generuj kolory dla każdego algorytmu
    colors = cm.get_cmap("tab10", len(algorithms))

    for i, algorithm in enumerate(algorithms):
        # Filtruj dane dla danego algorytmu
        data = seq_data[seq_data["sorting_algorithm"] == algorithm]
        data = data.sort_values("size")

        # Rysuj wykres z łaczonymi punktami
        plt.plot(data["size"], data["avg_time"],
                 marker="o",
                 linestyle="-",
                 color=colors(i),
                 label=algorithm)

    plt.title(f"Porównanie wydajności algorytmów sortujących dla ciągów typu {seq_type}")
    plt.xlabel("Liczba Elementów")
    plt.ylabel("Średni czas [s]")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"charts/{seq_type}_comparison.png")
    plt.close()

print("Wygenerowano wszystkie wykresy w folderze 'charts'")