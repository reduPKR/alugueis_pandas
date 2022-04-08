import pandas as pd

class Agrupar:
    def media(self, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        print("media geral")
        print(df[coluna].mean())

    def media_grupo(self, agrupamento,coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)
        #print(grupo.groups) exibe a indexação
        # for bairro, dados in grupo:
        #     print("*"*100)
        #     print(bairro)
        #     print(dados)
        print("media por {}".format(agrupamento))
        print(grupo[coluna].mean().round(2))

    def descrever(self, agrupamento, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)
        print("describe")
        print(grupo[coluna].describe())

    def minha_descricao(self, agrupamento, coluna):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        grupo = df.groupby(agrupamento)
        print("describe")
        print(grupo[coluna].aggregate(["min","max","sum","mean"]))
        print(grupo[coluna].aggregate(["min", "max", "sum", "mean"]).rename(columns={"min":"Valor minimo", "max":"Valor maximo", "sum":"soma de valores","mean":"media"}))