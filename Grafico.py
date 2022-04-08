#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

class Grafico:
    def desvio_padrao(self,agrupamento, coluna, cor):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)

        plt.rc('figure', figsize=(15, 8))
        fig = grupo[coluna].std().plot.bar(color=cor)
        fig.set_ylabel("Valor aluguel")
        fig.set_title("desvio padrão de aluguel por bairro")
        plt.show()

    def media(self, agrupamento, coluna, cor):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)

        plt.rc('figure', figsize=(15, 8))
        fig = grupo[coluna].mean().plot.bar(color=cor)
        fig.set_ylabel("Valor aluguel")
        fig.set_title("Media de aluguel por bairro")
        plt.show()

    def boxplot(self, agrupamento, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)

        plt.rc('figure', figsize=(15, 8))
        grupo.boxplot([coluna])
        plt.show()

    def histograma(self, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")

        plt.rc('figure', figsize=(15, 8))
        df.hist([coluna])
        plt.show()

    def histogramaGrupos(self, agrupamento, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)

        plt.rc('figure', figsize=(15, 8))
        grupo.hist([coluna])
        plt.show()