# Instruções para executar os algoritimos

## Robot.py
Este comando irá gerar uma grade com 4 de largura, 4 de altura e 3 obstáculos aleatórios.

```python
python robot.py 4 4 3
```

O comando faz o mesmo que o anterior, porém, adiciona o resultado gerado em um arquivo tgf.

```python
python robot.py 4 4 3 > nome_do_arquivo.tgf
```

## graph.py
Lê um arquivo no formato TGF (Trivial Graph Format), que descreve a estrutura do grafo, e realiza uma busca no grafo a partir de um nó de partida até um nó de destino. O código utiliza heurísticas para determinar o melhor caminho a ser percorrido durante a busca. O resultado da busca é impresso, mostrando o caminho encontrado e as informações associadas a cada nó no caminho.

```python
python graph.py nome_do_arquivo.tgf
```

## Exemplo de um arquivo TGF gerado pelo robot.py
```python
1 (1,1)
2 (1,2)
5 (2,1)
6 (2,2)
7 (2,3)
8 (2,4)
10 (3,2)
11 (3,3)
12 (3,4)
13 (4,1)
15 (4,3)
16 (4,4)
#
1 5 (1,1)>(2,1)
1 2 (1,1)>(1,2)
2 1 (1,2)>(1,1)
2 6 (1,2)>(2,2)
5 1 (2,1)>(1,1)
5 6 (2,1)>(2,2)
6 2 (2,2)>(1,2)
6 5 (2,2)>(2,1)
6 10 (2,2)>(3,2)
6 7 (2,2)>(2,3)
7 6 (2,3)>(2,2)
7 11 (2,3)>(3,3)
7 8 (2,3)>(2,4)
8 7 (2,4)>(2,3)
8 12 (2,4)>(3,4)
10 6 (3,2)>(2,2)
10 11 (3,2)>(3,3)
11 7 (3,3)>(2,3)
11 10 (3,3)>(3,2)
11 15 (3,3)>(4,3)
11 12 (3,3)>(3,4)
12 8 (3,4)>(2,4)
12 11 (3,4)>(3,3)
12 16 (3,4)>(4,4)
15 11 (4,3)>(3,3)
15 16 (4,3)>(4,4)
16 12 (4,4)>(3,4)
16 15 (4,4)>(4,3)
```
