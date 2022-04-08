import pandas as pd

class TratamentoDeDados:
    def retirarNulos(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        #dados.info() consegue achar quais linhas possuem valores null
        print("-"*80)
        original = dados.shape[0]
        print("Total com nulos {}".format(original))

        selecao = (dados["Tipo"] == "Apartamento") & (dados["Condominio"].isnull())
        dados = dados[~selecao]
        atual = original - dados.shape[0]
        print("Eliminados com condominios nulos {}".format(atual))

        dados.dropna(subset=["Valor","IPTU"], inplace=True)
        atual = original - dados.shape[0]
        print("Eliminados por valor ou IPTU nulos {}".format(atual))
        print("Total final {}".format(dados.shape[0]))

    def ColocarZero(self):
        dados = pd.read_csv("aluguel_residencial.csv", sep=";")
        print(dados.info())
        selecao = (dados["Tipo"] == "Apartamento") & (dados["Condominio"].isnull())
        dados = dados[~selecao]

        dados.fillna({"Valor":0.0, "IPTU":0.0, "Condominio":0.0}, inplace=True)
        print(dados.info())
        dados.to_csv("aluguel_residencial.csv", sep=";", index=False)