#write a map function to add 5 to every number in list
lst1 = [10,20,30,40,50]
lst2 = list(map(lambda x:x+5,lst1))
print(lst2)

#writa  a ap function which gives squares of all numbers in list
lst1 = [1,2,3,4,5]
lst2 = list(map(lambda x:x**2,lst1))
print(lst2)

#write a map function tht adds "hello" infront of each word in list
lst1 = ["athul","vishnu","jithin","vignesh","adhil"]
lst2 = list(map(lambda x:"Hello"+x,lst1))
print(lst2)

#write a function using map and lambda to add two lists
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,1]
lst3 = list(map(lambda a,b:a+b,lst1,lst2))
print(lst3)

#using map() function and lambda and count() function create a list which consists of the number of occurance of letter  a
lst1 = ["Athul","acid","apple","Aakash"]
lst2 = list(map(lambda x:x.count("a"),lst1))
print(lst2)