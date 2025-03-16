PMT = int(input("Enter your dollar price: "))
R = int(input("Enter your rate: "))
n = int(input("Enter your number of periods: "))
t = int(input("Enter your time: "))
A = ((PMT) * (1+R/n)**n*t -1)/R/n
print(A)

