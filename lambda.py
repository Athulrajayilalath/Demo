#lambda arguments : expression
x = lambda a:a+10
print(x(5))

#write a lambda function that takes x as parameter as returns x+2
w = lambda x:x+2
print(w(2))

#write a lambda function which takes two arguments : a and b and returns their multiplication
x = lambda a,b:a*b
print(x(1,7))

#uisng sorted() function and lambda sort second letter in alphabetical order for below lst

lst = ["ijkl","lmno","acdb","ptsa"]
lst = sorted(lst,key = lambda x:x[1])
print(lst)