import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# # Упражнение 1
# y = np.array([432, 405, 373, 304, 273, 248, 220, 164])
# x = np.array([1.584, 1.575, 1.556, 1.5325, 1.525, 1.542, 1.5575, 1.6425])
# plt.plot(y, x, "r")
# plt.show()

#Упражнение 2
# val1 = np.random.normal(10,10,1000)
# val2 = np.random.normal(10,10,5000)
# val3 = np.random.normal(10,10,11000)
# fig, axes = plt.subplots( ncols=3, figsize=(15, 8))
# axes[0].hist(val1)
# axes[1].hist(val2)
# axes[2].hist(val3)
# plt.tight_layout()
# plt.show()


# Упражнение 3
# df = pd.read_csv("iris_data.csv")
# a = df["Species"]
# wid =set(a)
# w=[]
# for i in wid:
#     w.append(i)
# s=[]
# for i in w:
#     k=0
#     for i1 in a:
#         if i1==i:
#             k+=1
#     s.append(k)
# q = df["PetalLengthCm"]
# l=[]
# k1=0
# k2=0
# k3=0
# for i in q:
#     if i <1.2:
#         k1+=1
#     if 1.2<= i <=1.5:
#         k2+=1
#     if i>1.5:
#         k3+=1
# l.append(k1)
# l.append(k2)
# l.append(k3)
# fig = plt.figure(figsize = (10,8))
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
# ax1.pie(s, labels = w, autopct = '%1.1f%%')
# ax2.pie(l, labels = ["small", "medium", "large"], autopct = '%1.1f%%')
# plt.show()


# Упражнение 4
# df = pd.read_csv("iris_data.csv")
# l1 = sorted((list((df["SepalLengthCm"]))))
# l2 = sorted((list(df["PetalLengthCm"])))
# w1 = sorted(list(df["SepalWidthCm"]))
# w2 = sorted(list(df["PetalWidthCm"]))
# fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))
# axes[0,1].plot(l1, l2)
# axes[1,0].plot(l1, w1)
# axes[1,1].plot(l1, w2)
# axes[1,2].plot(l2, w1)
# axes[0,0].plot(l2, w2)
# axes[0,2].plot(w1, w2)
# plt.tight_layout()
# plt.show()


# Упражнение 5
# import matplotlib.dates as mdates
# df = pd.read_csv("BTC_data.csv")
# time = df["time"]
# clos = df["close"]
# day = [i[:10] for i in time ]
# plt.plot(day, clos)
# ax = plt.gca()
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=75))
# plt.gcf().autofmt_xdate()
# plt.show()

# Упражнение 6
import matplotlib.ticker as ticker
df = pd.read_csv("BTC_data.csv")
time = df["time"]
clos = df["close"]
day = [i[:10] for i in time ]
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8))
ax1.plot(day, clos)
x = np.arange(0, len(clos), 1)
z = np.polyfit(x, clos, 15)
p = np.poly1d(z)
y = p(x)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax2.plot(day, y)
ax2.xaxis.set_major_locator(ticker.MultipleLocator(50))
fig.subplots_adjust(hspace=0.4)
ax1.tick_params(axis='x', labelrotation=45)
ax2.tick_params(axis='x', labelrotation=45)
plt.show()


#Упражнение 8
# a=(np.random.randint(0,100,40)).tolist()
# b=(np.random.randint(0,100,40)).tolist()
# a1 =sorted([i for i in a if a.count(i)==1])
# b1 =sorted([i for i in b if b.count(i)==1])
# print(a1, b1)
# s=[]
# for i in a:
#     s.append(i)
# for i in b:
#     s.append(b)
# s1 = sorted([i for i in s if s.count(i)==1])
# print(s1)
# a1 = set(a)
# b1 = set(b)
# ab= a1|b1
# q=set()
# m1 = max(a)
# m2 =max(b)
# m = max(m1,m2)
# for i in range(0, m+1):
#     if i in a1 and i in b1:
#         q.add(i)
# print(sorted(q))

#Упражнение 7
# import string
# def count_words(filename):
#     word_count = {}
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
#             cleaned_line = line.translate(translator)
#             words = cleaned_line.lower().split()
#             for word in words:
#                 if word:
#                     word_count[word] = word_count.get(word, 0) + 1
#     sorted_words = sorted(word_count.items(), key=lambda x: (-x, x)) [1]
#     print("Топ-10 самых частых слов:")
#     for word, count in sorted_words[:10]:
#         print(f"{word} {count}")
# count_words('/usr/share/licenses/python/LICENSE')