# упражнение 1

# def f(n):
#     if n<=1:
#         return n
#     a=1
#     b=0
#     for i in range(n-1):
#         a,b=a+b, a
#     return a
# print(f(int(input())))

# Упражнение 2

# def factor(n, i=2):
#     while (i*i<=n):
#         if n%i:
#             i+=1
#         else:
#             return [i]+factor(n//i, i)
#     return [n]
#
# print(factor(int(input())))


# Упражнение 3

# def f(a, b):
#     if b == 0:
#         return 1, 0, a
#     x1, y1, d = f(b, a % b)
#     x = y1
#     y = x1 - (a // b) * y1
#     if x >= (b // 2):
#         x -= b
#         y += a
#     return x, y, d
#
# a,b = map(int, input().split())
# print(f(a, b))

#Упражнение 4

# a,b=input().split(" ")
# a=int(a)
# def f(a,b):
#     k=1
#     while k<a//2+1:
#         print(k*b)
#         k+=1
#     print(k*b)
#     while k!=0:
#         k-=1
#         print(k*b)
# print(f(a,b))

#Упражнение 5

# import numpy as np

# def create_spiral_matrix(n, m):
#     matrix = np.zeros((n, m), dtype=int)
#
#     top, bottom = 0, n - 1
#     left, right = 0, m - 1
#     num = 1
#
#     while top <= bottom and left <= right:
#         for col in range(left, right + 1):
#             matrix[top, col] = num
#             num += 1
#         top += 1
#
#         for row in range(top, bottom + 1):
#             matrix[row, right] = num
#             num += 1
#         right -= 1
#
#         if top <= bottom:
#             for col in range(right, left - 1, -1):
#                 matrix[bottom, col] = num
#                 num += 1
#             bottom -= 1
#
#         if left <= right:
#             for row in range(bottom, top - 1, -1):
#                 matrix[row, left] = num
#                 num += 1
#             left += 1
#
#     return matrix
#
# n, m = 4, 5
# spiral = create_spiral_matrix(n, m)
# print(spiral)
#
# row_indices = np.arange(1, n + 1).reshape(-1, 1)
# result = spiral * row_indices
#
# print(result)

# Упражнение 6

# import numpy as np
# x=np.array(list(map(float, input().split())))
# y = np.array(list(map(float, input().split())))
# def mnk (x,y):
#     n = len(x)
#     b = (n*np.sum(x*y) - np.sum(x) * np.sum(y)) / (n * np.sum(x*x)  -(np.sum(x))**2)
#     a = (np.sum(y) - b*np.sum(x))/ n
#     return a, b
# a,b = mnk(x,y)
# print(f"Коэффициенты: k = {a}, b = {b}")

#Упражнение 7 (только для систем решаемые методом Крамера)
# import numpy as np
#
# n,m = map(int, input().split())
# matrix= np.zeros((n,m-1))
# b = np.zeros((n, 1))
# for i in range(n):
#     a = list(map(int, input().split()))
#     matrix[i] = a[:-1]
#     b[i] = a[-1]
#
# determinant = np.linalg.det(matrix)
# xsol= [0] * (-1)
# for i in range(n):
#     x = np.copy(matrix)
#     x=x.T
#     y = b.T
#     x[i] = y
#     x = x.T
#     det = np.linalg.det(x)
#     num = float(det/determinant)
#     xsol.append(f"{num:.5f}")
#
# print(xsol)

#Упражнение 8
import numpy as np
n = int(input())
x = np.random.randint(-1000, 1000, n)
y = np.random.randint(-1000, 1000, n)


def mnk (x,y):
    n = len(x)
    b = (n*np.sum(x*y) - np.sum(x) * np.sum(y)) / (n * np.sum(x*x)  -(np.sum(x))**2)
    a = (np.sum(y) - b*np.sum(x))/ n
    return a, b
a,b = mnk(x,y)
print(f"Коэффициенты: a = {a}, b = {b}")