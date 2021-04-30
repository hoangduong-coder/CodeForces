n = int(input())
countFor1 = 0
success = 0
if n>=1 and n<=1000:
    for x in range(n):
        inputStr = str(input())
        newStr = inputStr.replace(" ","")
        for i in newStr:
            if i == "1": countFor1 = countFor1 + 1
        if countFor1 >= 2:
            success = success + 1
        countFor1 = 0
print(success)
