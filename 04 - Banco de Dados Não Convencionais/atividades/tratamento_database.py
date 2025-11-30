import pandas as pd

df = pd.read_csv("seuarquivo.csv")

df["inicio_vigencia"] = df["inicio_vigencia"].dt.strftime("%Y-%m-%d")
df["fim_vigencia"] = df["fim_vigencia"].dt.strftime("%Y-%m-%d")