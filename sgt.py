"""
Student Grade Tracker by karthik

A simple CLI application to manage students,
grades, GPA calculations, and class rankings.
"""

import json

class student:
    def __init__(self,name,roll,grades):
        self.name=name
        self.roll=roll
        self.grades=grades
    
    def __str__(self):
        return f"Student: {self.name} | Roll: {self.roll}"       

class cource:
    def __init__(self,code,name,students):
        self.code=code
        self.name=name
        self.students=students

bsc=cource(1,'Bsc CS',[])
ba=cource(2,'Ba ENG',[])
msc=cource(3,'Msc AI',[])

co=[bsc,ba,msc]
st=[]

def save():
    data=[{'name':s.name,'roll':s.roll,'grades':s.grades} for s in st]
    with open('students.json','w')as f:
        json.dump(data,f)

def load():
    try:
        with open('students.json','r')as f:
            for d in json.load(f):
                st.append(student(d['name'],d['roll'],d['grades']))
    except FileNotFoundError:
        pass

def addstudent():
    n=input("ENTER NAME OF STUDENT:")
    r=int(input("ENTER ROLL NO OF STUDENT:"))
    c=input("ENTER YOUR COURCE")

    s=student(n,r,{})
    st.append(s)
   
    for x in co:
        if(c==x.name):
            x.students.append(s)

    save()



def addgrade():
    n=input("Enter student name:")
    g=input("Enter subject:")
    m=int(input("Enter mark:"))

    for x in st:
        if(n==x.name):
            x.grades[g]=m
            break
    else:
        print("No student of that name found")
    save()

def computegpa(n):
    tot=0
    for x in st:
        if(n==x.name):
            for p in x.grades.values():
                tot=tot+p
            gpa=tot/len(x.grades)
            return gpa
    else:
        print("No student of that name found")

def classavg():
    c=input("Enter the class name:")
    listgpa=[]
    for j in co:
        if(c==j.name):
            for st in j.students:
                listgpa.append(computegpa(st.name))
            return(sum(listgpa)/len(listgpa))
    print("No cource of that name found")

def leaderboard():
    c=input("Enter the class name:")
    listop={}
    for j in co:
        if(c==j.name):
            for st in j.students:
                listop[st.name]=(computegpa(st.name))
            leader=dict(sorted(listop.items(),key=lambda x:x[1] , reverse=True))
            for rank, (name, gpa) in enumerate(leader.items(), start=1):
                print(f"{rank}. {name} - GPA: {gpa:.2f}")
                if rank == 3:
                    break

load()

while True:
    print(" ")
    print("====STUDENT GRADE TRACKER====")
    print("WHAT YOU WANT TO DO?")
    print('1)ADD STUDENT')
    print('2)ADD GRADE')
    print('3)COMPUTE GPA')
    print('4)CLASS AVG')
    print('5)SHOW LEADERBOARD')
    print("6)EXIT")

    try:
         a=int(input("ENTER YOUR CHOICE:"))
    except ValueError:
         print("ENTER A VALID NUMER")
         continue

    if(a==1):
        addstudent()

    elif(a==2):
        addgrade()
         
    elif a == 3:    
        n= input("Enter student name:")
        gpa = computegpa(n)
        if gpa:
            print(f"{n}'s GPA: {gpa}")


    elif(a==4):
        c=classavg()
        if c:
            print(f'Class avg is {c}')
    
    elif(a==5):
        leaderboard()

    elif(a==6):
        break
    




    







