# a=12345
# print(a%10) #remainder(last digit given)
# print(a//10) #quotient decimal ni tisesi round figure chestundi(last digit removed)
# print(a/10)  #quotient decimal istundi remainder 0 cheydaniki
print("=============================================")
# b=12
# print(b%2)
print("=============================================")
n = 1234
rev = 0
while n > 0:
    digit = n%10
    rev = rev * 10 + digit
    n = n // 10
print(rev)