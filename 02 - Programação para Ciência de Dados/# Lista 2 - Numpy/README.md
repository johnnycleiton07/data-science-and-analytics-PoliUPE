###### PT

# Numpy

A biblioteca NumPy é uma das bases da computação científica em Python, oferecendo suporte a arrays multidimensionais e operações matemáticas de alto desempenho. É amplamente usada para processamento numérico, estatística e análise de dados.



## Iniciando com Numpy

### Método *numpy.info()*

Você pode usar este método para exibir informações detalhadas sobre qualquer função do NumPy, como `numpy.add`, da seguinte forma:

```python
# importando a biblioteca e dando um apelido para uso (np)
import numpy as np

np.info(np.add)
```

Esse comando mostra na tela a documentação interna do método np.add, incluindo sua assinatura, descrição, parâmetros, tipos de retorno e exemplos de uso.




### Função *range()*

Cria um objeto do tipo "range" (um iterável que não é armazenado na memória). Já o uso da função `list` é para transformar esse objeto range em uma lista:

```python
lista = list(range(0, 16))
print(lista)
```

🔹 **Saída:**

```python
# o range(0, 16) gera números de 0 até 15, pois o valor final (16) não é incluído.
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```



### Método *numpy.array()*

Para converter a lista em um array NumPy, basta usar a função `np.array()`:

```python
array = np.array(lista)
print(array)
```

🔹 **Saída:**

```python
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
```

Dessa forma, é possível obter um array NumPy, que permite realizar operações matemáticas vetorizadas e muito mais rapidamente do que com listas comuns do Python.




### Função *numpy.arange(início, fim)*

Funciona de forma parecida com `range()`, mas já retorna um array NumPy, que é ideal para cálculos numéricos e manipulação de dados.

```python
array = np.arange(0, 16)
print(array)
```



## Exercícios

1. A partir do último array criado anteriormente na seção "Iniciando com Numpy", realize os seguintes procedimentos:

* Exiba o formato atual do array.

```python
print("Formato original:", array.shape)
```

🔹 **Saída:**

```python
# o “16” indica a quantidade de elementos e a vírgula indica que é uma tupla de um único elemento.
Formato original: (16,)
```


* Altere o formato para (4, 4) e exiba novamente o formato do array após redimensioná-lo.

```python
# Altera o formato para 4x4
array = array.reshape(4, 4)

# Exibe o novo formato e mostra o array dimensionado
print("Novo formato:", array.shape)
print(array)
```

🔹 **Saída:**

```python
Novo formato: (4, 4)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
```



2. Compute a média, mediana e o desvio padrão do array resultante da questão anterior.

* Média: representa o valor médio dos dados, obtido somando todos os elementos e dividindo pela quantidade total.
* Mediana: é o valor central que separa a metade menor e a metade maior dos dados quando estão em ordem.
* Desvio padrão: mede o quanto os valores se afastam da média, indicando o grau de variação ou dispersão dos dados.

É possível calcular a média, mediana e o desvio padrão de um array NumPy usando as funções `np.mean()`, `np.median()` e `np.std()`:

```python
media = np.mean(array)
mediana = np.median(array)
desvio_padrao = np.std(array)

print("Média:", media)
print("Mediana:", mediana)
print("Desvio padrão:", desvio_padrao)
```

🔹 **Saída:**

```python
Média: 7.5
Mediana: 7.5
Desvio padrão: 4.6097722286464435
```



3. Crie uma cópia do array atual e transforme todos os números em valores negativos.

```python
# cria uma cópia do array
array_negativo = array.copy()

# transforma todos os valores em negativos
array_negativo = -array_negativo

print (array_negativo)
```

* Você pode criar uma cópia do array e multiplicar todos os elementos por `-1` para torná-los negativos:

```python
# cria uma cópia do array
array_negativo = array.copy()

# transforma todos os valores em negativos
array_negativo = -array_negativo

print(array_negativo)
```

🔹 **Saída:**

```python
[[  0  -1  -2  -3]
 [ -4  -5  -6  -7]
 [ -8  -9 -10 -11]
 [-12 -13 -14 -15]]
```

* O método `.copy()` garante que a modificação não altere o array original, mantendo os dados intactos.




4. Realize os seguintes procedimentos:

* Passo 1. Concatene verticalmente (row-wise) o array de números positivos com o array de números negativos.

```python
# renomeando o array para array_positivo só para entender melhor o código
array_positivo = array

array_vertical = np.vstack((array_positivo, array_negativo))
print("Vertical (8x4):\n", array_vertical)
```

🔹 **Saída do Passo 1:**

```python
Vertical (8x4):
 [[  0   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]
 [ 12  13  14  15]
 [  0  -1  -2  -3]
 [ -4  -5  -6  -7]
 [ -8  -9 -10 -11]
 [-12 -13 -14 -15]]
```


* Passo 2. Concatene horizontalmente (column-wise) o array resultante do passo 1 com ele mesmo.

```python
# Concatenação horizontal com ele mesmo
array_horizontal = np.hstack((array_vertical, array_vertical))
print("Horizontal (8x8):\n", array_horizontal)
```

🔹 **Saída do Passo 2:**

```python
Horizontal (8x8):
 [[  0   1   2   3   0   1   2   3]
 [  4   5   6   7   4   5   6   7]
 [  8   9  10  11   8   9  10  11]
 [ 12  13  14  15  12  13  14  15]
 [  0  -1  -2  -3   0  -1  -2  -3]
 [ -4  -5  -6  -7  -4  -5  -6  -7]
 [ -8  -9 -10 -11  -8  -9 -10 -11]
 [-12 -13 -14 -15 -12 -13 -14 -15]]
```



* Passo 3. Concatene em profundidade três cópias do array resultante do passo anterior, exibindo o formato final.

`np.dstack` é usado para empilhar arrays ao longo de uma terceira dimensão.

```python
array_profundidade = np.dstack((array_horizontal, array_horizontal, array_horizontal))
print("Profundidade (8x8x3):\n", array_profundidade)
print("Formato final:", array_profundidade.shape)
```

🔹 **Saída do Passo 3:**

```python
Profundidade (8x8x3):
 [[[  0   0   0]
  [  1   1   1]
  [  2   2   2]
  [  3   3   3]
  [  0   0   0]
  [  1   1   1]
  [  2   2   2]
  [  3   3   3]]

 [[  4   4   4]
  [  5   5   5]
  [  6   6   6]
  [  7   7   7]
  [  4   4   4]
  [  5   5   5]
  [  6   6   6]
  [  7   7   7]]

 [[  8   8   8]
  [  9   9   9]
  [ 10  10  10]
  [ 11  11  11]
  [  8   8   8]
  [  9   9   9]
  [ 10  10  10]
  [ 11  11  11]]

 [[ 12  12  12]
  [ 13  13  13]
  [ 14  14  14]
  [ 15  15  15]
  [ 12  12  12]
  [ 13  13  13]
  [ 14  14  14]
  [ 15  15  15]]

 [[  0   0   0]
  [ -1  -1  -1]
  [ -2  -2  -2]
  [ -3  -3  -3]
  [  0   0   0]
  [ -1  -1  -1]
  [ -2  -2  -2]
  [ -3  -3  -3]]

 [[ -4  -4  -4]
  [ -5  -5  -5]
  [ -6  -6  -6]
  [ -7  -7  -7]
  [ -4  -4  -4]
  [ -5  -5  -5]
  [ -6  -6  -6]
  [ -7  -7  -7]]

 [[ -8  -8  -8]
  [ -9  -9  -9]
  [-10 -10 -10]
  [-11 -11 -11]
  [ -8  -8  -8]
  [ -9  -9  -9]
  [-10 -10 -10]
  [-11 -11 -11]]

 [[-12 -12 -12]
  [-13 -13 -13]
  [-14 -14 -14]
  [-15 -15 -15]
  [-12 -12 -12]
  [-13 -13 -13]
  [-14 -14 -14]
  [-15 -15 -15]]]
Formato final: (8, 8, 3)
```

Em resumo:

| Função      | Descrição                                | Dimensão do resultado                               |
| ----------- | ---------------------------------------- | --------------------------------------------------- |
| `np.vstack` | Empilha arrays verticalmente (linhas)    | Aumenta o número de linhas                          |
| `np.hstack` | Empilha arrays horizontalmente (colunas) | Aumenta o número de colunas                         |
| `np.dstack` | Empilha arrays na profundidade (3ª dim)  | Cria uma nova dimensão, aumentando a “profundidade” |



5. Utilize o array do passo 1 da questão anterior e transforme os valores da segunda e terceira colunas em 1.

* Podemos acessar colunas específicas de um array NumPy usando indexação por slices e atribuir novos valores diretamente.

```python
# transformar a 2ª e 3ª colunas em 1
array_vertical[:, 1:3] = 1

print (array_vertical)
```

* `:` indica todas as linhas e 1:3 seleciona a segunda e terceira colunas. Assim, todos os valores dessas colunas foram substituídos por 1.

🔹 **Saída:**

```python
[[  0   1   1   3]
 [  4   1   1   7]
 [  8   1   1  11]
 [ 12   1   1  15]
 [  0   1   1  -3]
 [ -4   1   1  -7]
 [ -8   1   1 -11]
 [-12   1   1 -15]]
```


6. Adicione 2.5 a todos os valores presentes no array resultante da etapa anterior.

```python
array_soma = array_vertical + 2.5

print (array_soma)
```

🔹 **Saída:**

```python
[[  2.5   3.5   3.5   5.5]
 [  6.5   3.5   3.5   9.5]
 [ 10.5   3.5   3.5  13.5]
 [ 14.5   3.5   3.5  17.5]
 [  2.5   3.5   3.5  -0.5]
 [ -1.5   3.5   3.5  -4.5]
 [ -5.5   3.5   3.5  -8.5]
 [ -9.5   3.5   3.5 -12.5]]
```



7. Realize as seguintes operações:

* Crie uma matriz com valor 3 em todas as posições com dimensionalidade (4, 2).

```python
matriz3 = np.full((4, 2), 3)
print ("Matriz 4x2 com valor 3:\n", matriz3)
```

🔹 **Saída:**

```python
Matriz 4x2 com valor 3:
 [[3 3]
 [3 3]
 [3 3]
 [3 3]]
```

* Crie uma matriz identidade de dimensionalidade (4, 4).

```python
identidade = np.eye(4)
print ("Matriz identidade 4x4:\n", identidade)
```

🔹 **Saída:**

```python
Matriz identidade 4x4:
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```

* Compute o produto entre a transposta da primeira matriz e a matriz identidade, apresentando o resultado final.

```python
resultado = matriz3.T @ identidade
print ("Produto da transposta com a identidade:\n", resultado)
```

🔹 **Saída:**

```python
Produto da transposta com a identidade:
 [[3. 3. 3. 3.]
 [3. 3. 3. 3.]]
```


🔹 **Explicações**:

* `np.full((4,2), 3)` cria uma matriz 4x2 com todos os elementos iguais a 3.
* `np.eye(4)` cria uma matriz identidade 4x4, com 1 na diagonal principal e 0 nos demais elementos.
* `matriz3.T` retorna a transposta da matriz 4x2, que passa a ser 2x4.
* `@` realiza o produto matricial (dot product) entre a transposta e a identidade.




8. Realize as seguintes operações:

* Crie uma nova matriz de valores inteiros de 25 até 49 com dimensionalidade (5,5).

```python
matriz_inteiros = np.arange(25, 50).reshape(5, 5)
print ("Matriz 5x5 de inteiros:\n", matriz_inteiros)
```

🔹 **Saída:**

```python
Matriz 5x5 de inteiros:
 [[25 26 27 28 29]
 [30 31 32 33 34]
 [35 36 37 38 39]
 [40 41 42 43 44]
 [45 46 47 48 49]]
```



* Crie uma nova matriz com valores uniformemente espaçados entre 0 e 1 e defina a sua dimensionalidade em (5,1).

```python
matriz_uniforme = np.linspace(0, 1, 5).reshape(5, 1)
print ("Matriz 5x1 de valores uniformes:\n", matriz_uniforme)
```

🔹 **Saída:**

```python
Matriz 5x1 de valores uniformes:
 [[0.  ]
 [0.25]
 [0.5 ]
 [0.75]
 [1.  ]]
```

* Concatene horizontalmente as duas matrizes criadas anteriormente.

```python
matriz_concatenada = np.hstack((matriz_inteiros, matriz_uniforme))
print ("Matriz concatenada 5x6:\n", matriz_concatenada)
```

🔹 **Saída:**

```python
Matriz concatenada 5x6:
 [[25.   26.   27.   28.   29.    0.  ]
 [30.   31.   32.   33.   34.    0.25]
 [35.   36.   37.   38.   39.    0.5 ]
 [40.   41.   42.   43.   44.    0.75]
 [45.   46.   47.   48.   49.    1.  ]]
```

🔹 **Explicações**:

* `np.arange(25, 50)` gera números inteiros de 25 até 49 (50 não incluído).
* `.reshape(5,5)` transforma em uma matriz 5x5.
* `np.linspace(0, 1, 5)` gera 5 valores igualmente espaçados entre 0 e 1.
* `.reshape(5,1)` transforma em uma matriz coluna.
* `np.hstack((A, B))` concatena horizontalmente, criando uma matriz de 5 linhas e 6 colunas.



9. Crie uma nova matriz com dimensionalidade (5,1) com números uniformemente espaçados utilizando um espaço logarítmico ao invés de um espaço linear.

```python
matriz_log = np.logspace(0, 1, 5).reshape(5, 1)

print("Matriz 5x1 com espaço logarítmico:\n", matriz_log)
```

🔹 **Saída:**

```python
Matriz 5x1 com espaço logarítmico:
 [[ 1.        ]
 [ 1.77827941]
 [ 3.16227766]
 [ 5.62341325]
 [10.        ]]
```

🔹 **Explicações**:

* `np.logspace(start, stop, num)` gera num valores entre `10**start` e `10**stop`.
* `.reshape(5,1)` transforma em uma matriz coluna (5 linhas, 1 coluna).


10. Crie uma função que receba um array e adicione uma borda composta de zeros nos quatro lados do array. Utilize o array resultante da questão anterior para testar o método criado.

* Podemos criar uma função que usa `np.pad` do NumPy para adicionar uma borda de zeros ao redor de um array:

```python
def adicionar_borda_zeros(array):
    return np.pad(array, pad_width=1, mode='constant', constant_values=0)

matriz_com_borda = adicionar_borda_zeros(matriz_log)
print ("Array com borda de zeros:\n", matriz_com_borda)
```

🔹 **Saída:**

```python
Array com borda de zeros:
 [[ 0.          0.          0.        ]
 [ 0.          1.          0.        ]
 [ 0.          1.77827941  0.        ]
 [ 0.          3.16227766  0.        ]
 [ 0.          5.62341325  0.        ]
 [ 0.         10.          0.        ]
 [ 0.          0.          0.        ]]
```

* `np.pad` é muito flexível: você pode definir largura da borda, valor da borda `(constant_values)` e até outros modos, como `edge` ou `reflect`.


11. Crie um array de 36 números aleatórios oriundos de uma distribuição normal. Exiba o valor máximo, mínimo, a média e o desvio padrão desse array.

```python
# cria um array de 36 números aleatórios com distribuição normal padrão (média=0, desvio=1)
array_normal = np.random.randn(36)

print ("Máximo:", np.max(array_normal))
print ("Mínimo:", np.min(array_normal))
print ("Média:", np.mean(array_normal))
print ("Desvio padrão:", np.std(array_normal))
```

🔹 **Saída:**

```python
Máximo: 2.439216155649339
Mínimo: -1.9467946915363594
Média: 0.11582862261281328
Desvio padrão: 0.90313287390376
```


🔹 **Explicações**:

* `np.random.randn(36)` gera 36 números aleatórios da distribuição normal padrão.
* `np.max()` e `np.min()` retornam os valores máximo e mínimo.
* `np.mean()` calcula a média.
* `np.std()` calcula o desvio padrão, que indica a dispersão dos valores em relação à média.
* Você pode ajustar a média e o desvio padrão com `np.random.normal(loc=média, scale=desvio, size=36)` se quiser valores diferentes da normal padrão.



---

**Observação:** Este repositório é de caráter **educacional** e serve como documentação de estudo e prática.
