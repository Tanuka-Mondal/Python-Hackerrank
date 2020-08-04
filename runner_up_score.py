#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.


if __name__ == '__main__':
   
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))

    print (max(lis))      

    
