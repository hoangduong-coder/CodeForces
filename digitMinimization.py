def swap_and_delete(str):
  arr = list(map(int, str))
  if(len(arr) == 2):
    print(arr[1])
  else:
    print(min(arr))

case = int(input())
for _ in range (case):
  swap_and_delete(input())