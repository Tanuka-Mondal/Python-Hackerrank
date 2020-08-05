#You are given a two lists  and . Your task is to compute their cartesian product X.



from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))
