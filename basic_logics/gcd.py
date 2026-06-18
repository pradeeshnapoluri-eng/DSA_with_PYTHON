# a=12
# b=18
# gcd=1
# for i in range(1,min(a,b)+1):
#     if a % i == 0 and b % i == 0:
#         gcd=i
#         print(gcd)
# print('=======================================')
# a=12
# b=18
# gcd=1
# for i in range(1,19):
#     if a%i == 0 and b % i == 0:
#         gcd=i
#         print
# print('================================================')
# a=16
# gcd=1
# for i in range(1,a+1):
#     if a % i == 0:
#         gcd=i
#         print(gcd)
# print('===== OWN CODE ======')
def gcd_factor(a):
    num=a
    for i in range(1,a+1):
        if a % i == 0:
            print(i)
            # print(gcd)
gcd_factor(8)
gcd_factor(12)
# gcd_factor(14)