import requests
from typing import List
from bs4 import BeautifulSoup
import os


url_base = 'https://dadosabertos.tse.jus.br/dataset/resultados-2024-correspondencias-esperadas-e-efetivadas-1-turno'
downloads = './dados'

if not os.path.exists(downloads):
    os.mkdir(downloads)

def download_csv_from_tse(url, download_dir):
    pages = find_pages(url)

    for page in pages:
        link = page.find('a', class_='btn btn-primary resource-url-analytics resource-type-None', href=True)

        print(page)
        print(link)

        if link:
            if link['href'].endswith('.zip'):
                path = link['href']

                with open(f'{downloads}/{os.path.basename(path)}', 'w') as _:
                    pass 

                file = requests.get(path, stream=True)

                with open(f'{downloads}/{os.path.basename(path)}', 'wb') as _:
                    for index, chunk in enumerate(file.iter_content(chunk_size=8192)):
                        print(f'Salvando chunk {index + 1} de: {downloads}/{os.path.basename(path)}')

                        if chunk:
                            _.write(chunk)


def find_pages(url) -> List[BeautifulSoup]:
    response = requests.get(url)
    pages = list()

    if response.status_code == 200:
        print('Página carregada com sucesso!')

        soup = BeautifulSoup(response.content, 'lxml')
        container = soup.find('ul', class_='resource-list')
        links = container.find_all('a')

        for link in links:
            path = link['href']

            if not any([path.endswith('.zip.sha512'), path.endswith('.zip'), path == '#']):
                target = f'https://dadosabertos.tse.jus.br{path}'

                print(f'Buscando {target}')
                
                page_response = requests.get(target)

                if page_response.status_code == 200:
                    page = BeautifulSoup(page_response.content, 'lxml')
                    pages.append(page)

                elif page_response.status_code == 404:
                    print('Página interna não encontrada. Erro 404')

                else:
                    raise Exception('Erro ao requisitar a página interna!')
        
        return pages
    
    elif page_response.status_code == 404:
        print('Página não encontrada. Erro 404')
    
    raise Exception('Erro ao requisitar a página!')



if __name__ == '__main__':
    download_csv_from_tse(url_base, downloads)
