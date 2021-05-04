inputLine = int(input(""))
resultList = []
for x in range(inputLine):
    arr = list(map(int,input().split()))
    red = arr[0]
    blue = arr[1]
    d = arr[2]
    result = "YES" if max(red, blue) <= min(red,blue)*(d+1) else "NO"
    resultList.append(result)
for x in resultList:    
    print(x)
