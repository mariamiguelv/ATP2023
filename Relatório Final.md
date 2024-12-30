# Relatório Final 
Realizado por : João Silva A103919, Leonor Matos A103920, Maria Miguel A103906.

--------
## **CONTEÚDO** 
1. Introdução
2. Metodologia
3. Funcionamento da aplicação
    1. Descrição Informal do projeto
    2. funções
        1. Carregar dados
        2. Guardar dados
        3. Criar Publicação 
        4. Consultar Publicação
        5. Listar Publicações
        6. Listar Autores
        7. Eliminar Publicação
        8. Gerar Relatório

-------


## ** 1. INTRODUÇÃO**
Este projeto foi realizado no âmbito da Unidade Curricular de Algortimos e Técnicas de Programação, com o intuito de criar um sistema que permite criar, atualizar e analisar publicações científicas, além de gerar relatórios com estatístiticas úteis. Com base num dataset de publicações, o sistema possibilita a pesquisa de artigos usando filtros relevantes, tais como a data de publicação, as palavras-chave, autores, etc.
Neste projeto, tivemos como objetivo atender a todas as funções pedidas, tentando solucionar eventuais erros que poderiam surgir aquando da utilização da aplicação pelo utilizador.

## **2. METODOLOGIA** 
Para a realização deste trabalho foi utilizado o editor "Visual Studio Code"e o "Jupiter notebook"em python 3.11.7 64-bit. Para o desenvolvimento da interface gráfica para a aplicação das funções criadas foi utilizado "PySimpleGUI".
Para facilitar o desenvolvimento do projeto foi utilizado o documento disponibilizado: "publicacoes.json" que contém todas as publicações associadas ao trabalho. 
Para a organização do nosso código dividimos em duas principais classes: TaskManager que é responsável por gerenciar as operações com publicações (carregar, guardar, criar, eleminar, etc.) e Menu que é a interface da linha de comando que vai conectar o utilizador às funcionalidades da aplicação.


## **3. FUNCIONAMENTO DA APLICAÇÃO**
### **1. Descrição informal do Projeto**
Este projeto tem por base a criação de uma aplicação de criação, atualização e analise de publicações científicas, que permita ao utilizador a pesquisa de artigos usando filtros relevantes. Deste modo, a interface principal criada é constituída por nove botões
"help", "criar publicação", "consulta de publicação", "conuslta de publicações", "eliminar publicação", "relatório de estatísticas", "listar autores", "importar publicações", "guardar publicações".

### **2. Funções** 
#### **1. Carregar Dados**
Primeiramente, para trabalhar com a base de dados que nos foi fornecida implementamos uma função que carrega todas os dados do ficheiro JSON de modo a que estes possam ser utilizados no restante trabalho. Caso o arquivo JSON não exista é retornada uma lista vazia.

```
def carregar_data(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            return []
```

### **2. Guardar Dados**
Criamos uma função que é capaz de guardar todas as alterações que são feitas no nosso sistema JSON. Este passo é crucial para que consigamos manter a persistência dos dados. 

```
def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)
```

### **3. Criar Publicação** 
Com a criação desta função solicitamos ao utilizador que insira os dados referentes ao título, resumo, palavras-chave, DOI, data de aplicação e URL, bem como as respectivas informações sobre os autores, como o seu nome e afiliação. Os dados são então adiconados à lista e guardados no ficheiro JSON.

```
def criar_publicacao(self):
        new_publication = {
            "title": input("Título: "),
            "abstract": input("Resumo: "),
            "keywords": input("Palavras-chave (separadas por vírgula): "),
            "authors": [],
            "doi": input("DOI: "),
            "publish_date": input("Data de publicação (YYYY-MM-DD): "),
            "url": input("URL: ")
        }

        num_autors = int(input("Número de autores: "))
        for _ in range(num_autors):
            autor = {
                "name": input("Nome do autor: "),
                "affiliation": input("Afiliação: ")
            }
            new_publication["authors"].append(autor)

        self.data.append(new_publication)
        self.save_data()
        print("Publicação criada com sucesso!")
```

#### **4. Consultar Publicação** 
Com a função consultar publicação permitimos ao utilizador que consulte publicações com base no seu título. Caso existam correspondências, as informações serão exibidas em detalhe ( título, resumo e autores).

```
def consultar_publicacao(self):
        while True:
            title = input("Insira o título ou parte dele: ").lower()
            results = [pub for pub in self.data if title in pub["title"].lower()]

            if results:
                for pub in results:
                    print("------------------------------------------------------------------------------------------")
                    print(f"Título: {pub['title']}\n \nResumo: {pub['abstract']}\n \nAutores: {[author['name'] for author in pub['authors']]}\n------------------------------------------------------------------------------------------\n")
                break
            else:
                print("Nenhuma publicação encontrada. Deseja tentar novamente?")
                if input().lower() != 'sim':
                    break
```

#### **5. Listar Publicações** 
De modo a conseguirmos listar publicações, o nosso sistema tem funções responsáveis pela listagem de todos dos títulos, datas e autores de cada respectiva publicação.

```
def listar_publicacoes(self):
        for pub in self.data:
            print(f"Título: {pub['title']}\nData de publicação: {pub['publish_date']}\nAutores: {[author['name'] for author in pub['authors']]}\n")
```

#### **6. Listar Autores**
Para que nos fosse possível organizar as publicações por autores, criamos uma função que exibe o nome de cada autor e as suas publicações.

```
def listar_autores(self):
        autores = {}
        for pub in self.data:
            for autor in pub["authors"]:
                if autor["name"] not in autores:
                    autores[autor["name"]] = []
                autores[autor["name"]].append(pub["title"])

        for autor, artigos in sorted(autores.items()):
            print(f"Autor: {autor}\nPublicações: {', '.join(artigos)}\n")
```

#### **7. Excluir Publicação** 
Com esta função conseguimos remover uma publicação da nossa lista com base no seu título.

```
def delete_publicacao(self):
        while True:
            title = input("Insira o título da publicação a ser removida: ").lower()
            for i, pub in enumerate(self.data):
                if title in pub["title"].lower():
                    print(f"Removendo publicação: {pub['title']}")
                    del self.data[i]
                    self.save_data()
                    print("Publicação removida com sucesso.")
                    return
            print("Publicação não encontrada. Deseja tentar novamente?")
            if input().lower() != 'sim':
                break
```

#### **8. Gerar Relatório** 
Para que conseguissemos criar estatísticas sobre as publicações criamos esta aplicação que nos mostra quais forma as palavras-chaves mais usadas, quais os autores com mais publicações e distribuições de publicações por ano.

```
def gerar_relatorio(self):
        if not self.data:
            print("Nenhuma publicação disponível no sistema.")
            return

        print("\n--------Relatório de Estatísticas--------")
        # Frequência de palavras-chave
        keywords = [keyword for pub in self.data for keyword in pub["keywords"].split(",")]
        keywords_freq = Counter(keywords).most_common(20)
        print("\nPalavras-chave mais frequentes:")
        for keyword, freq in keywords_freq:
            keyword_limpo = keyword.replace(",", "")
            print(f"{keyword_limpo}: {freq} vezes")

        # Número de publicações por autor
        autores = [author["name"] for pub in self.data for author in pub["authors"]]
        autores_freq = Counter(autores).most_common(20)
        print("\nAutores com mais publicações:")
        for autor, freq in autores_freq:
            print(f"{autor}: {freq} publicações")

        # Número de publicações por ano
        anos = [datetime.strptime(pub["publish_date"], "%Y-%m-%d").year for pub in self.data]
        anos_freq = Counter(anos).most_common()
        print("\nNúmero de publicações por ano:")
        for ano, freq in anos_freq:
            print(f"{ano}: {freq} publicações")
        print("----------------------------------------")
```



