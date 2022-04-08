import pandas as pd

class Frequencias:
    def total_de_apartamento(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        selecao = dados["Tipo"] == "Apartamento"

        #Pega todos os apartamentos
        saida = dados[selecao].shape[0]
        print("Total apartamentos {}".format(saida))

    def total_de_casas(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        selecao = (dados["Tipo"] == "Casa") | (dados.Tipo == "Casa de Vila") | (dados["Tipo"]  == "Casa de Condomínio")

        saida = dados[selecao].shape[0]
        print("Total casas {}".format(saida))

    def area_60_a_100(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        selecao = (dados["Area"] >= 60) & (dados.Area <= 100)

        saida = dados[selecao].shape[0]
        print("Total area entre 60 e 100 {}".format(saida))

    def mais_4_quartos_aluguel_menor_4000(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        selecao = (dados["Quartos"] >= 4) & (dados.Valor <= 4000)

        saida = dados[selecao].shape[0]
        print("Total mais de 4 quaros {}".format(saida))