import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from myConvexHull import ConvexHull
from sklearn import datasets

print("masukkan data yang ingin anda gunakan: \n1. iris \n2. wine\n")
pilihanData = int(input("masukkan input : "))

if(pilihanData == 1):
    data = datasets.load_iris()
    print("1. Sepal Width VS Sepal Length \n2. Petal Width VS Petal Length")
    pilihan = int(input("masukkan perbandingan : "))
    if(pilihan == 1):
        t = 0
        u = 1
    elif(pilihan == 2):
        t = 2
        u = 3

if(pilihanData == 2):
    data = datasets.load_wine()
    print("1. Malic Acid VS Color Intensity \n2. Alcohol VS Flavanoids")
    pilihan = int(input("masukkan perbandungan: "))
    if(pilihan == 1):
        t = 1
        u = 9
    elif(pilihan == 2):
        t = 0
        u = 6

df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(f'{data.feature_names[t].title()} vs {data.feature_names[u].title()}')
plt.xlabel(data.feature_names[t])
plt.ylabel(data.feature_names[u])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[t,u]].values
    bucket = bucket.tolist()
    hull = ConvexHull(bucket) #hasil implementasi convexHull
    bucket = np.array(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    x = [hull[len(hull)-1][0]]
    y = [hull[len(hull)-1][1]]
    for p in hull:
        x.append(p[0])
        y.append(p[1])
    plt.plot(x, y, colors[i])
    plt.legend()
plt.show()