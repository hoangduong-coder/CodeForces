arr = list(map(int, input()))

def count_lucky_digits(a):
  digit_numbers=0
  for i in a:
    if i == 4 or i == 7:
      digit_numbers += 1
  if digit_numbers in [4, 7]:
    return True
  else:
    return False


if (count_lucky_digits(arr)):
  print("YES")
else:
  print("NO")
