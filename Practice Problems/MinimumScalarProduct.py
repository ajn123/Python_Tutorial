file  = open('text.txt')

testNum = int(file.readline())

for numberOfTests in range(testNum):
    vectorSize = int(file.readline())
    v1 = list(file.readline().split())
    v1 = [int(x) for x in v1]
    
    v2 = list(file.readline().split())
    v2 = [int(x) for x in v2]
    ans = 0
    
    """
    All logic here, to get the lowest multiplication value, 
    multiply the maximum of the vector by the highest of another
    to cancel out the high terms.  Then remove them from the 
    list.
    """
    while len(v1) != 0:
        ans += min(v1) * max(v2)
        v1.remove(min(v1))
        v2.remove(max(v2))
    
    print "Case #{}: {}".format(numberOfTests,ans) 
        