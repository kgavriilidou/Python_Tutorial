print("This line will be printed.")

x = 1
if x== 1:
	print ("x is 1.")
        
               
p1 = 6
p2 = 3
p3 = p1+p2
print(p3)

a,b = 3,4
print(a,b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print "hello"+"world"
print "hello world" ; print "hello world" ; print """ hello world """
""" My comments"""
print 4+6
print 3*3
print 5%2
print 5**2
print float(5/2)
print float(5)/2
print 5.0/2.0
print 2>3
print 5+5==7
print 5+5<=10
print -1<=-10
if 3>5: "Yes" 
	#else: "No"

lot = "hello" * 10
print (lot)

even = [2,4,6,8]
odd = [1,3,5,7]
all_numbers = even + odd
print all_numbers
all_numbers.sort()
print all_numbers

print 5+399989884
print "5+399989884"
print "5"+"399989884"

text = "abcd"
print text
text = 1234

myage = 36
yourage = 40
diff  = myage - yourage
avg = (myage + yourage)/2
print "the first age is", myage
print "the second age is", yourage
print "the difference is", diff
print "the average is", avg

myvarr = 5655777688
print "lets sub .. %d without" %myvarr

var1=2
var2=3
var3=4
print "I know my numbers %d, %d, %d" %(var1,var2,var3)

var1=2
var2=3.44
var3="Hello"
print "I know my numbers %d, %.2f, %s" %(var1,var2,var3)

for i in range(10):
	print i

print " "
	
for i in range (5,100,10):
	print i

print " "
	
for i in range (100,5,-10):
	print i

print ""

for i in range(1,7):
	for j in range (1,7):
		print i,j
print ""	
file_in = open("fibo.py","r")
for line in file_in:
	print line
file_in.close()

print ""

file_in = open("textfile.txt", "w")
file_in.write("My demo")
file_in.close()

myfile=open("textfile.txt", "w")
myfile.write("whats news pushy cat?")
myfile.close()

a=[1,2,34,56]
print a[1]
print a[3]
print a[-3], a[-2], a[-1]
a[2]= 56
print a[2]
print a 

a= [34,56,7,7,8,9]
a.append(899)
print a

myfile = open("myfile.txt", "w")
myfile.write ("[a,b,c,d,e,f,g]")
myfile.close()

myfile = open("myfile.txt", "a")
myfile.write("h")
myfile.close()

a=[3,4,5,6,9]
a.insert (4,7)
a.insert (5,8)
print a
a.remove(6)
print a
print a.count(5)
a.reverse ()
print a
print ""

a = [13,24,36,4,5,6,7,8,9,10]
print a
b = a[3:8]
c= a[:8]
d= a[:-1]
e= a[4:]
f = a[::2]
g = a[1::2]
k = a+ g
print b, c, d, e, f, g
print len(a), max(a), min(a), sum(a)
print ""
print k
print cmp(a,k)

print ""

#fin = open("a.txt", "r")
#lst=[]
#for line in fin :
#	line=line.strip()
#	lst.append(line)
#headers = lst[0].split(",")
#values= lst[-1].split(",")
#tmp="<html><title>Meteo</title><body><h1>Meteo</h1>"
#for i in range(len(headers)):
#	tmp+="%s<br>"%(str(headers[i]),str(values[i]))
#	tmp+="</body></html>"
#	fout=open("out.html","w")
#	fout.write(tmp)
#	fout.close()
#
x=3
p=4
if x>p : print "x is greater than p"
else : print "p is greater than x"

name = "john"
age = 23
if name == "john" and age ==23 : print "your name is %s" %(name)
print ""

for x in range(5):
	print(x)
for x in range (5,7):
	print(x)
	
print ""
count=0
while count <= 10:
	print (count)
	count+=1
print ""	

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
	
students ={
"Nikos": 555555,
"Giota": 888888,
"July" : 56656
}
for name, number in students.items():
	print("phone numbers of %s is %d") %(name,number)
print students
del students ["Nikos"]
print students

print ""
students ={
"Nikos": 555555,
"Giota": 888888,
"July" : 56656
}
for name, number in students.items():
	print("phone numbers of %s is %d") %(name,number)
print students
students.pop("July")
print(students)
