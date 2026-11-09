from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "bank-full.csv"

def main():
    df = pd.read_csv(DATA_PATH, sep=";")

    print("Dimensões (linhas, colunas):")
    print(df.shape)

    print("\nNomes das colunas:")
    print(df.columns.tolist())

    print("\nPrimeiras cinco linhass:")
    print(df.head(7))

if __name__ == "__main__":
    main()