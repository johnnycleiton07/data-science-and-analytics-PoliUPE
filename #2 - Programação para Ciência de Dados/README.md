###### PT

# Programação para Ciência de Dados

Disciplina voltada à introdução e aplicação da programação em Python para ciência de dados, abordando desde conceitos básicos da linguagem até o uso de bibliotecas específicas como NumPy, Pandas e Matplotlib. A avaliação será composta por duas listas de exercícios práticas.

---

## Revisão Básica de Python



<div align="center">

### Operadores Aritméticos
  
| Operador | Descrição | Exemplo | Resultado |
|-----------|------------|----------|------------|
| `+` | Adição: soma valores | `5 + 3` | `8` |
| `-` | Subtração: subtrai valores | `10 - 4` | `6` |
| `*` | Multiplicação: multiplica valores | `7 * 2` | `14` |
| `/` | Divisão: divide valores (resultado em float) | `9 / 2` | `4.5` |
| `//` | Divisão inteira: descarta as casas decimais | `9 // 2` | `4` |
| `%` | Módulo: retorna o resto da divisão | `9 % 2` | `1` |
| `**` | Exponenciação: eleva um número a uma potência | `3 ** 2` | `9` |
| `-x` | Negação: inverte o sinal de um número | `-5` | `-5` |
| `+x` | Valor positivo: mantém o número como positivo | `+5` | `5` |

</div>





<div align="center">

### Biblioteca Math
  
| Função / Constante | Descrição | Exemplo | Resultado |
|--------------------|------------|----------|------------|
| `math.sqrt(x)` | Retorna a raiz quadrada de `x` | `math.sqrt(9)` | `3.0` |
| `math.pow(x, y)` | Retorna `x` elevado a `y` (equivalente a `x**y`) | `math.pow(2, 3)` | `8.0` |
| `math.pi` | Constante π (pi) | `math.pi` | `3.141592653589793` |
| `math.e` | Constante do número de Euler | `math.e` | `2.718281828459045` |
| `math.ceil(x)` | Arredonda `x` para cima | `math.ceil(4.3)` | `5` |
| `math.floor(x)` | Arredonda `x` para baixo | `math.floor(4.7)` | `4` |
| `math.sin(x)` | Seno de `x` (em radianos) | `math.sin(math.pi/2)` | `1.0` |
| `math.cos(x)` | Cosseno de `x` (em radianos) | `math.cos(0)` | `1.0` |
| `math.tan(x)` | Tangente de `x` (em radianos) | `math.tan(math.pi/4)` | `1.0` |
  
</div>





<div align="center">

### Operadores Relacionais
  
| Operador | Descrição | Exemplo | Resultado |
|-----------|------------|----------|------------|
| `==` | Igual a — verifica se dois valores são iguais | `5 == 5` | `True` |
| `!=` | Diferente de — verifica se dois valores são diferentes | `5 != 3` | `True` |
| `>` | Maior que | `7 > 4` | `True` |
| `<` | Menor que | `3 < 8` | `True` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `2 <= 3` | `True` |

</div>




<div align="center">

### Operadores Lógicos
  
| Operador | Descrição | Exemplo | Resultado |
|-----------|------------|----------|------------|
| `and` | Retorna `True` se **ambas** as condições forem verdadeiras | `(5 > 2) and (3 < 4)` | `True` |
| `or` | Retorna `True` se **pelo menos uma** condição for verdadeira | `(5 > 10) or (3 < 4)` | `True` |
| `not` | Inverte o valor lógico da expressão | `not (5 > 2)` | `False` |

</div>



<div align="center">

#### Tabela Verdade dos Operadores Lógicos em Python
  
| A | B | `A and B` | `A or B` | `not A` |
|---|---|------------|-----------|----------|
| True  | True  | True  | True  | False |
| True  | False | False | True  | False |
| False | True  | False | True  | True  |
| False | False | False | False | True  |

</div>




<div align="center">

### Métodos de String em Python
  
| Método | Descrição | Exemplo | Resultado |
|---------|------------|----------|------------|
| `upper()` | Converte todos os caracteres para maiúsculas | `"python".upper()` | `"PYTHON"` |
| `lower()` | Converte todos os caracteres para minúsculas | `"PyThOn".lower()` | `"python"` |
| `title()` | Converte a primeira letra de cada palavra em maiúscula | `"curso de python".title()` | `"Curso De Python"` |
| `capitalize()` | Converte apenas a primeira letra da string em maiúscula | `"python é legal".capitalize()` | `"Python é legal"` |
| `strip()` | Remove espaços em branco no início e no fim | `"  texto  ".strip()` | `"texto"` |
| `replace(a, b)` | Substitui um trecho da string por outro | `"olá mundo".replace("mundo", "Python")` | `"olá Python"` |
| `split()` | Divide a string em uma lista de palavras | `"a b c".split()` | `["a", "b", "c"]` |
| `join()` | Junta elementos de uma lista em uma única string | `" ".join(["Python", "é", "legal"])` | `"Python é legal"` |
| `find()` | Retorna o índice da primeira ocorrência de um trecho | `"Python".find("t")` | `2` |
| `count()` | Conta quantas vezes um trecho aparece | `"banana".count("a")` | `3` |
| `startswith()` | Verifica se a string começa com um trecho | `"Python".startswith("Py")` | `True` |
| `endswith()` | Verifica se a string termina com um trecho | `"Python".endswith("on")` | `True` |
| `len()` | (função, não método) Retorna o tamanho da string | `len("Python")` | `6` |

</div>




<div align="center">

### Indexação em Strings no Python
  
|           Caractere |  P  |  Y  |  T  |  H  |  O  |  N  |
| ------------------: | :-: | :-: | :-: | :-: | :-: | :-: |
| **Índice positivo** |  0  |  1  |  2  |  3  |  4  |  5  |
| **Índice negativo** |  -6 |  -5 |  -4 |  -3 |  -2 |  -1 |

</div>



<div align="center">

#### Exemplos de Acesso e Fatiamento (Slicing)
  
| Expressão     | Resultado  | Explicação                |
| ------------- | ---------- | ------------------------- |
| `texto[0]`    | `'P'`      | Primeiro caractere        |
| `texto[-1]`   | `'N'`      | Último caractere          |
| `texto[1:4]`  | `'YTH'`    | Do índice 1 até o 3       |
| `texto[:3]`   | `'PYT'`    | Do início até o índice 2  |
| `texto[3:]`   | `'HON'`    | Do índice 3 até o fim     |
| `texto[::2]`  | `'PTO'`    | Pula de 2 em 2 caracteres |
| `texto[::-1]` | `'NOHTYP'` | Inverte a string          |

</div>




<div align="center">

### Principais Operações com Listas em Python

| Método / Operação | Descrição | Exemplo | Resultado |
|--------------------|------------|----------|------------|
| `append(x)` | Adiciona o elemento `x` ao final da lista | `lista.append(4)` | `[1, 2, 3, 4]` |
| `insert(i, x)` | Insere o elemento `x` na posição `i` | `lista.insert(1, 10)` | `[1, 10, 2, 3]` |
| `extend(iterável)` | Adiciona vários elementos de um iterável (ex: outra lista) | `lista.extend([4, 5])` | `[1, 2, 3, 4, 5]` |
| `remove(x)` | Remove a **primeira ocorrência** de `x` | `lista.remove(2)` | `[1, 3, 4]` |
| `pop([i])` | Remove e retorna o elemento da posição `i` (ou o último, se não informado) | `lista.pop()` | `[1, 2]` |
| `clear()` | Remove **todos** os elementos da lista | `lista.clear()` | `[]` |
| `index(x)` | Retorna o índice da **primeira ocorrência** de `x` | `lista.index(3)` | `2` |
| `count(x)` | Conta quantas vezes `x` aparece na lista | `lista.count(2)` | `1` |
| `sort()` | Ordena a lista **in-place** (modifica a original) | `lista.sort()` | `[1, 2, 3]` |
| `sorted(lista)` | Retorna uma **nova lista ordenada** (não altera a original) | `sorted([3,1,2])` | `[1, 2, 3]` |
| `reverse()` | Inverte a ordem dos elementos **in-place** | `lista.reverse()` | `[3, 2, 1]` |
| `len(lista)` | Retorna o número de elementos da lista | `len([1, 2, 3])` | `3` |
| `in` | Verifica se um elemento está presente na lista | `3 in [1, 2, 3]` | `True` |
| `+` | Concatena listas | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]` |
| `*` | Repete os elementos da lista | `[1, 2] * 2` | `[1, 2, 1, 2]` |
| `sum(lista)` | Retorna a soma de todos os elementos numéricos da lista | `sum([10, 20, 30])` | `60` |

</div>




<div align="center">

### Operações com Tupla
  
| Função / Método | Descrição | Exemplo | Resultado |
|------------------|------------|----------|------------|
| `dir(objeto)` | Lista todos os métodos e atributos disponíveis de um objeto (tupla / lista) | `dir(tuple)` | Retorna métodos como `count`, `index` |
| `tuple(iterável)` | Converte outro tipo de dado (lista, string, etc.) em tupla | `tuple([1, 2, 3])` | `(1, 2, 3)` |

</div>


<div align="center">
  
### Métodos Exclusivos de Dicionários em Python

| Método | Descrição | Exemplo | Resultado |
|---------|------------|----------|------------|
| `dict.keys()` | Retorna uma *view* com todas as chaves do dicionário | `d = {'a':1, 'b':2}; d.keys()` | `dict_keys(['a', 'b'])` |
| `dict.values()` | Retorna uma *view* com todos os valores do dicionário | `d.values()` | `dict_values([1, 2])` |
| `dict.items()` | Retorna pares `(chave, valor)` | `d.items()` | `dict_items([('a', 1), ('b', 2)])` |
| `dict.get(chave, padrão)` | Retorna o valor de uma chave, ou o padrão se a chave não existir | `d.get('c', 0)` | `0` |
| `dict.update(outro_dict)` | Atualiza o dicionário com pares de outro dicionário | `d.update({'c':3})` | `{'a':1, 'b':2, 'c':3}` |
| `dict.pop(chave[, padrão])` | Remove a chave especificada e retorna o valor | `d.pop('a')` | `1` |
| `dict.popitem()` | Remove e retorna o **último** par inserido | `d.popitem()` | `('b', 2)` |
| `dict.clear()` | Remove todos os itens do dicionário | `d.clear()` | `{}` |
| `dict.copy()` | Retorna uma cópia rasa (shallow copy) do dicionário | `d.copy()` | `{'a':1, 'b':2}` |
| `dict.fromkeys(seq[, valor])` | Cria um novo dicionário com chaves de uma sequência e um mesmo valor | `dict.fromkeys(['x', 'y'], 0)` | `{'x':0, 'y':0}` |
| `dict.setdefault(chave[, valor])` | Retorna o valor da chave, ou define com o valor padrão se não existir | `d.setdefault('c', 3)` | `3` |

</div>


<div align="center">
  
#### Estruturas de Controle de Fluxo no Python

| Comando | Descrição | Exemplo de Uso |
|----------|------------|----------------|
| `break` | Interrompe imediatamente o loop mais interno (for ou while) | `for i in range(5): if i == 3: break` |
| `continue` | Pula o restante do bloco atual e vai para a próxima iteração do loop | `for i in range(5): if i == 2: continue` |
| `pass` | Não faz nada — usado como placeholder em blocos vazios | `if condicao: pass` |
| `return` | Encerra a execução de uma função e retorna um valor | `def soma(a,b): return a + b` |
| `yield` | Retorna um valor **sem encerrar** a função (gera um iterador) | `def gen(): yield 1; yield 2` |
| `raise` | Lança uma exceção (erro) de forma explícita | `raise ValueError("Erro intencional")` |
| `else` (em loops) | Executa um bloco **após** o loop terminar normalmente (sem `break`) | `for i in range(3): print(i) else: print("Fim")` |

</div>


<div align="center">

#### List Comprehension

</div>

**Definição:**  
List Comprehension é uma forma concisa e eficiente de criar listas em Python. Ela substitui loops `for` tradicionais, tornando o código mais legível e compacto. A estrutura básica é:

```python
[expressão for item in iterável if condição]
```

Exemplo 1: criar uma lista com números de 0 a 9

```python
# Forma tradicional
lista = []
for i in range(10):
    lista.append(i)

# Usando List Comprehension
lista = [i for i in range(10)]
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Exemplo 2: criar uma lista com os quadrados dos números de 0 a 4

```python
# Forma tradicional
quadrados = []
for i in range(5):
    quadrados.append(i ** 2)

# Usando List Comprehension
quadrados = [i ** 2 for i in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]
```








---
### Exercícios

#### Introduzindo Operações Básicas com Tipos Numéricos e Booleanos

1 - A expressão a ser computada é:

$$
a^{2} + \frac{3}{4} \times b \times 987 \left( c - \frac{10^{-9}}{\sqrt{0.5^{3}}} \right)
$$

Assuma que:
- \( a = 2 \)
- \( b = 4 \)
- \( c = 8 \)

```python
import math

a = 2
b = 4
c = 8

resultado = a**2 + (3/4) * b * 987 * (c - (10**-9) / math.sqrt(0.5**3))
print(resultado)
```

2 - Armazene em uma variável o resto da divisão da expressão anterior por 23691.

```python
# usando o operador aritmético de módulo que retorna o resto da divisão
resto = resultado % 23691

print (resto)
```


3 - Cheque se a saída do resto da divisão é ***i) igual a 1***, ***ii) maior que 1***, ***iii) menor ou igual que 1*** e ***iv) diferente de 1***.

```python
# apenas usando operadores relacionais
print (resto == 1)
print (resto > 1)
print (resto <= 1)
print (resto != 1)
```

4 - Escreva a seguinte expressão booleana **(A + B) . (¬B . A)**.
- Defina *A* como True e *B* como False
- "+" indica uma operação  OR 
- "." indica uma operação AND 
- ''¬'' indica uma operação de negação (NOT)

```python
a = True
b = False

booleano = (a or b) and (not(b and a))
print (booleano)
```



#### Introduzindo Operações com Strings

5 - Defina uma variável com o valor *"hello wORld"* e reproduza as seguintes saídas: 
- "Hello World"
- "hello world"
- "HELLO WORLD"

```python
hello_world = "hello wORld"

print (hello_world.title())
print (hello_world.lower())
print (hello_world.upper())
```


6 - Dada a seguinte frase " *Esse é o seu primeiro tweet.* ", remova os espaços em branco das extremidades. Em seguida, substitua a palavra *'primeiro'* por *'segundo'*.

```python
frase = " Esse é o seu primeiro tweet "
frase_sem_espaco = frase.strip()
frase_final = frase_sem_espaco.replace("primeiro", "segundo")

print (frase_final)
```

7 - Fazendo uso do resultado da questão anterior, exiba a quantidade de ocorrências da palavra *'segundo'* e em seguida a quantidade de caracteres *'s'*.

```python
count_segundo = frase_final.count("segundo")
count_s = frase_final.count("s")

print (f"A palavra segundo aparece {count_segundo} vez(es)")
print (f"A letra S aparece {count_s} vez(es) na frase")
```

8 - Concatene duas variáveis do tipo strings com valores arbitrários e exiba o resultado.

```python
fruta = "maçã"
cor = "verde"

resultado = fruta + " " + cor
print (resultado)
```

9 - Utilize a indexação e exiba apenas do segundo ao quarto caractere da variável do tipo string resultante da questão imediatamente anterior.

```python
print (resultado[1:4])
```


10 - Exiba a string *"Mensagem: "* seguida pela string armazenada na variável *msg* definida abaixo. Dica: utilize a função format() ou *f-string*.

```python
msg = "This is your first tweet."

#f-string
print (f"Mensagem: {msg}")

#format()
print ("Mensagem: {}".format(msg))
```


11 - Reproduza as próximas três mensagens a partir das variáveis definidas na célula de código.
- **Mensagem**: Definir uma string com três aspas simples permite construir textos com quebra de linha automática.
```python
tipo_var = "string"
qtd = "três"

# Insira a resposta abaixo.
print (f"Definir uma {tipo_var} com {qtd} aspas simples permite construir textos com quebra de linha automática")
print ("Definir uma {} com {} aspas simples permite construir textos com quebra de linha automática".format(tipo_var, qtd))
```

- **Mensagem**:  O número pi é aproximadamente 3.14
```python
pi = 3.14159
# Insira a resposta abaixo.

# f-string
print (f"O número pi é aproximadamente {pi:.2f}")

#  format()
print ("O número pi é aproximadamente {:.2f}".format(pi))
```
  
- **Mensagem**: O meu nome é [*receber string via input*] e eu tenho [*receber inteiro via input*] anos.
```python
# Insira a resposta abaixo.
nome = (input("nome: "))
idade = (input("idade: "))

print (f"O meu nome é {nome} e eu tenho {idade} anos")
print ("O meu nome é {} e eu tenho {} anos".format(nome, idade))
```



#### Introduzindo Estruturas de Dados

12 - Realize as seguintes operações:

1. Crie uma lista vazia.
2. Adicione três elementos do tipo inteiro ao final da lista (*o método para adição de novos elementos em uma lista atua de forma in-place, portanto, basta invocá-lo.*).
3. Adicione um novo elemento na segunda posição da lista (*método in-place).
4. Exiba a soma dos quatro elementos (*python já possui uma função built-in para esssa operação*.)
5. Re-assinale o elemento da terceiro posição com um valor do tipo float.
6. Repita o passo 4.
7. Inverta os elementos da lista atual. (*função para inversão é in-place*)
8. Re-ordene os elementos da lista.
9. Armazene uma nova lista em uma variável qualquer com 2 números inteiros.
10. Concatena a nova lista criada com a lista resultante do passo 7.
11. Exiba o valor máximo e mínimo da resultante do passo anterior.

```python
# Insira a resposta abaixo.

#1
lista = []

#2
lista.append(1)
lista.append(2)
lista.append(3)

#3
lista.insert(1, 5)

#4
print ("Soma dos elementos:", sum(lista))

#5
lista[2] = 25.5

#6
print ("Soma atualizada:", sum(lista))

#7
lista.reverse()
print ("Lista invertida:", lista)

#8
lista.sort()
print ("Lista ordenada:", lista)

#9
nova_lista = [10, 20]

#10
lista_final = lista + nova_lista
print ("Lista concatenada:", lista_final)

#11
print ("Valor máximo:", max(lista_final))
print ("Valor mínimo:", min(lista_final))
```

13 - Converta a string definida abaixo em uma lista de palavras, armazene a lista em uma variável.

```python
frase = "Formação de Recursos Humanos Qualificados em Inteligência Artificial"

# Insira a resposta abaixo.
print (frase.split())
```

14 - Verifique se a palavra "Humanos" está contida na lista de palavras criada anteriormente. Exiba True ou False para indicar a resposta.

```python
print ("Humanos" in frase)
```


15 - Crie automaticamente uma lista contendo 50 elementos de valor 3 e armazene-a em uma variável. Dica: utilize o operador de multiplicação.

```python
lista = [3] * 50

print (lista)
```


#### Tuplas


16 - Converta a lista resultante da primeira questão sobre listas para uma tupla e exiba o tipo de dados do objeto criado. Após realizar o casting, utilize a indexação para exibir todos os elementos com exceção do primeiro e último.

```python
tupla = tuple(lista_final)
print (type(tupla))

# slicing para pegar do segundo elemento até o penúltimo
print (tupla[1:-1])
```

17 - Exiba os atributos/métodos disponíveis a partir dos objetos do tipo lista e tuple utilizados na questão anterior.

```python
print("Métodos para listas:")
print(dir(lista_final))

print("\nMétodos para tuplas:")
print(dir(tupla))
```


18 - Crie uma tupla contendo 5 números inteiros quaisquer. Em seguida, exiba o valor máximo e o valor mínimo da tupla criada.

```python
nova_tupla = (1, 2, 3, 4, 5)
print (f"Valor máximo da Tupla: {max(nova_tupla)}")
print (f"Vamor mínimo da Tupla: {min(nova_tupla)}")
```


#### Dicionários


19 - A partir do dicionário inicializado abaixo com quatro items, adicione três novos items com chaves "three", "four" e "five" e valores "três", "quatro" e "cinco".

```python
my_dict = {}
my_dict["one"] = "um"
my_dict["two"] = "dois"
my_dict[(1,2)] = ["um","dois"]
my_dict[1.3] = "um ponto três"

# adicionando novos
my_dict["three"] = "três"
my_dict["four"] = "quatro"
my_dict["five"] = "cinco"
```

20 - A partir do dicionário definido anteriormente, remova o item ("one", "um") do dicionário.

```python
my_dict.pop("one")

print (my_dict)
```


21 - A partir do dicionário definido anteriormente, realize as seguintes operações ordenadamente.

1. Exiba a quantidade de items do dicionário.
2. Gere automaticamente uma lista contendo as chaves do dicionário.
3. Gere automaticamente uma lista contendo os valores do dicionário.
4. Gere automaticamente uma lista composta por tuplas do tipo (chave, valor).
5. Remova os items cuja chaves são (1,2) e 1.3.
6. Exiba o dicionário final

```python
# Passo 1
print (f"O dicionário possui {len(my_dict)} itens")

# Passo 2
my_dict_keys = list(my_dict.keys())
print (f"Lista de chaves: {my_dict_keys}")

# Passo 3
my_dict_values = list(my_dict.values())
print (f"Lista de valores: {my_dict_values}")

# Passo 4
my_dict_items = list(my_dict.items())
print (f"lista de tuplas: {my_dict_items}")

# Passo 5
my_dict.pop((1,2))
my_dict.pop(1.3)


# Passo 6
print("Dicionário final:", my_dict)
```


22 - A partir dos dicionários 'en' e 'pt_br' definidos abaixo, crie um terceiro dicionário denominado 'translator' cujas chaves são, respectivamente, 'en' e 'pt_br' e os valores sejam os dicionários correspondentes. Exiba o dicionário criado.

```python
pt_br = {1:"um", 2:"dois", 3:"tres"}
en = {1:"one", 2:"two", 3:"three"}

translator = {"pt_br":pt_br, "en":en}
print (translator)
```


#### Estruturas de Decisão

23 - Utilize estruturas de decisão se-senão para construir um script que simule a árvore de decisão disposta na figura abaixo. Para cada nó da árvore, o usuário deve fornecer um valor a ser armazenado em uma variável e utilizado para verificar o fluxo que deve ser seguido até atingir uma das folha, exibindo algum dos valores "Opção 1", "Opção 2" ou "Opção 3".

<div align="center">
  
| ![Árvore de Decisão](/assets/CursoPython_DecisionTree.png) |
|:--:|
| *Árvore de Decisão para questão 23* |

</div>

```python
# NÓ 1
x1 = float(input("x1: "))

if (x1 > 3.77):
  print ("Opção 1")

else:
  # NÓ 2
  x2 = float(input("x2: "))
  if (x2 > 0.5):
    # NÓ 3
    x3 = float(input("x3: "))
    if (x3 >= 0.78):
      print ("Opção 2")
    else:
      print ("Opção 1")

  else:
    # NÓ 4
    x4 = float(input("x4: "))
    if (x4 < 0.5) and (x4 > 0.25):
      print ("Opção 1")
    elif (x4 == 0.5):
      print ("Opção 3")
    elif (x4 > 0.5) or (x4 <= 0.5):
      print ("Opção 2")
```

#### Estruturas de Repetição (for (with range), while, list comprehension)

24 - Crie um programa que receba do usuário uma entrada referente a string *"Please, type 'q' to quit"*. Enquanto o usuário não digitar o caractere *'q'*, o programa deve exibir *"Sorry, try again."* e continuar solicitando a informação. Dica: utilize o comando break para interrupção.

```python
entrada = "a"

while entrada != "q":
  entrada = input("Please, type 'q' to quit: ")
  if (entrada == "q"):
    break
  else:
    print ("Sorry, try again")
```

25 - Crie um programa que imprima apenas os números ímpares entre 1 e 100.

```python
for i in range(101):
  if (i % 2) != 0:
    print (i)
```

26 - A partir da lista definida abaixo, crie uma nova lista contendo apenas os números negativos. Dica: considere utilizar o modo list comprehension.

```python
lista = [-6, 21, -22, 4, -17, -21, 22, -11, 3, 28]

# [expressão for item in iterável if condição]
lista_negativos = [num for num in lista if num < 0]
print (lista_negativos)
```





---

✍️ **Observação:** Este repositório é de caráter **educacional** e serve como documentação de estudo e prática.
