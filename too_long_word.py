n = int(input())
if n>=1 and n<=100:
    for x in range(n):
        s = str(input(""))
        if(len(s) > 10):
            newStr = s[1:len(s)-1]
            result = s[0] + str(len(newStr)) + s[len(s)-1]
            print(result)
        else:
            print(s)