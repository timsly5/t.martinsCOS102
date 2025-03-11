P = int(input("Enter your principal: "))
R = int(input("Enter your rate: "))
n = int(input("Enter your number: "))
t = int(input("Enter your time: "))
A =  P * (1 + R/n)**n*t
print(A)