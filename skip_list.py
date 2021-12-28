import random
# code from: https://gist.github.com/sachinnair90/3bee2ef7dd3ff0dc5aec44ec40e2d127
from openpyxl import Workbook
import numpy as np
import time
from random import randint
copy = 0 # 計算平均 additional copy
maxhigh = 1 # 計算list個數

class SkipNode:
    """A node from a skip list"""

    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [None] * height


class SkipList:

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.maxHeight = 0

    def __len__(self):
        return self.len

    def find(self, elem, update=None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None

    def contains(self, elem, update=None):
        return self.find(elem, update) != None

    def randomHeight(self): # 正面機率0.5
        global copy
        global maxhigh
        height = 1
        while randint(1, 2) != 1:
            height += 1
            copy = copy+1
        maxhigh = max(maxhigh, height)
        return height

    def updateList(self, elem):
        update = [None] * self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def insert(self, elem):

        node = SkipNode(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def remove(self, elem):

        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1

    def printList(self):
        for i in range(len(self.head.next) - 1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print(x.next[i].elem)
                x = x.next[i]
            print('')

wb = Workbook()
ws = wb.active
ws['A1'] = '時間'

for a in range(10, 11):
    N = 2 ** 30 + 1
    n = 2 ** a
    A = SkipList()
    #ws.append(["2的", a])

    random_list = np.random.randint(0, N, size=n)

    start = time.time()
    for i in range(n):
        A.insert(random_list[i])
    end = time.time()

    ws.append([a, end-start])
# wb.save("skiplist_insert.xlsx")

    start = time.time()
    for i in range(100000):
        num = random.randrange(N)
        A.find(num)
    end = time.time()
    ws.append([a, end - start])
# wb.save("skiplist_search.xlsx")
    ws.append([copy/n])
# wb.save("SkipList_copy.xlsx")
    ws.append([maxhigh])
wb.save("SkipList_list.dat")
