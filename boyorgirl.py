str = input()
# if len(str) <= 10**3:
#     print(str[0].capitalize(),str[1:],sep='')
str1 = str.upper()
def check_capital(stra, strb):
    result = False
    for i in range(len(str)):
        if str[i] == str1[i]:
            result = True
    return result

if bool(check_capital(str,str1)) == False:
    character = [str[0]]
    x = 1
    for i in range(len(str)):
        if str[i] not in character:
            x += 1
            character.append(str[i])
    if x % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')