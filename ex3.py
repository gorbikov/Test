import numpy as np
import time

r1 = 0
r2 = 0
r3 = 0
counter = 0

for i in range(100):
    r = np.random.sample(10**8)
    counter += 1
    print(counter)

    # Создаёт массив индексов (0, 10, 20 ...) через arrange и выбирает эти индексы из изначального массива.
    a = r.copy()
    startTime = time.time()
    a[np.arange(0, len(a), 10)]
    r1 += (time.time() - startTime) * 10 ** 6
    print(r1)

    # Аналогично, только через take.
    a = r.copy()
    startTime = time.time()
    np.take(a, np.arange(0, len(a), 10), axis=0)
    r2 += (time.time() - startTime) * 10 ** 6
    print(r2)

    # Выбирается напрямую каждый десятый элемент.
    a = r.copy()
    startTime = time.time()
    a[::10]
    r3 += (time.time() - startTime) * 10 ** 6
    print(r3)

print('Result 1: ' + str(round(r1/counter, 0)) + 'ns')
print('Result 2: ' + str(round(r2/counter, 0)) + 'ns')
print('Result 3: ' + str(round(r3/counter, 0)) + 'ns')

# Самый быстрый результат: 3 > 1 > 2, но 2 и 1 очень похожи.



