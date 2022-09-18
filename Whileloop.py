i = 1
while i<=10:
    print(i)
    i+=1
#

i=1
while i<10:
    print(i)
    if i == 3:
        break
    i+=1

#to reverse a number

num = 12
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num//10
print(reversed_num)

#natural numbers in reverse order
num = int(input("enter your number"))
i = num
while i>=0:
    print(i)
    i=i-1


# print star pattern

i = 1
while i<=4:
    print("*"*i)
    i=i+1


