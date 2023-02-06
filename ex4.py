from itertools import permutations
import random
import numpy as np
import time

elementsInitial = ['a', 'c', 'd', 'x', 'z', 'e', 'b', 'df', 'g', 'd']

startTime = time.time()
elements = elementsInitial.copy()
permutation_2 = tuple(np.random.permutation(elements))
print('Result 1: ' + str(round((time.time() - startTime)*10**6, 0)) + 'ns')

startTime = time.time()
elements = elementsInitial.copy()
permutation_1 = random.choice(list(permutations(elements)))
print('Result 2: ' + str(round((time.time() - startTime)*10**6, 0)) + 'ns')

# Самый быстрый результат: 1 (permutation_2)