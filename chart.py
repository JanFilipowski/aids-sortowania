import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colormaps  # Zamiast matplotlib.cm.get_cmap
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

    # Przygotuj mapę kolorów
    cmap = colormaps.get_cmap("tab10")

    for i, seq_type in enumerate(sequence_types):
        # Filtruj dane dla danego typu sekwencji
        data = algorithm_data[algorithm_data["sequence_type"] == seq_type]
        data = data.sort_values("size")

        # Rysuj wykres z łączonymi punktami i słupkami błędu
        plt.errorbar(
            data["size"],
            data["avg_time"],
            yerr=data["standard_deviation"],  # Dodanie słupków błędu
            marker="o",
            linestyle="-",
            color=cmap(i),
            label=seq_type,
            capsize=3  # Długość „czapeczki” słupka błędu
        )

    # Ustawienia wykresu
    plt.title(f"Wydajność algorytmu {algorithm.replace('_',' ')} według rodzaju ciągu")
    plt.xlabel("Liczba Elementów")
    plt.ylabel("Średni czas [s]")
    # plt.yscale("log", base=10)  # Ustawienie skali logarytmicznej (log base 10)
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

    # Przygotuj mapę kolorów
    cmap = colormaps.get_cmap("tab10")

    for i, algorithm in enumerate(algorithms):
        # Filtruj dane dla danego algorytmu
        data = seq_data[seq_data["sorting_algorithm"] == algorithm]
        data = data.sort_values("size")

        # Rysuj wykres z łączonymi punktami i słupkami błędu
        plt.errorbar(
            data["size"],
            data["avg_time"],
            yerr=data["standard_deviation"],
            marker="o",
            linestyle="-",
            color=cmap(i),
            label=algorithm,
            capsize=3
        )

    # Ustawienia wykresu
    plt.title(f"Porównanie wydajności algorytmów sortujących dla ciągów typu {seq_type}")
    plt.xlabel("Liczba Elementów")
    plt.ylabel("Średni czas [s]")
    plt.yscale("log", base=10)  # Ustawienie skali logarytmicznej (log base 10)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"charts/{seq_type}_comparison.png")
    plt.close()

print("Wygenerowano wszystkie wykresy w folderze 'charts'")
