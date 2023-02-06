import pandas as pd
from sklearn import tree

x = pd.DataFrame([1, 2, 3, 4, 5])
y = pd.DataFrame([1, 4, 9, 16, 25])

model = tree.DecisionTreeClassifier(criterion="entropy")

model.fit(x, y)

print(model.score(x, y))
print(model.get_depth())

#При глубине 3 включительно - достигается нулевая ошибка.