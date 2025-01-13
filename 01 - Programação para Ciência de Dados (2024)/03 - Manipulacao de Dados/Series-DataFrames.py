import numpy as np
import pandas as pd

def celsiusToFahrenheit(vetor):
    return vetor * (9/5) + 32

# celsiusVetor = np.random.randint(0,11,10)
# celsiusVetor = np.random.rand(10)
# print(celsiusVetor)

# fahrenheitVetor = celsiusToFahrenheit(celsiusVetor)
# print(fahrenheitVetor)


# a3D = np.random.randint(1,11,(2,3,5))
# print(a3D)
# print(a3D.sum(axis=2))

# print(a3D)
# print(a3D.sum(axis=1))

# print(a3D)
# print(a3D.sum(axis=0))



# a3D = np.random.randint(1,11,(2,3,5))
# print(a3D)
# print(a3D.min(axis=2))

# print(a3D)
# print(a3D.min(axis=1))

# print(a3D)
# print(a3D.min(axis=0))

# percentiles = [98, 76.37, 55.55, 69, 88]
# first_subject = np.array(percentiles)
# print(first_subject.dtype.name)

# dataset = np.array(['paul', 'jacob', 'vince', 'paul', 'miky', 'larence', 'warren'])
# print(dataset == 'paul')



# s = pd.Series([0,1,2,3,4,5,6,7,8,9])

# print(s)



valores = np.arange(1, 73)
valores.shape = (12,6)

print (valores)

indexes = np.arange(1,13)
columns = np.array(['A','B','C','D','E','F'])
df = pd.DataFrame(valores, index=indexes, columns=columns)

print(df)

df["Subtotal1"] = df["A"] + df["C"] + df["E"]
print(df)

df["Subtotal2"] = df["B"] + df["D"] + df["F"]
print(df)

df["Total"] = df["Subtotal1"] + df["Subtotal2"]
print(df)

df.drop(['Subtotal1','Subtotal2'],axis=1,inplace=True)
print(df)

dfex3 = df.drop(['D','E','F','Total'],axis=1)
dfex3 = dfex3.drop(np.arange(1,9),axis=0)
print(dfex3)

somaColunas = np.array(df.sum(axis=0)).reshape(1,7)
dfSoma = pd.DataFrame(somaColunas,columns=np.array(df.columns))
df = pd.concat([df,dfSoma],ignore_index=True)
print(df)

print(df.iloc[9:,:3])
