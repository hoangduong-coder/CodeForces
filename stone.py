x = input()
stoneNum = int(x)
str = input()
taken = 0
def return_value(new_str,x):
    x = int(x)
    result = False
    if len(new_str) != x or x == 1:
        result = False
    else: 
        for i in range(len(new_str)):
            if new_str[i] not in "RGB":
                result = False
                break
        else:
            result = True
    return result

if return_value(str,stoneNum):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            taken += 1
else:
    taken = 0

print(taken)



