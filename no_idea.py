#There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
arr = [int(x) for x in input().split()]
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])
count = [0 + 1 if x in A else 0-1 if x in B else 0 + 0 for x in arr]
print(sum(count))
