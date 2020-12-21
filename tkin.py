# STUDENT APPLICATION FORM USING TKINTER #

from tkinter import *


a = Tk()


a.title("Student Info")

Label(a,text="Coimbatore Institute of Technology",font =("Helvetica",16)).grid(row = 0,column = 1)



name = Label(a,text = "Name").grid(row=1,column=0)

namevalue = StringVar()

e1=Entry(a,textvariable = namevalue)

e1.grid(row=1,column=1)



rollno = Label(a,text="Roll Number").grid(row = 2,column = 0)

rollvalue = IntVar()

e2 = Entry(a,textvariable = rollvalue)

e2.grid(row=2,column=1)



dob = Label(a,text="Date of Birth (DD.MM.YYYY)").grid(row = 3, column = 0)

dobvalue = IntVar()

e3 = Entry(a,textvariable = dobvalue)

e3.grid(row = 3,column = 1)



Label(a,text="Gender").grid(row = 4 , column = 0)

var1 = IntVar()

m = Radiobutton(a,text="Male",variable = var1 ,value = 1)

f = Radiobutton(a,text="Female",variable = var1 ,value = 2)


m.grid(row = 5 , column =1)

f.grid(row = 5 , column =2)



Label(a,text = "Department").grid(row = 6, column = 0)

var2 = IntVar()


d1 = Radiobutton(a,text="Cs",variable = var2,value=1)

d2 = Radiobutton(a,text="ECE",variable = var2,value=2)

d3 = Radiobutton(a,text="Civil",variable = var2,value=3)

d4 = Radiobutton(a,text="EEE",variable = var2,value=4)

d5 = Radiobutton(a,text="Mech",variable = var2,value=5)


d1.grid(row = 7,column = 1)

d2.grid(row = 7,column = 2)

d3.grid(row = 7,column = 3)

d4.grid(row = 8,column = 1)

d5.grid(row = 8,column = 2)



Label(a,text = "Current Year").grid(row = 9, column = 0)


year=["First Year","Second Year","Third Year","Fourth Year"]

y = StringVar(a)

y.set("SELECT")

y1 = OptionMenu(a, y, *year)

y1.grid(row = 10, column = 1)



Label(a,text = "10th Percentage").grid(row = 12, column = 0)

mark_1 = Scale(a,from_=0,to=100,orient = HORIZONTAL)

mark_1.grid(row = 12, column = 1)

Label(a,text = "12th Percentage").grid(row = 13, column = 0)

mark_2 = Scale(a,from_=0,to=100,orient = HORIZONTAL)

mark_2.grid(row = 13 , column =1)

Label(a,text = " Programming Languages Known:").grid(row = 14 , column = 0)


var3 = IntVar()

var4 = IntVar()

var5 = IntVar()

var6 = IntVar()

var7 = IntVar()

var8 = IntVar()


c1 = Checkbutton(a,text = "C",variable = var3, onvalue = 1, offvalue= 0)

c2 = Checkbutton(a,text = "C++",variable = var4, onvalue = 1, offvalue= 0)

c3 = Checkbutton(a,text = "Phython",variable = var5, onvalue = 1, offvalue= 0)

c4 = Checkbutton(a,text = "Java",variable = var6, onvalue = 1, offvalue= 0)

c5 = Checkbutton(a,text = "Javascript",variable = var7, onvalue = 1, offvalue= 0)

c6 = Checkbutton(a,text = "HTML",variable = var8, onvalue = 1, offvalue= 0)

c1.grid(row = 15, column = 1)

c2.grid(row = 15, column = 2)

c3.grid(row = 15, column = 3)

c4.grid(row = 16, column = 1)

c5.grid(row = 16, column = 2)

c6.grid(row = 16, column = 3)



Label(a,text = "Attendance Percentage").grid(row = 17,column = 0)

att = Spinbox(from_=65,to=100,increment=5)

att.grid(row = 18, column = 1)



Label(a,text  = "CGPA").grid(row = 19,column = 0)

gpa = Spinbox(from_=6,to=10,increment = 0.5)

gpa.grid(row = 20, column = 1)



def submit():
    
    print(f"YOUR SUBMIT RESPONSE HAS BEEN RECORDED")
    
    x1=e1.get()
    
    x2=int(e2.get())
    
    x3=e3.get()
    
    x4=int(mark_1.get())
    
    x5=int(mark_2.get())

    x6=att.get()

    x7=gpa.get()


    print(" ")
    
    print("Student Name: ",x1)
    
    print(" ")
    
    print("Roll Number: ",x2)
    
    print(" ")

    global gender
    
    gender = var1.get()
    
    a.quit()

    if(gender == 1):
        print("Gender : Male")
        
    elif(gender == 2):
        print("Gender : Female")
        
    print(" ")

    global department
    
    department = var2.get()
    
    a.quit()

    if(department == 1):
        
        print("Department : CS")
        
    elif(department == 2):
        
        print("Department : ECE")
        
    elif(department == 3):
        
        print("Department : Civil")
        
    elif(department == 4):
        
        print("Department : EEE")
        
    elif(department == 5):
        
        print("Department : Mech")
        

    print(" ")
    
    print("Date Of Birth: ",x3)
    
    print(" ")

    print("10th Mark: ",x4,"%")

    print(" ")

    print("12th Mark: ",x5,"%")

    print(" ")
    
    print("Attendance percentage: ",x6,"%")
    
    print(" ")
    
    print("CGPA: ",x7)

    print(" ")

    print("Programming Languages known: ")

    
    if (var3.get() == 1):
        print("                             * C")
        
    if(var4.get() == 1):
        print("                             * C++")
        
    if(var5.get() == 1):
        print("                             * Python")
        
    if(var6.get() == 1):
        print("                             * Java")
        
    if(var7.get() == 1):
        print("                             * Javascript")
        
    if(var8.get() == 1):
        print("                             * Html")


    print(" ")


    global ye
    
    ye = y.get()
    
    a.quit()

    print("Current Year: ",ye)
    


sub = Button(a,text = "SUBMIT",fg="Blue",command = submit)

sub.grid(row = 22, column =2)

a.mainloop()







          
          
