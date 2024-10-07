# Coletor de Dados Eleitorais Municipais

Este projeto tem como finalidade baixar todos os dados eleitorais disponíveis no site oficial do TSE (Tribunal Superior Eleitoral). Os dados podem ser utilizados para aprendizagem, já que possuem um grande volume e abrangem resultados eleitorais significativos.

## Funcionalidades
- Acessa automaticamente o site do TSE para buscar páginas que contenham arquivos de dados.
- Faz o download de arquivos compactados (.zip) contendo dados eleitorais.
- Salva os arquivos localmente para posterior análise.

## Tecnologias Utilizadas
- **Python**: Linguagem principal utilizada no projeto.
- **Requests**: Para realizar as requisições HTTP e fazer o download dos arquivos.
- **BeautifulSoup**: Para fazer o scraping do conteúdo HTML das páginas.
- **OS**: Para manipular diretórios e arquivos localmente.

## Como Usar

### Requisitos
- Python 3.x
- Bibliotecas: `requests`, `beautifulsoup4`, `lxml`

### Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/coletor-dados-eleitorais.git
    ```
2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

### Execução
Para baixar os dados eleitorais, execute o script principal:

```bash
python coletor.py
