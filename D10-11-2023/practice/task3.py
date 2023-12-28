n =int(input("enter a value"))
sum1 =0
for x in range(n):
    a = int(input("enter the number"))
    sum1 =sum1+a
    if a ==0:
        break    
print(sum1)