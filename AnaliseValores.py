import pandas as pd

class AnaliseValores:
    def valor_bruto(self):
        df = pd.read_csv("aluguel_residencial.csv", sep=';')
        df['ValorBruto'] = df["Valor"] + df["Condominio"] + df["IPTU"]
        print(df)
        df.to_csv("aluguel_residencial.csv", sep=";", index=False)

    def valor_metros(self):
        df = pd.read_csv("aluguel_residencial.csv", sep=';')
        df['ValorMetros'] = (df["Valor"] / df["Area"]).round(2)
        print(df)
        df.to_csv("aluguel_residencial.csv", sep=";", index=False)

    def valor_metros_bruto(self):
        df = pd.read_csv("aluguel_residencial.csv", sep=';')
        df['ValorMetrosBruto'] = (df["ValorBruto"] / df["Area"]).round(2)
        print(df)
        df.to_csv("aluguel_residencial.csv", sep=";", index=False)

    def tipo_agregado(self):
        df = pd.read_csv("aluguel_residencial.csv", sep=";")
        lista = [ "Casa", "Casa de Condomínio", "Casa de Vila"]
        df["TipoAgregado"] = df["Tipo"].apply(lambda item: 'Casa' if item in lista else 'Apartamento')
        print(df)
        df.to_csv("aluguel_residencial.csv", sep=";", index=False)
