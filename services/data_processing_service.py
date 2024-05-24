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

    def setHeaderComercio(self, df):
        n_colunas = df.shape[1]
        colunas = ['index', 'bebida', 'genero'] + list(range(1970, 1970 + n_colunas - 3))

        df.columns = colunas
        return df

    def setHeaderExpImp(self, df):
        n_colunas = df.shape[1]
        colunas = ['id', 'pais', 'tipo'] + list(range(1970, 1970 + n_colunas - 3))

        df.columns = colunas
        return df

    def trataCategoria(self, df):
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
        #df_melted['ano'] = df_melted['ano'].str.replace(r'\.\d+', '', regex=True)
        return df_melted


    def get_comercio(self):
        df = pd.read_csv('csv/Comercio.csv', sep=';', header=None)
        df = self.setHeaderComercio(df)
        df = self.trataCategoria(df)
        return self.melt_dataframe(df, id_vars=['index', 'bebida', 'genero', 'categoria'])

    def readcsv(self, csv, tipo):
        df = pd.read_csv('csv/'+csv, sep=';',  memory_map=True)
        df = self.setHeaderExpImp(df)
        df['tipo'] = tipo
        return self.melt_dataframe(df, id_vars=['id', 'pais', 'tipo'])

    def get_exportacao(self):
        df1 = self.readcsv('ExpVinho.csv', 'ExpVinho')
        df2 = self.readcsv('ExpEspumantes.csv', 'ExpEspumantes')
        df3 = self.readcsv('ExpUva.csv', 'ExpUva')
        df4 = self.readcsv('ExpSuco.csv', 'Expsuco')
        df = pd.concat([df1, df2, df3, df4], ignore_index=True)

        return df

    def get_importacao(self):
        df1 = pd.read_csv('csv/ImpVinhos.csv', sep=';')
        df1['tipo'] = 'ImpVinhos'
        df2 = pd.read_csv('csv/ImpEspumantes.csv', sep=';')
        df2['tipo'] = 'ImpEspumantes'
        df3 = pd.read_csv('csv/ImpFrescas.csv', sep=';')
        df3['tipo'] = 'ImpFrescas'
        df4 = pd.read_csv('csv/ImpPassas.csv', sep=';')
        df4['tipo'] = 'ImpPassas'
        df5 = pd.read_csv('csv/ImpSuco.csv', sep=';')
        df5['tipo'] = 'ImpSuco'
        df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
        return self.melt_dataframe(df, id_vars=['id', 'control', 'produto', 'categoria', 'tipo'])

    def get_processa(self):
        df1 = pd.read_csv('csv/ProcessaViniferas.csv', sep='\t')
        df1['Tipo'] = 'ProcessaViniferas'
        df2 = pd.read_csv('csv/ProcessaSemclass.csv', sep='\t')
        df2['Tipo'] = 'ProcessaSemclass'
        df3 = pd.read_csv('csv/ProcessaMesa.csv', sep='\t')
        df3['Tipo'] = 'ProcessaMesa'
        df4 = pd.read_csv('csv/ProcessaAmericanas.csv', sep='\t')
        df4['Tipo'] = 'ProcessaAmericanas'
        df = pd.concat([df1, df2, df3, df4], ignore_index=True)
        df = self.trataCategoria(df)
        return self.melt_dataframe(df, id_vars=['id', 'control', 'produto', 'categoria', 'tipo'])

    def get_producao(self):
        df = pd.read_csv('csv/Producao.csv', sep=';')
        df = self.trataCategoria(df)
        return self.melt_dataframe(df, id_vars=['id', 'control', 'produto', 'categoria' ])
