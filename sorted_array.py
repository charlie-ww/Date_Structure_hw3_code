# code from: https://www.tutorialspoint.com/python-inserting-item-in-sorted-list-maintaining-order
import random
import bisect
from openpyxl import Workbook
import numpy as np
import time




wb = Workbook()
ws = wb.active
ws['A1'] = '時間'



for a in range(20, 21):
    N = 2 ** 30 + 1
    n = 2 ** a
    A = list()

    random_list = np.random.randint(0, N, size=n)

#     start = time.time()
    for i in range(n):
        bisect.insort(A, random_list[i])
#     end = time.time()

#     print("use ", end-start, "seconds")
#     ws.append([end-start,a])

# wb.save("sortedarray_search.xlsx")


    start = time.time()
    for i in range(100000):
        num = random.randrange(N)
        bisect.bisect(A, num)
    end = time.time()
    print(a, "use ", end-start, "seconds")
    ws.append([a, end-start])
wb.save("sortedarray_search.xlsx")