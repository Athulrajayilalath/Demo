cars =["ford","benz","Toyota","Skoda"]
for x in cars:
    print(x)

#to check if triangle is equi,isos or scalene

a = int(input("enter side one"))
b = int(input("enter side two"))
c = int(input("enter side three"))
if a==b==c:
    print("Triangle is equilateral")
elif a==b or b==c or a==c:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")

#to find even numbers in a list

num =[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i%2==0:
        print(i)

#to print star pattern with for loop

n = int(input("Enter number of rows"))
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print()

#to print star pattern in reverse order

rows = int(input("Enter number of rows:"))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end="")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")