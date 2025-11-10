###### PT

# Pandas

É uma ferramenta de código aberto para manipulação e análise de dados, amplamente utilizada em ciência de dados, machine learning e outras áreas. Ela permite organizar, limpar e explorar grandes volumes de informações de forma eficiente, utilizando estruturas de dados como os Series (unidimensionais) e DataFrames (bidimensionais). 


## Iniciando com Pandas

* Biblioteca escrita sobre o numpy
* Oferece diversos recursos para visualização e limpeza de dados, com funcionalidades similares aquelas que temos no Excel
* Pandas possui essencialmente dois objetos:
    * `Series` → representa uma única coluna de dados (um vetor unidimensional).
    * `DataFrame` → representa uma tabela de dados (bidimensional), composta por várias `Series` alinhadas pelos índices.


## Criando Estruturas Básicas

### Criando uma Series

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)
```

### Criando um DataFrame

```python
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba']
}

df = pd.DataFrame(dados)
print(df)
```

---

## Operações Comuns

### Visualizando Dados

```python
df.head()      # Mostra as 5 primeiras linhas
df.tail(3)     # Mostra as 3 últimas linhas
df.info()      # Mostra informações gerais do DataFrame
df.describe()  # Estatísticas básicas das colunas numéricas
```

### Selecionando Dados

```python
df['Nome']            # Seleciona uma coluna
df[['Nome', 'Idade']] # Seleciona múltiplas colunas
df.iloc[0]            # Seleciona a primeira linha (por posição)
df.loc[0, 'Nome']     # Seleciona valor específico (por rótulo)
```

---

## Manipulação de Dados

```python
df['Idade'] = df['Idade'] + 1        # Modifica valores
df['Estado'] = ['SP', 'RJ', 'PR']    # Adiciona nova coluna
df.drop('Cidade', axis=1, inplace=True)  # Remove coluna
df.rename(columns={'Nome': 'Pessoa'}, inplace=True)  # Renomeia coluna
```

---

## Leitura e Escrita de Arquivos

```python
df = pd.read_csv('dados.csv')       # Lendo CSV
df.to_csv('saida.csv', index=False) # Salvando CSV
```

---

## Filtrando Dados

```python
df_filtrado = df[df['Idade'] > 25]  # Filtra linhas pela condição
```




---

**Observação:** Este repositório é de caráter **educacional** e serve como documentação de estudo e prática.
