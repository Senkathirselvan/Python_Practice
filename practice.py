# print("Hello World")

# Find Positive Number and Negative Number:-
"""
number=int(input("Enter The Nuumber:"))
if number==0:
    print(number,"The Number is Center:")
elif number>0:
    print(number,"It is Positve Number:")
else:
    print(number,"It is Negative Number:")    
"""

# Find The Odd or Even Numbers:-
"""
number=int(input("Enter The Nuumber:"))
if number%2==1:
    print("It is Odd Number")
else:
    print("It is even Nmber")"""

# Find alphabet or Not alphabet:-

"""char=(input("Enter The Nuumber:"))
if (char>='a','A') and (char<='z','Z'):
    print("It is Alphabet")
    
else:
    print("It is Not Alphabet")"""


# Find Vowel or Consonant:-
"""
char=(input("Enter The Letter:"))
if (char=='a'or char=='e'or char=='i'or char=='o'or char=='u') and (char=='A'or char=='E'or char=='I'or char=='O'or char=='U'):
    print("It is  a Vowel")
    
else:
    print("It is Consonant")
"""


# Average of Given 5 numbers:-
"""n1=int(input("Enter The  First Number:"))
n2=int(input("Enter The Second Number:"))
n3=int(input("Enter The Third Number:"))
n4=int(input("Enter The  Forth Number:"))
n5=int(input("Enter The Fifth Number:"))
 
total=(n1+n2+n3+n4+n5)
average=((n1+n2+n3+n4+n5)/5)
print("Totale:",total)
print("Average:",average)
"""

#  Average of Given n numbers:-
"""n=int(input("How Many Numbers Yo Want To Find Average:"))
l1=[]
for i in range(n):
    l2=int(input("Enter The Numbers:"))
    l1.append(l2)
total=sum(l1)
print("Total:",total)
average=(total/len(l1)) # or We Use (total/n)
print("Average:",average)
"""

# Find Grade Value For Student:-

"""s1=int(input("Enter The Tamil Mark:"))
s2=int(input("Enter The English Mark:"))
s3=int(input("Enter The Maths Mark:"))
s4=int(input("Enter The Science Mark:"))
s5=int(input("Enter The Social Science Mark:"))
if s1>=90 and s1<=100:
    print("A Grade","Pass")
elif s1>=80 and s1<=89:
    print("B Grade","Pass")
elif s1>=70 and s1<=79:
    print("C Grade","Pass")
elif s1>=60 and s1<=69:
    print("D Grade","Pass")
elif s1>=50 and s1<=59:
    print("E Grade","Pass")
elif s1>=35 and s1<=49:
    print("F Grade","Fail")
else:
    print("No Grade")

if s2>=90 and s2<=100:
    print("A Grade","Pass")
elif s2>=80 and s2<=89:
    print("B Grade","Pass")
elif s2>=70 and s2<=79:
    print("C Grade","Pass")
elif s2>=60 and s2<=69:
    print("D Grade","Pass")
elif s2>=50 and s2<=59:
    print("E Grade","Pass")
elif s2>=35 and s2<=49:
    print("F Grade","Pass")
else:
    print("No Grade","Fail")

if s3>=90 and s3<=100:
    print("A Grade","Pass")
elif s3>=80 and s3<=89:
    print("B Grade","Pass")
elif s3>=70 and s3<=79:
    print("C Grade","Pass")
elif s3>=60 and s3<=69:
    print("D Grade","Pass")
elif s3>=50 and s3<=59:
    print("E Grade","Pass")
elif s3>=35 and s3<=49:
    print("F Grade","Pass")
else:
    print("No Grade","Fail")

if s4>=90 and s4<=100:
    print("A Grade","Pass")
elif s4>=80 and s4<=89:
    print("B Grade","Pass")
elif s4>=70 and s4<=79:
    print("C Grade")
elif s4>=60 and s4<=69:
    print("D Grade","Pass")
elif s4>=50 and s4<=59:
    print("E Grade","Pass")
elif s4>=35 and s4<=49:
    print("F Grade","Pass")
else:
    print("No Grade","Fail")

if s5>=90 and s5<=100:
    print("A Grade","Pass")
elif s5>=80 and s5<=89:
    print("B Grade","Pass")
elif s5>=70 and s5<=79:
    print("C Grade","Pass")
elif s5>=60 and s5<=69:
    print("D Grade","Pass")
elif s5>=50 and s5<=59:
    print("E Grade","Pass")
elif s5>=35 and s5<=49:
    print("F Grade","Pass")
else:
    print("No Grade","Fail")
total=(s1+s2+s3+s4+s5)
avarage=(total/5)
print("Total:",total)
print("Avarage",avarage)"""

# Number in a range That are Divisible By Gviven Number:-
"""
n1=int(input("Enter The Starting  Number:"))
n2=int(input("Enter The Ending Number:"))
n3=int(input("Enter The Divisible Number:"))
for i in range(n1,n2+1):
    if (i%n3==0):
        print(i)
else:
    print("No Numbers Can Divided")
"""
# Swaping Two Numbers Using Temprory Variable:-
"""
x=input("Enter The Numbers:")
y=input("Enter The Numbers:")   
z=x
x=y
y=z
print("x:",x)
print("y:",y)
"""

# Swaping Two N cumbers Without Temprory Variable:-
"""x=input("Enter The Numbers:")
y=input("Enter The Numbers:")   
x,y=y,x
print("x:",x)
print("y:",y)
"""
# Find quotient and Remainder Values in Given Numbers:-

"""n1=int(input("Enter The Number:"))
n2=int(input("Enter The Divisible Number:"))
quotient=n1/n2
remainder=n1%n2
print("The Quotient Value is:",quotient)
print("The Remainder Value is:",remainder)
"""

# Find Odd Numbers in Given Range and Find Even Numbers in Given Range:-
"""
n1=int(input("Enter The Starting  Number:"))
n2=int(input("Enter The Ending Number:"))

for i in range(n1,n2+1):
    if(i%2==1):
        print(i,"It is a Odd Number")
    else:
        print(i,"It is a Even Numbers")
        """

#  Write Multipilication Table:-

"""n1=int(input("Which Table You Want Print:"))
for i in range(1,20+1):
    table=i*n1
    print(i,"x",n1,"=",table)
print(n1,"Table Printed")
"""

# Unit Km to Mile Covertion:-

"""km=float(input("Enter The Number:"))
mile=km*0.621371
print("Your Mile Is:",mile)
"""
# Unit ile to Km Covertion:-
"""mile=float(input("Enter The Number:"))
km=mile*1.60934
print("Your Km Is:",km)
"""

# Find Largest Number in Three Inputs:-
"""
n1=int(input("Enter The First Number:"))
n2=int(input("Enter The Second  Number:"))
n3=int(input("Enter The Third Number:"))
l1=[]
l1.append(n1)
l1.append(n2)
l1.append(n3)
l1.sort()
if n1==n2==n3:
    print("All athe Numbers are Equal")
else:
    print(l1[2])
"""
# Find Sum of Natural Numbers:-
"""
n1=int(input("Enter The Number:"))
if n1<0:
    print("Pleas Enter The Positive Number Only")
else:
    val=0
    while(n1>0):
        val=val+n1
        n1=n1-1
print(val)
"""
# Find The Factorial Value:-

"""n1=int(input("Enter The Number:"))
if n1<0:
    print("Pleas Enter The Positive Number Only")
elif n1==0:
    print("The Factorial of 0 is",n1)
else:
    val=1
    while(n1>1):
        val=val*n1
        n1=n1-1
    print(val)
"""

# Find Fibonacci:-
"""
n1=int(input("Enter The Number:"))
a,b=0,1
count=0
while count<n1:
    print(a)
    c=a+b
    a=b
    b=c
    count=count+1
    """
    
# Find Leap Year or Not:-
"""
year=int(input("Enter The Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
             print("it is a Leap Year")
        else:
            print("it is Not a Leap Year")
    else:
        print("it is a Leap Year")
else:
    print("it is Not a Leap Year")
"""

# Find Whether a String is Palindrom or Not:-


"""str=input("Enter The Word:")
var=str[::-1]
if str==var:
    print("it is a Palindrom Word")
else:
    print("it is Not a Palindrom Word")
"""

# Find Whether a Number is Armstrong or Not:-
# some technical fault
"""n1=(input("Enter The Number:"))
a=[int(a) for a in str(n1)]
b=len(a)
result = []
for i in a[0:]:
    c=(i**b)
    result.append(c)
d=[(sum(result))] 
print(result)
print(d)
if a==d:
    print("The Number is Armstrong ") 
else:
    print("The Number is Not Armstrong ") 
"""


# To Print a Calender:-
"""
import calendar
print(calendar.calendar(2024))
print(calendar.prmonth(5))"""

# How to Find Lenth of The Int Value:-
"""
n1=int(input("Enter The Numbers:"))
count=0
while n1!=0:
    n1=n1//10
    count=count+1
print("Lenth of Your Number is:",count)
"""

# Find How Many characters in The List:-
 
"""str=int(input("Enter The Numbers:"))
count=0
for i in str:
    
    print("Lenth of Your Number is:",count)
"""


# Find Profit or Loss:-
"""
n1=float(input("Enter The Buy Rate:"))
n2=float(input("Enter The Salse Rate:"))
if n1<n2:
    amount=n2-n1
    print("Your Profit Is:",amount)
elif n1>n2:
     amount=n1-n2
     print("Your Loss Is:",amount)
else:
     print("No Profit No Loss All are Equal")
"""
# Find Factors:-
"""value=1
while value<=n1:
    if n1%value==0:
        print(value)
    value=value+1
"""

# Find Intrest:-
"""asall=int(input("Enter The Amount of Asall:"))
b=0.01
vatti=int(input("How Many Paisa vatti You Want:"))
if b<vatti:
    vatti=vatti*b
vatti1=asall*vatti
month=int(input("Enter The Month:"))
vatti1=vatti1*month
print("Your Asall Amount is:",asall)
print("Your Vatti Amount is:",vatti1)
total_asal_vatti=asall+vatti1
print("Your Total Amount [Asall + Vatti] is:",total_asal_vatti)
"""

# Find The List Lenth and Minimum Maximum:-
"""
list=[80,60,50,40,45,34,32,73,89,]
list.sort()
l1=len(list)
print("Lenth of The List is:",l1)
print("The Minimum Value of The list is:",list[0])
print("The Maximum Value of The list is:",list[8])
"""

# Find Student Mnimum and maximum Mark:-
"""l1=[]
sl=int(input("Enther The How Many Students:"))
i=0
while i<sl:
    mark=int(input("Enther The Students Marke:"))
    l1.append(mark)
    i=i+1
    l1.sort()
print("Total Student :",sl)
print("The Minimum Student Marke is:",l1[0])
print("The Minimum Student Marke is:",l1[-1])
"""
 # Find The Anagram Word:-

"""word1=input("Enter The Word:")
a=list(word1)  #
a.sort()       #or  a=sorted(word1)
word2=input("Enter The Word:")
b=list(word2)  #
b.sort()       #or  b=sorted(word2)
if a==b:
    print("It is a Anagram Word")
else:
     print("It is Not a Anagram Word")
"""

# Find a Valid Date:-
"""
day=int(input("Enter The Days:"))
month=int(input("Enter The Month:"))
year=int(input("Enter The Year:"))

if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    days=31
elif month==4 or month==6 or month==9 or month==11:
    days=30
    
elif year%4==0 and year%100!=0 or year%400==0:
    days=29
else:
    days=28
   

if day<=1 or day>=days:
    print("Pleas Provide a Valide Day")
elif month<=1 or month>=12:
    print("Pleas Provide a Valide Month")
else:
    print("Valid Date.....")

"""

# Find Second Largest Number:-
"""
l1=[]
l2=int(input("How Many Numbers You Want:"))
for i in range(l2):
    l3=int(input("Enter The Number:"))
    l1.append(l3)
l1.sort()
set(l1)
print(l1[-2])
"""

# Replace Characters:-
"""
word=input("Enter The Word:")
rword=input("Enter The Old Letter:")
nword=input("Enter The New Letter:")

word1=""
for i in range(len(word)):
    if word[i]==rword:
        word1=word1+nword
    else:
        word1=word1+word[i]
print("\noriginal word:",word)
print("new word:",word1)
"""
# Write a Program Draw a Pyramid:-
















