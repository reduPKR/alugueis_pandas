import pandas as pd


class ImovelResidencial:

    def pegar(self):
        dataframe = pd.read_csv("aluguel.csv", sep=";")
        # print(type(dataframe))
        # print(dataframe.info)
        print(dataframe)
        print(dataframe.head(10))
        # print(dataframe.shape)
        # print(dataframe.shape[0])
        # print(dataframe.shape[1])

        df = pd.DataFrame(dataframe.dtypes, columns=["Tipo dados"])
        df.columns.name = "Variaveis"
        # print(df)

        # print(dataframe["Tipo"])
        # print(dataframe.Tipo)
        tipo = dataframe.Tipo
        tipo.drop_duplicates(inplace=True)
        # corrigir o index
        tipo.index = range(tipo.shape[0])
        print(tipo)

        # Retornar apenas imoveis residenciais
        residencial = [
            "Quitinete", "Casa", "Apartamento", "Casa de Condomínio",
            "Prédio Inteiro", "Flat", "Casa de Vila", "Loft", "Chácara"
        ]

        print(dataframe["Tipo"].isin(residencial))
        selecao = dataframe["Tipo"].isin(residencial);
        df_residencial = dataframe[selecao]
        df_residencial.index = range(df_residencial.shape[0])
        print(df_residencial)
        df_residencial.to_csv("aluguel_residencial.csv", sep=";", index=False)
