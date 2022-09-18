#print newlist that has word "a" in each word

fruits = ["apple","banana","mango","cherry","kiwi"]
new_list = [x for x in fruits if "a" in x]
print(new_list)

#create a identical list from existing list using list comprehension

lst1 = [1,2,3,4,5]
new = [i for i in lst1]
print(new)

#create a list from range 1200 to 2000, with 130 steps intwn each using list comp
new=[i for i in range(1200,2000,130)]
print(new)

#use list comp to create new list but add 6 to each
lst1 = [1,2,3,4,5]
new = [i+6 for i in lst1]
print(new)

#using list comp , create anew list with squares of each in old list which is greater than 50
lst1= [2,4,6,8,10,12,14]
new = [i**2 for i in lst1 if i**2<50]
print(new)

#given dict is vehicles and their weight , construct new list with vechiles name only having weight less than 5000.also make key names all upper case.
dict= {"sedan":1500, "SUV":2000, "Pickup":2500, "Minivan":1600, "Van":2400, "Semi":13600, "Bicyccle":7, "Motorcycle":110}
new= [i.upper() for i in  dict if dict[i]<5000]
print(new)
