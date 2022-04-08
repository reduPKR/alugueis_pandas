import matplotlib.pyplot as plt
import pandas as pd

class Outlier:
    def remover(self):
        df = pd.read_csv("aluguel_residencial.csv", sep=';')
        valor = df['Valor']

        #pegar os quartiles
        q1 = valor.quantile(.25)
        q3 = valor.quantile(.75)

        iiq = q3 - q1

        limite_inferior = q1 - (1.5 * iiq)
        limite_superior = q3 + (1.5 * iiq)

        selecao = (valor >= limite_inferior) & (valor <= limite_superior)
        dados = df[selecao]
        dados.to_csv("aluguel_residencial_corrigidos.csv", sep=";", index=False)