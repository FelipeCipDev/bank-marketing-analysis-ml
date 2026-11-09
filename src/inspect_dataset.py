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

    print("\nPrimeiras sete linhas:")
    print(df.head(7))

    print("\nInformações gerais:")
    df.info()

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nValores ausentes por colunas:")
    print(df.isna().sum())

    print("\nDistribuição da variável-alvo:")
    print(df["y"].value_counts())

    print("\nDistribuição percentual da variável-alvo:")
    print(df["y"].value_counts(normalize=True).mul(100).round(2))

    print("\nEstatística descritiva das colunas numéricas:")
    print(df.describe().round(2))

    print("\nValores únicos de job:")
    print(df["job"].unique())

    print("\nQuantidade de 'unknown' por coluna textual:")
    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        unknown_count = df[column].eq("unknown").sum()
        print(f"{column}: {unknown_count}")

    print("\nDistribuição dos valores de pdays:")
    print(df["pdays"].value_counts().head(10))

    print("\nRegistros com pdays = -1:")
    print(df["pdays"].eq(-1).sum())

    print("\nAnálise de pdays sem o código especial -1:")

    valid_pdays = df.loc[df["pdays"] != -1, "pdays"]

    print("Quantidade:", valid_pdays.count())
    print("Média:", round(valid_pdays.mean(), 2))
    print("Mediana:", valid_pdays.median())

    print(
        pd.crosstab(
            df["pdays"] == -1,
            df["poutcome"] == "unknown",
            rownames=["pdays é -1"],
            colnames=["poutcome é unknown"]
        )
    )

if __name__ == "__main__":
    main()