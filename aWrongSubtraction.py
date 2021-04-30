inputLine = input("")
newInput = inputLine.split()
x = int(newInput[0])
for i in range(int(newInput[1])):
    if(x%10 == 0):
        x /= 10
    else:
        x -= 1
if(x > 0):
    print(int(x))