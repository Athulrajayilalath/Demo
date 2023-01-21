#def my_function():
#    print("Hello")

#my_function()

#to sum two numbers
#def add(a,b):
#    print("SUM",a+b)

#add(2,3)

#to print gmail of nay user that we give

#def gmail(username):
#    print(username+"@gmail.com")

#gmail("athul")

#take name and age as input and get output as username is "name" and age is "age"

def person(name,age):
    print("username is"+name+" and age is "+age)

person("athul",str(26))

#write a function that takes roll number and returns "available"is roll number is there in list and "not available" if not there in list

x =[23,44,66,55,12,6]

def data(roll):
    if roll in x:
        print("available")
    else:
        print("not available")
data(25)

#Define a function which print vowels and consonent in a word

def name(word):
    vow=0
    cont=0
    for i in word:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            vow=vow+1
        else:
            cont=cont+1
        print("count of vowels",vow)
        print("count of cont",cont)
name("apple")

#define a function that accepts radius and returns area of a circle
def circle(radius):
    print("area of circle:"+" "+str(3.14*(radius)**2))

circle(2)

#length and sum functions
lst = [1,2,3,4,5]
s = sum(lst)
print(s)

lst = [1,2,3,4,5]
s = len(lst)
print(s)

#sorted function
l = [3,1,2,4,5]
s = sorted(l)
print(s)

output = [1,2,3,4,5]

#Come up with a function that divides the first input by the second input:
def div(a,b):
    print(a/b)
div(4,2)
