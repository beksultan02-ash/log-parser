lst = [1, 2, 3, 4, 5]

tpl = tuple(lst)

print("Try to change first element of tuple:")
try:
    tpl[0] = int(input())

except TypeError:
    print("U cant change elements of tuple")

lst_1 = list(tpl)

print("Try to change first element of list: ")
try: 
    lst_1[0] = int(input())

except ValueError as e:
    print(f"Ur input is wrong, not integer: {e}")