# n = 987651
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)
print("====================================================")
def counting(n):
    count = 0
    while n > 0:  ##if this becomes true only it will work
        n = n // 10  ##floor division reduces the number by dividing
        count += 1
        print(count)
counting(9023112)