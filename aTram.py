tram = int(input())
passenger = []

def greater_than_2(arr):
    for row in arr:
        if len(row) > 2:
            return True
        else:
            return False
        
def return_data(arr):
    seats = 0
    list_value = []
    result = 0
    if arr[0][0] != 0 or arr[len(arr)-1][1] != 0:
        result = 0
    else:
        for i in range(len(arr)):
            seats = seats + arr[i][1] - arr[i][0]
            if seats >= 0:
                list_value.append(seats)
            else:
                result = 0
    if len(list_value) != 0:
        result = max(list_value)
    return result

for x in range(tram):
    #parse Integer for each value in the list created after inputing
    passenger.append([int(y) for y in input().split()])

if bool(greater_than_2(passenger)) == False:
    print(return_data(passenger))
else:
    print(0)
