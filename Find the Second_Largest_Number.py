# Enter your code here. Read input from STDIN. Print output to STDOUT
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i] # It is so powerful to use map(func,seq) and strip(), split() to fetch info from strings
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)

'''
# Another good idea
N = int(input())
num = map(int,raw_input().split())
print sorted(list(set(num)))[-2]
'''
