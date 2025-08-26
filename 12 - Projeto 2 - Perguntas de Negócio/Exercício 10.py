#10 (Desafio Nível Master Ninja das Galáxias) - Qual o Total de Vendas Por 
#Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 
#Demonstre tudo através de um único gráfico.

#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Agrupamento por categoria e subcategoria e cálculo da soma somente para variáveis numéricas
valores = df_dsa.groupby(['Categoria',
                          'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda', ascending = False).head(12)

#Conversão da coluna Valor_Venda em número inteiro e classificação por categoria
valores = valores[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()

#Dataframe com categorias e subcategorias
print(valores)

#Criação de outro dataframe somente com os totais por categoria
valores_categoria = valores.groupby('Categoria').sum(numeric_only = True).reset_index()

#Dataframe com categorias
print(valores_categoria)

#Função para converter os dados em valor absoluto
def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

#Lista de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

#Listas de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

#Plot

#Tamanho da figura
fig, ax = plt.subplots(figsize = (18, 12))

#Gráfico das categorias
p1 = ax.pie(valores_categoria['Valor_Venda'],
            radius = 1,
            labels = valores_categoria['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

#Gráfico de subcategorias
p2 = ax.pie(valores['Valor_Venda'],
            radius = 0.9,
            labels = valores['SubCategoria'],
            autopct = autopct_format(valores['Valor_Venda']),
            colors = cores_subcategorias,
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'),
            pctdistance = 0.53,
            rotatelabels = True)

#Limpa o centro do círculo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

#Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(valores['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas por Categoria e Top 12 SubCategorias')
plt.show()