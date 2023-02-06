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

sns.scatterplot(data=generatedDf, x='X', y='Y', hue='Color')
matplotlib.pyplot.show()

#KNN
from sklearn.neighbors import KNeighborsRegressor
regressor = KNeighborsRegressor(n_neighbors=5)
regressor.fit(generatedDf.drop(['Color'], axis=1), generatedDf['Color'])

resolution = 10

x_test=pd.DataFrame([np.array(range(resolution))/resolution-1.5, np.array(range(resolution))/resolution-1.5]).transpose()
print(x_test)


print(np.array(range(resolution), dtype=np.float32)/resolution)

# y_pred = regressor.predict(x_test)