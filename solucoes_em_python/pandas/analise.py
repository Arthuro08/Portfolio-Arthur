import pandas as pd

df = pd.read_excel("solucoes_em_python/pandas/planilha.xlsx")
print("\n",df.head())
print("\n\n", df.info())
print("\n", df.describe())