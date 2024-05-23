import pandas as pd

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/download"
def __init__(self, base_url):
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
    
def setHeaderComercio(df):
    n_colunas = df.shape[1]
    colunas = ['index', 'Bebida', 'Genero'] + list(range(1970, 1970 + n_colunas - 3))
    df.columns = colunas
    return df

def trataCategoria(df):
    maiuscula = ''
    df['Categoria'] = ''
    coluna = df.columns[1]
    
    df[coluna].fillna(df[df.columns[2]], inplace=True)
    for indice, linha in df.iterrows():
        if str(linha[coluna]).isupper() or str(linha[coluna]) == None:
            maiuscula = linha[coluna].title()
            if df.loc[indice + 1, coluna].isupper() or str(linha[coluna]) == None:
                df.loc[indice, 'Categoria'] = maiuscula
                df.loc[indice, df.columns[2]] = maiuscula
        else:
            df.loc[indice, 'Categoria'] = maiuscula
    return df[df['Categoria'] != ""]

def get_comercio():
    df = pd.read_csv('csv/Comercio.csv', sep=';', header=None)
    df = setHeaderComercio(df)
    return trataCategoria(df)

def get_exportacao():
    df1 = pd.read_csv('csv/ExpVinho.csv', sep=';')
    df1['Tipo'] = 'ExpVinho'
    df2 = pd.read_csv('csv/ExpEspumantes.csv', sep=';')
    df2['Tipo'] = 'ExpEspumantes'
    df3 = pd.read_csv('csv/ExpUva.csv', sep=';')
    df3['Tipo'] = 'ExpUva'
    df4 = pd.read_csv('csv/ExpSuco.csv', sep=';')
    df4['Tipo'] = 'ExpSuco'
    df = pd.concat([df1, df2, df3, df4], ignore_index=True)
    return df

def get_importacao():
    df1 = pd.read_csv('csv/ImpVinhos.csv', sep=';')
    df1['Tipo'] = 'ImpVinhos'
    df2 = pd.read_csv('csv/ImpEspumantes.csv', sep=';')
    df2['Tipo'] = 'ImpEspumantes'
    df3 = pd.read_csv('csv/ImpFrescas.csv', sep=';')
    df3['Tipo'] = 'ImpFrescas'
    df4 = pd.read_csv('csv/ImpPassas.csv', sep=';')
    df4['Tipo'] = 'ImpPassas'
    df5 = pd.read_csv('csv/ImpSuco.csv', sep=';')
    df5['Tipo'] = 'ImpSuco'
    df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
    return df

def get_processa():
    df1 = pd.read_csv('csv/ProcessaViniferas.csv', sep='\t')
    df1['Tipo'] = 'ProcessaViniferas'
    df2 = pd.read_csv('csv/ProcessaSemclass.csv', sep='\t')
    df2['Tipo'] = 'ProcessaSemclass'
    df3 = pd.read_csv('csv/ProcessaMesa.csv', sep='\t')
    df3['Tipo'] = 'ProcessaMesa'
    df4 = pd.read_csv('csv/ProcessaAmericanas.csv', sep='\t')
    df4['Tipo'] = 'ProcessaAmericanas'
    df = pd.concat([df1, df2, df3, df4], ignore_index=True)
    return trataCategoria(df)

def get_producao():
    df = pd.read_csv('csv/Producao.csv', sep=';')
    return trataCategoria(df)
