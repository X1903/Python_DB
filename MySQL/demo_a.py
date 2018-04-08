# _*_ coding:utf-8 _*_
__author__ = 'Xbc'

# from collections import deque
#
#
# def search(lines, pattern, history):
#     previous_lines = deque(maxlen=history)
#     for i in lines:
#         if pattern in li:
#             yield li, previous_lines
#         previous_lines.append(li)

#查找最大最小的n个元素
# import heapq
# nums = [1,2,3,4,5,6,7]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1},
#               {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#               {'name': 'FB', 'shares': 200, 'price': 21.09},
#               {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#               {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#               {'name': 'ACME', 'shares': 75, 'price': 115.65}
#               ]
# cheap = heapq.nsmallest(3, portfolio, lambda s : s['price'])
# # print(cheap)
# expensive = heapq.nlargest(3, portfolio, lambda s : s['price'])
# heapq.heapify(nums)
# print(heapq.heappop(nums))

#1.5一个优先队列
# import heapq
#
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-int(priority), self._index, item))
#         self._index +=1
#
#     def pop(self):
#         return  heapq.heappop(self._queue)[-1]
#
# class Item:
#      def __init__(self, name):
#          self.name = name
#      def __repr__(self):
#          return 'Item({!r})'.format(self.name)
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# print(q.pop())

#1.6 字典中映射多个值
# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(1)
# for key in d:
#     print(key, d[key])
# print(d)
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(1)
# print(d)
# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('b', []).append(4)
# print(d)

# 1.7 字典排序
# from collections import OrderedDict
#
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['add'] = 3
# for key in d:
#     print(key, d[key])

#1.8 字典运算
# prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# prices_sort = sorted(zip(prices.values(), prices.keys()), reverse=True)
# print(max(prices_sort))
# print(min(prices_sort))
#zip是迭代器只能访问一次，可以对zip进行排序后，在进行操作

#1.9  查找两个字典的相同点
# a = { 'x' : 1, 'y' : 2, 'z' : 3 }
# b = { 'w' : 10, 'x' : 11, 'y' : 2 }
# print(a.keys() & b.keys())
# print(a.items() & b.items())
# c = {key:a[key] for key in a.keys() - {'z', 'b'}}
# print(c)

#1.10 删除元素并保持顺序
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
# #list append set add, set 有序，
# a= [1, 5, 3, 4, 6, 7, 7, 4, 5]
# print(list(dedupe(a)))

# def deque(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
# a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# # print(list(deque(a, key=lambda d: (d['x'], d['y']))))
# # print(list(deque(a, key=lambda d:d['x'])))
# print(list(deque(a, key=lambda d:d['y'])))
#1.11命名切片
# record = '....................100 .......513.25 ..........'
# cost = int(record[20:23])*float(record[31:37])
# print(cost)
# a1 = slice(20, 23)
# a2 = slice(31, 37)
# cost = int(record[a1])*float(record[a2])

#1.12 序列中出现次数最多的元素
# words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes',
#           'the', 'eyes', 'not', 'around', 'the',
#           'eyes', "don't", 'look', 'around',
#           'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]
# from collections import Counter
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print(top_three)
# print()

#1.13 通过某个关键字排序一个字典列表
# rows = [ {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#          {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#          {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#          {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]

# from operator import itemgetter
# rows_by_frame = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# print(rows_by_uid)
# rows_by_fname = sorted(rows, key=lambda r: r['fname'])
# print(rows_by_fname)

#3.14 排序不支持
# class User:
#     def __init__(self, user_id):
#         self.user_id = user_id
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
# def sort_notcompare():
    # users = [User(23), User(3), User(99)]
    # print(users)
    # print(sorted(users, key=lambda u :u.user_id))
# users = [User(23), User(3), User(99)]
# from operator import attrgetter
# a = sorted(users, key=attrgetter('user_id'))
# a = sort_notcompare()

#1.15 通过某个字段将记录分组
# rows = [ {'address': '5412 N CLARK', 'date': '07/01/2012'},
#          {'address': '5148 N CLARK', 'date': '07/04/2012'},
#          {'address': '5800 E 58TH', 'date': '07/02/2012'},
#          {'address': '2122 N CLARK', 'date': '07/03/2012'},
#          {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#          {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#          {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#          {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# from operator import itemgetter
# from itertools import groupby
#
# rows.sort(key=itemgetter('date'))
# for data, items in groupby(rows, key=itemgetter('date')):
#     print(data)
    # for i in items:
    #     print(' ', i)

#1.16 过滤系列元素
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# pos = (n for n in mylist if n >0)
# print(pos)
# for i in pos:
#     print(i)

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int (val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
# ivals = list(filter(is_int, values))
# print(ivals)

# 1.17 从字典中提取子集
prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
p1 = {key:value for key, value in prices.items() if value > 200}
# p1 = dict((key,value) for key, value in prices.items() if value > 20)
print(p1)

#1.18 映射名称到序列元素