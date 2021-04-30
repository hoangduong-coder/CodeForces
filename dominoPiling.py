sizeOfBoard = input()
sizeOfBoard = sizeOfBoard.split()
numSqr = int(sizeOfBoard[0])*int(sizeOfBoard[1])
i = 0
if numSqr % 2 == 0:
    while i < numSqr/2:
        i += 1
    print(i)
else:
    while i < numSqr/2 - 1:
        i += 1
    print(i)
