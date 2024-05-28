import pandas as pd
from .csv_download_service import CSVDownloadService

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/download"

class DataProcessingService:
    def __init__(self):
        self.csv_service = CSVDownloadService(BASE_URL)
        self.csv_files = [
            "Producao.csv", "ProcessaSemclass.csv", "ProcessaViniferas.csv",
            "ProcessaMesa.csv", "ProcessaAmericanas.csv", "Comercio.csv",
            "ImpVinhos.csv", "ImpEspumantes.csv", "ImpFrescas.csv",
            "ImpPassas.csv", "ImpSuco.csv", "ExpVinho.csv",
            "ExpEspumantes.csv", "ExpUva.csv", "ExpSuco.csv"
        ]
        self.download_csv_files()

    def download_csv_files(self):
        self.csv_service.download_csv_files(self.csv_files)

    def trataCategoria(seld,df):
        maiuscula = ''
        df['categoria'] = ''
        coluna = df.columns[1]

        df[coluna].fillna(df[df.columns[2]], inplace=True)
        for indice, linha in df.iterrows():
            if str(linha[coluna]).isupper() or str(linha[coluna]) == None:
                maiuscula = linha[coluna].title()
                if df.loc[indice + 1, coluna].isupper() or str(linha[coluna]) == None:
                    df.loc[indice, 'categoria'] = maiuscula
                    df.loc[indice, df.columns[2]] = maiuscula
            else:
                df.loc[indice, 'categoria'] = maiuscula
        return df[df['categoria'] != ""]
    def melt_dataframe(self, df, id_vars):
        df_melted = df.melt(id_vars=id_vars, var_name='ano', value_name='valor')

        df_melted['ano'] = df_melted['ano'].str.extract('(\d{4})').astype(int)

        id_vars.extend(['ano'])

        df_grouped = df_melted.groupby(id_vars).agg({'valor': 'sum'}).reset_index()

        df_grouped['id'] = range(1, len(df_grouped) + 1)

        return df_grouped

    def readcsvTipo(self, csv, tipo, sep=';'):
        df = pd.read_csv('csv/' + csv, sep=sep)
        df['tipo'] = tipo
        return df
    def get_comercio(self):
        df = pd.read_csv('csv/Comercio.csv', sep=';')
        df.rename(columns={'Produto': 'produto'}, inplace=True)
        df = self.trataCategoria(df)

        return self.melt_dataframe(df, id_vars=['id', 'control', 'produto', 'categoria'])

    def get_exportacao(self):
        df1 = self.readcsvTipo('ExpVinho.csv', 'Vinhos')
        df2 = self.readcsvTipo('ExpEspumantes.csv', 'Espumantes')
        df3 = self.readcsvTipo('ExpUva.csv', 'Uvas')
        df4 = self.readcsvTipo('ExpSuco.csv', 'Sucos')
        df = pd.concat([df1, df2, df3, df4], ignore_index=True)
        df.rename(columns={'Id': 'id', 'País': 'pais'}, inplace=True)

        return self.melt_dataframe(df, id_vars=['id', 'pais', 'tipo'])

    def get_importacao(self):
        df1 = self.readcsvTipo('ImpVinhos.csv', 'Vinhos')
        df2 = self.readcsvTipo('ImpEspumantes.csv', 'Espumantes')
        df3 = self.readcsvTipo('ImpFrescas.csv', 'Frescas')
        df4 = self.readcsvTipo('ImpPassas.csv', 'Passas')
        df5 = self.readcsvTipo('ImpSuco.csv', 'Sucos')

        df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
        df.rename(columns={'Id': 'id', 'País': 'pais'}, inplace=True)

        return self.melt_dataframe(df, id_vars=['id', 'pais', 'tipo'])

    def get_processa(self):
        df1 = self.readcsvTipo('ProcessaViniferas.csv', 'Viniferas', '\t')

        df2 = self.readcsvTipo('ProcessaSemclass.csv', 'Sem Classe', '\t')
        df3 = self.readcsvTipo('ProcessaMesa.csv', 'Mesa', '\t')
        df4 = self.readcsvTipo('ProcessaAmericanas.csv', 'Americanas', '\t')

        df = pd.concat([df1, df2, df3, df4], ignore_index=True)
        df = self.trataCategoria(df)

        return self.melt_dataframe(df, id_vars=['id', 'control', 'cultivar', 'categoria', 'tipo'])

    def get_producao(self):
        df = pd.read_csv('csv/Producao.csv', sep=';')
        df.rename(columns={'Produto': 'produto'}, inplace=True)
        df = self.trataCategoria(df)
        return self.melt_dataframe(df, id_vars=['id', 'control', 'produto', 'categoria'])