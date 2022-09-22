#f = open("data","r")
#lst=[]
#for num in f:
#    lst.append(num.rstrip("\n"))
#print(lst)

#we can also read a file asssss
with open ("filepath","r") as File1:
    Filenew = File1.read()
    print(Filenew)
    
#we can read 1st line by
with open ("filepath","r") as File1:
    Filenew = File1.readline()
    print(Filenew)
 #Here if we give 2,3,4 etc inside brackets-we will get output that much compoenents

#open tempfile and load district and their max temp
#step1:open temp file in python
#f = open("tempfile","r")
#lst=[]
#for num in f:
#    lst.append(num.rstrip("\n"))
#print(lst)
#step 2: find district with max temp
#f = open("tempfile","r")
#dic={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    district=data[0]
    temperature=data[1]
    if(district not in dic):
        dic[district]=temperature
    else:
        old=dic[district]
        if temperature>old:
            dic[district]=temperature
print(dic)

#now open customer file and find count of age
f = open("customer","r")
dict={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    age=data[3]
    if (age in dic):
        dic[age]+=1
    else:
        dic[age]=1
print(dic)

