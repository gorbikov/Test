import matplotlib.pyplot
import numpy as np
import pandas as pd
import seaborn as sns

dotNumber = 2000
stDev=0.13

red = np.array([np.random.normal(0, 2*stDev, dotNumber), np.random.normal(3, 2.5*stDev, dotNumber), np.ones(dotNumber)*1])
green = np.array([np.random.normal(-1, stDev, dotNumber), np.random.normal(0, 4*stDev, dotNumber), np.ones(dotNumber)*2])
blue = np.array([np.random.normal(1, stDev, dotNumber), np.random.normal(0, 4*stDev, dotNumber), np.ones(dotNumber)*3])

generatedDf = pd.concat([pd.DataFrame(red).transpose(), pd.DataFrame(green).transpose(), pd.DataFrame(blue).transpose()], ignore_index='true')
generatedDf.columns = ['X', 'Y', 'Color']

#Оптимальный Байесовый классификатор
from sklearn.naive_bayes import GaussianNB
regressor = GaussianNB()
regressor.fit(generatedDf.drop(['Color'], axis=1), generatedDf['Color'])

#KNN
# from sklearn.neighbors import KNeighborsRegressor
# regressor = KNeighborsRegressor(n_neighbors=5)
# regressor.fit(generatedDf.drop(['Color'], axis=1), generatedDf['Color'])

resolution = 100
x_min = -1.5
x_max = 1.5
y_min = -2
y_max = 4

grid = np.meshgrid(np.arange(x_min, x_max, 1/resolution), np.arange(y_min, y_max, 1/resolution))
xx, yy = grid

predicted = regressor.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
matplotlib.pyplot.pcolormesh(xx, yy, predicted, cmap='autumn')
sns.scatterplot(data=generatedDf, x='X', y='Y', hue='Color')
matplotlib.pyplot.show()
print('Done')

#По итогу Оптимальный Байесовый - более выпуклый. Поэтому слева-направо: Байесовый, KNN, Tree.