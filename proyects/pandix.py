import pandas as pd
data= {
    'Nombre': ['juan','maria','pedro'],
    'Edad': [20,30,25],
    'Ciudad': ['Madrid','Bogota','Medellin']
}
df = pd.DataFrame(data)
print(df)
print(df.shape)

#print(df.head())
print(df['Nombre'].values)
print(df[df['Edad']>20])
print(df.loc[df['Edad'] > 20, ['Nombre', 'Edad']])
df['Genero'] = ['M','F','M']
df['Genero2'] = ['B','NB','Q']
print(df)
print(df.loc[df['Edad'] > 20, ['Nombre', 'Genero']])
df.drop('Genero2',axis=1,inplace=True)#axis 1 elimina la columna relacionada con el nombre y axis=0 la fila con ese nombre
print(df)
df.rename(columns={'Nombre':'Name'},inplace=True)
print(df)
print(df.describe())
print(df.groupby('Ciudad')['Edad'].mean())
print(df.sort_values(by='Edad', ascending=True))

#import matplotlib.pyplot as plt
#df['Edad'].hist()
#plt.xlabel('Edad')
#plt.ylabel('Frecuencia')
#plt.title('Histograma de Edades')
#plt.show()