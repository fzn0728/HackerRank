# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
mydict = {}
for line in range(n):
    info = raw_input().split(" ")
    score = map(float, info[1:])
    mydict[info[0]] = sum(score) / float(len(score))

print "%.2f" % round(mydict[raw_input()],2) 

# The split function and map function is very useful, mark.
# Also, learn how to deal with dictionary
