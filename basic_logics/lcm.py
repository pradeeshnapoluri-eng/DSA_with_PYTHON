# a = 4
# b = 8
# i = max(a,b)
# while True:
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break
#     else:
#         i += 1
print('===========================================================')
def lcm_factor(a,b):
    num=a,b
    i = max(a,b)
    while True:
        if i % a == 0 and i % b == 0:
            print(i)
            break
        else:
            i += 1
lcm_factor(9,4)