cars={
    "brand":"ford",
    "model":"Mustang",
    "year":2018,
    "colour":"blue",
    "Transmission":"Automatic"
}


#print(cars["brand"])

#print(cars.keys())

#print(cars.values())

#print(cars["year"],["colour"])

#to change any value
cars["year"]=2002
print(cars)

#to check if mileage key is available
if "mileage" in cars:
    print("available")
else:
    print("not available")

#add mileage to cars
cars["mileage"]=20
print(cars)
print("mileage",cars["mileage"])

#to delete any key from dict
cars.pop("year")
print(cars)

#to delete complete dict
del cars

#using clear in dict
#cars.clear()
#print(cars)

cars={
    "brand":"ford",
    "model":"Mustang",
    "year":2018,
    "colour":"blue",
    "Transmission":"Automatic"
}
print(cars)

#using for to get key and value from dict
for i in cars:
    print(i,cars[i])

#now we have a array
cars=["ford","volvo","bmw","volkswagon","Skoda"]

#print(cars[0])
#cars[0]="Toyota"
#print(cars)
#print(len(cars))

#using for loop in arrays
# for i in cars:
#    print(i)

#add new thing to array
cars.append("HONDA")
print(cars)

#to add simply new things to array/list
cars.extend("maruthi")
print(cars)

#o delete from array
cars.pop(1)
print(cars)

#we can split
a = "athul raj"
a.split()
print(a)

#also we can use remove here, but we have to use value name isntead of index
cars.remove("bmw")
print(cars)

#print characters from a string that are available in even index number
name = str(input("enter your name"))
for k in range(len(name)):
    if k%2==1:
        print(name[k])

#display numbers divisible by 5 from array

numbers = [10,20,33,46,55,32,1]
for i in numbers:
    if i%5==0:
        print(i)

#count total number of diits in a number
num = int(input("enter number"))
count=0
while num != 0:
    num=num//10
    count=count+1
print(count)

#or

n = 123456
print(len(str(n)))