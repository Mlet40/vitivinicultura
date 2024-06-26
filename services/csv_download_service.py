import os
import requests

class CSVDownloadService:
    def __init__(self, base_url, download_dir='./csv'):
        self.base_url = base_url
        self.download_dir = download_dir
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def download_csv(self, filename):
        url = f"{self.base_url}/{filename}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_path = os.path.join(self.download_dir, filename)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return True
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar o arquivo {filename}: {e}")
            return False

    def download_csv_files(self, filenames):

        for filename in filenames:
            if not self.download_csv(filename):
                print(f"Falha no download de {filename} no site da embrapa, a api poderá ser utilizada, porém  a api consumirá os CSVs que estão em sua versão antiga, na pasta csv")
                break
