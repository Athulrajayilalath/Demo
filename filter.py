#to use filter and lambda together
lst1 = [12,-2,-1,0,2]
lst2 = list(filter(lambda x:x<0,lst1))
print(lst2)

#using filter and lambda ,filter even numbers so that only odd numers are passed to new list
lst1 = [22,100,19,13,11,1,4,66]
lst2 = list(filter(lambda x:x%2!=0,lst1))
print(lst2)

#using filter , list () functions and .lower() methoed filter all the vowels in a given string
str1="winter olympics in 2022 will take place in beijing China"
str2 = list(filter(lambda x: True if x.lower() in "aeiou" else False,str1))
print(str2)

#using map() and filter() function, add 2000 to all values below 8000
lst1= [1000,500,600,700,5000,9000,17500]
lst2 = list(map(lambda x:x+2000), filter(lambda x:x<8000,lst1))
print(lst2)