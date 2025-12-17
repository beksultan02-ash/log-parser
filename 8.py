coor_1 = tuple(map(int, input().split()))
coor_2 = tuple(map(int, input().split()))

sum_1 = sum_2 = 0

for i in coor_1:
    sum_1 += i ** 2

for i in coor_2:
    sum_2 += i ** 2

if sum_1 > sum_2:
    print(f"{coor_2} are points that are located closer")
else:
    print(f"{coor_1} are points are located closer")
    
