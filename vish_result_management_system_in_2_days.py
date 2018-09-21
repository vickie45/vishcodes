from tkinter import *
import sqlite3

#open database connection
db=sqlite3.connect('resultdisplay.db')
#creating cursor objects for database
cursor=db.cursor()

class resplay:
    
    
    def __init__(self,win):

        #model
        
        #for entry window
        self.stud_name=StringVar()
        self.seat_no=IntVar()
        self.coursevar=StringVar()

        #for teacher window
        self.usernameval=StringVar()
        self.passwordval=StringVar()

        
        
        #for entry window
        self.sexval=StringVar()
        
        #subject variables
        self.sub1=StringVar()
        self.sub2=StringVar()
        self.sub3=StringVar()
        self.sub4=StringVar()
        self.sub5=StringVar()
        self.sub6=StringVar()
        self.sub7=StringVar()
        
        #marks variables
        self.m1=IntVar()
        self.m2=IntVar()
        self.m3=IntVar()
        self.m4=IntVar()
        self.m5=IntVar()
        self.m6=IntVar()
        self.m7=IntVar()
        
        #evaluation variables
        self.total=IntVar()
        self.percent=DoubleVar()
        self.grade=StringVar()
        
        #window-one for id choice
        #widgets
        #frames
        self.f1=Frame(win,height=500,bd=30,width=750,relief=RIDGE)
        self.f2=Frame(win,height=500,bd=30,width=750,relief=RIDGE)
        
        #label
        self.lab1=Label(self.f1,text="select your identity",font=24,fg="green",relief=RIDGE)
        
        #buttons
        self.b1=Button(self.f2,text="Teacher",fg="green",font=24,command=self.Teacher_window,relief=RIDGE)#button opens teacher window
        self.b2=Button(self.f2,text="Student",fg="green",font=24,command=self.Student_window,relief=RIDGE)#button opens student window

        #packing
        self.f1.pack(expand=YES,fill=BOTH)
        self.f2.pack(expand=YES,fill=BOTH)
        self.lab1.pack(side=LEFT,expand=YES,fill=BOTH)
        self.b1.pack(side=TOP,expand=YES,fill=BOTH)
        self.b2.pack(side=TOP,expand=YES,fill=BOTH)
        
    def  Teacher_window(self):

        #window-two for teacher login
        #widgets
        self.top1=Toplevel(bd=30,relief=RIDGE)#add frame pending
        self.twf=Frame(self.top1,height=250,bd=30,width=500,relief=RIDGE)
        self.twf0=Frame(self.twf,height=250,bd=20,width=500,relief=RIDGE)
        self.twf1=Frame(self.twf0,height=250,bd=10,width=500,relief=RIDGE)
        self.twf2=Frame(self.twf0,height=250,bd=10,width=500,relief=RIDGE)
        
        #labels
        self.lab2=Label(self.top1,text="Welcome Respected Teacher",font=24,fg="green",relief=RIDGE)
        self.username=Label(self.twf1,text="username:",fg="green",font=24,relief=RIDGE,)
        self.password=Label(self.twf1,text="password",fg="green",font=24,relief=RIDGE,)
        
        #entries
        self.entry_1=Entry(self.twf2,bg="black",fg="green",relief=RIDGE,font=24,textvariable=self.usernameval)#username_entry
        self.entry_2=Entry(self.twf2,bg="black",show="*",fg="green",relief=RIDGE,font=24,textvariable=self.passwordval)#password_entry

        
        #buttons
        self.c=Checkbutton(self.twf,text="keep me logged in",fg="red",font=24,relief=RIDGE)#checkbutton
        self.login=Button(self.top1,text="Sign In",fg="green",font=24,command=self.loginf,relief=RIDGE)#button
        self.signup=Button(self.top1,text="Sign up",fg="green",font=24,command=self.create_acc,relief=RIDGE)
        
        #packing
        self.top1.minsize(1024,768)
        self.lab2.pack(side=TOP,expand=YES,fill=BOTH)
        
        #frames
        self.twf.pack(expand=YES,fill=BOTH)
        self.twf0.pack(expand=YES,fill=BOTH)
        self.twf1.pack(side=LEFT,expand=YES,fill=BOTH)
        self.twf2.pack(side=RIGHT,expand=YES,fill=BOTH)
        
        #widgets 
        self.username.pack(side=TOP,expand=YES,fill=BOTH)
        self.password.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.entry_1.pack(side=TOP,expand=YES,fill=BOTH)
        self.entry_2.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.c.pack(side=RIGHT,expand=YES,fill=BOTH)
        self.login.pack(side=RIGHT,expand=YES,fill=BOTH)
        self.signup.pack(side=LEFT,expand=YES,fill=BOTH)
        
        
    def  Student_window(self):

        #student_window
        #widgets
        self.top2=Toplevel(bd=30,relief=RIDGE)
        self.fsw=Frame(self.top2,height=250,bd=30,width=500,relief=RIDGE)
        self.fsw1=Frame(self.fsw,height=250,bd=5,width=500,relief=RIDGE)
        self.fsw2=Frame(self.fsw,height=250,bd=5,width=500,relief=RIDGE)
        
        
        #label
        self.lab3=Label(self.top2,text="Welcome Dear Student",font=24,fg="green",relief=RIDGE)
        self.studentname=Label(self.fsw1,text="enter your name",font=24,fg="green",relief=RIDGE)
        self.seat_no_label0=Label(self.fsw1,fg='green',font=24,text='Seat no:',relief=RIDGE)
        #entry
        self.stud_entry=Entry(self.fsw2,bg="black",fg="green",font=24,relief=RIDGE,textvariable=self.stud_name)
        self.seat_no_entry0=Entry(self.fsw2,bg='black',fg="green",font=24,textvariable=self.seat_no,relief=RIDGE)
        #button
        self.getresult=Button(self.top2,text="Get Result",font=24,fg="green",command=self.dbviewer,relief=RIDGE)
        self.bk12=Button(self.top2,font=24,text='Back',relief=RIDGE,command=lambda : self.backf(self.top2))
        
        #student_window packing
        self.top2.minsize(1024,768)
        self.lab3.pack(side=TOP,expand=YES,fill=BOTH)
        self.fsw.pack(side=TOP,expand=YES,fill=BOTH)
        self.fsw1.pack(side=LEFT,expand=YES,fill=BOTH)
        self.fsw2.pack(side=RIGHT,expand=YES,fill=BOTH)

        
        #student_window widgets packing
        self.studentname.pack(side=TOP,expand=YES,fill=BOTH)
        self.stud_entry.pack(side=TOP,expand=YES,fill=BOTH)
        self.seat_no_label0.pack(side=TOP,expand=YES,fill=BOTH)
        self.seat_no_entry0.pack(side=TOP,expand=YES,fill=BOTH)
        self.getresult.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.bk12.pack(side=BOTTOM,expand=YES,fill=BOTH)
        
    def  dbopener(self):
        
        #window-3 for teacher to open db
        #widgets
        self.top3=Toplevel(bd=30,relief=RIDGE)
        self.dbpf1=Frame(self.top3,height=250,width=500,bd=30,relief=RIDGE)
        
        self.menu1=Menu()
        self.top3.config(menu=self.menu1)
        self.file=Menu(self.menu1)
        self.menu1.add_cascade(label="File",menu=self.file)
        self.file.add_command(label="Create new record",font=24,command=self.entry_window)
        self.file.add_separator()
        self.file.add_command(label="quit",command=quit)
        
        self.lab4=Label(self.dbpf1,text="Go to file to create new record",font=44,fg='green',relief=RIDGE)
        self.bk13=Button(self.top3,font=24,text='Back',relief=RIDGE,command=lambda : self.backf(self.top3))
        #packing
        self.top3.minsize(1024,768)
        self.dbpf1.pack(expand=YES,fill=BOTH)
        self.lab4.pack(expand=YES,fill=BOTH)
        self.bk13.pack(expand=YES,fill=BOTH)
        
        
    def entry_window(self):

        #window-4 for teacher to enter data
        #widgets
        self.top6=Toplevel()
        
        #frame
        self.f3=Frame(self.top6,borderwidth=4,bd=30,height=250,width=500,relief=RIDGE)
        
        #labels
        self.label1=Label(self.f3,fg='green',text='Name:',font=24,relief=RIDGE)
        self.seat_no_label=Label(self.f3,fg='green',text='Seat no:',font=24,relief=RIDGE)
        self.sex=Label(self.f3,fg='green',text='sex:',font=24,relief=RIDGE)
        self.courselab=Label(self.f3,fg='green',text='Course name:',font=24,relief=RIDGE)
        
        #entries
        self.name_entry=Entry(self.f3,textvariable=self.stud_name,font=24,relief=RIDGE)
        self.seat_no_entry=Entry(self.f3,textvariable=self.seat_no,font=24,relief=RIDGE)
        self.course_entry=Entry(self.f3,textvariable=self.coursevar,font=24,relief=RIDGE)

        #radiobuttons
        self.sex1=Radiobutton(self.f3,text="male",variable=self.sexval,font=24,value='male',relief=RIDGE)
        self.sex2=Radiobutton(self.f3,text="female",variable=self.sexval,font=24,value='female',relief=RIDGE)
        self.sex3=Radiobutton(self.f3,text="other",variable=self.sexval,font=24,value='other',relief=RIDGE)
        
        #frames
        self.f04=Frame(self.top6,borderwidth=4,bd=10,height=500,width=1000,relief=RIDGE)
        self.f4=Frame(self.f04,borderwidth=4,bd=10,height=250,width=500,relief=RIDGE)
        self.f4a=Frame(self.f4,borderwidth=4,bd=10,height=250,width=500,relief=RIDGE)
        self.f4b=Frame(self.f4,borderwidth=4,bd=10,height=250,width=500,relief=RIDGE)
        self.f5=Frame(self.f04,borderwidth=4,bd=10,height=250,width=500,relief=RIDGE)
        
        #buttons
        self.bclear=Button(self.f5,text="Clear",relief=RIDGE,font=24,command=self.clearf)
        self.bsave=Button(self.f5,text="Save",relief=RIDGE,font=24,command=self.savef)
        self.bundo=Button(self.f5,text="Undo",relief=RIDGE,font=24,command=self.undof)
        self.calb=Button(self.f4,text="Calculate ",relief=RIDGE,font=24,command=self.calf)
        self.bk1=Button(self.f5,font=24,text='Back',relief=RIDGE,command=lambda : self.backf(self.top6))
        

        #labels 
        self.lbs=Label(self.f4a,bg='powder blue',fg='black',font=24,text="subjects:",relief=RIDGE)
        self.mlbs=Label(self.f4b,bg='powder blue',fg='black',font=24,text="marks:",relief=RIDGE)

        #entries for subjects
        self.e1=Entry(self.f4a,fg='green',font=24,textvariable=self.sub1,relief=RIDGE)#storing subject names entries
        self.e2=Entry(self.f4a,bg='powder blue',font=24,fg='green',textvariable=self.sub2,relief=RIDGE)
        self.e3=Entry(self.f4a,fg='green',font=24,textvariable=self.sub3,relief=RIDGE)
        self.e4=Entry(self.f4a,bg='powder blue',font=24,fg='green',textvariable=self.sub4,relief=RIDGE)
        self.e5=Entry(self.f4a,fg='green',font=24,textvariable=self.sub5,relief=RIDGE)
        self.e6=Entry(self.f4a,bg='powder blue',font=24,fg='green',textvariable=self.sub6,relief=RIDGE)
        self.e7=Entry(self.f4a,fg='green',font=24,textvariable=self.sub7,relief=RIDGE)
        
        #entries  for marks
        self.me1=Entry(self.f4b,font=24,fg='green',textvariable=self.m1,relief=RIDGE)#storing subject marks entries
        self.me2=Entry(self.f4b,font=24,bg='powder blue',fg='green',textvariable=self.m2,relief=RIDGE)
        self.me3=Entry(self.f4b,font=24,fg='green',textvariable=self.m3,relief=RIDGE)
        self.me4=Entry(self.f4b,font=24,bg='powder blue',fg='green',textvariable=self.m4,relief=RIDGE)
        self.me5=Entry(self.f4b,font=24,fg='green',textvariable=self.m5,relief=RIDGE)
        self.me6=Entry(self.f4b,font=24,bg='powder blue',fg='green',textvariable=self.m6,relief=RIDGE)
        self.me7=Entry(self.f4b,font=24,fg='green',textvariable=self.m7,relief=RIDGE)

        
        
        #eval-labels
        self.lt0=Label(self.f4a,font=24,fg='green',text='The TOTAL is=',relief=RIDGE)
        self.lp0=Label(self.f4a,font=24,fg='green',text='The Percentage is=',relief=RIDGE)
        self.lg0=Label(self.f4a,font=24,fg='green',text='The Grade is =',relief=RIDGE)
        
        self.lt=Label(self.f4b,font=24,fg='green',textvariable=self.total,relief=RIDGE)
        self.lp=Label(self.f4b,font=24,fg='green',textvariable=self.percent,relief=RIDGE)
        self.lg=Label(self.f4b,font=24,fg='green',textvariable=self.grade,relief=RIDGE)
        
        #packing
        self.top6.minsize(1024,768)
        #frame-f3
        self.f3.pack(expand=YES,fill=BOTH)
        self.label1.grid(row=2,column=2,columnspan=4,rowspan=4)
        self.name_entry.grid(row=2,column=6,columnspan=4,rowspan=4)
        self.seat_no_label.grid(row=8,column=2,columnspan=4,rowspan=4)
        self.seat_no_entry.grid(row=8,column=6,columnspan=4,rowspan=4)
        self.sex.grid(row=14,column=2,columnspan=4,rowspan=4)
        self.sex1.grid(row=14,column=8,rowspan=4)
        self.sex2.grid(row=14,column=9,rowspan=4)
        self.sex3.grid(row=14,column=14,rowspan=4)
        self.courselab.grid(row=20,column=2,rowspan=4,columnspan=4)
        self.course_entry.grid(row=20,column=8,rowspan=4,columnspan=4)
        

        #frame-04
        self.f04.pack(expand=YES,fill=BOTH)
        
        #frame-f4 in f04 
        self.f4.pack(expand=YES,fill=BOTH)
        self.calb.pack(side=BOTTOM,expand=YES,fill=BOTH)
        
        #frame f4a & f4b in f4
        self.f4a.pack(side=LEFT,expand=YES,fill=BOTH)
        self.f4b.pack(side=RIGHT,expand=YES,fill=BOTH)
        
        
        #subjects entry widget packing
        self.lbs.pack(expand=YES,fill=BOTH)
        self.e1.pack(expand=YES,fill=BOTH)
        self.e2.pack(expand=YES,fill=BOTH)
        self.e3.pack(expand=YES,fill=BOTH)
        self.e4.pack(expand=YES,fill=BOTH)
        self.e5.pack(expand=YES,fill=BOTH)
        self.e6.pack(expand=YES,fill=BOTH)
        self.e7.pack(expand=YES,fill=BOTH)
        
        #marks entry widget packing
        self.mlbs.pack(expand=YES,fill=BOTH)
        self.me1.pack(expand=YES,fill=BOTH)
        self.me2.pack(expand=YES,fill=BOTH)
        self.me3.pack(expand=YES,fill=BOTH)
        self.me4.pack(expand=YES,fill=BOTH)
        self.me5.pack(expand=YES,fill=BOTH)
        self.me6.pack(expand=YES,fill=BOTH)
        self.me7.pack(expand=YES,fill=BOTH)
        
        #evaluation label packing
        self.lt0.pack(expand=YES,fill=BOTH)
        self.lp0.pack(expand=YES,fill=BOTH)
        self.lg0.pack(expand=YES,fill=BOTH)
        self.lt.pack(expand=YES,fill=BOTH)
        self.lp.pack(expand=YES,fill=BOTH)
        self.lg.pack(expand=YES,fill=BOTH)

        #frame-f5 in f04
        self.f5.pack(expand=YES,fill=BOTH)
        self.bclear.pack(expand=YES,fill=BOTH)
        self.bsave.pack(expand=YES,fill=BOTH)
        self.bundo.pack(expand=YES,fill=BOTH)
        self.bk1.pack(expand=YES,fill=BOTH)

        
        
    def  dbviewer(self):
        
     if(self.seat_no.get()!=0):
        cursor.execute("SELECT * FROM studentresult WHERE seatno='%d'"%(self.seat_no.get()))
        res=tuple()
        res=cursor.fetchone()
        
        self.stud_name.set(res[0])
        self.seat_no.set(res[1])
        self.coursevar.set(res[2])
        self.sexval.set(res[3])
        
        #subject variables
        self.sub1.set(res[4])
        self.sub2.set(res[5])
        self.sub3.set(res[6])
        self.sub4.set(res[7])
        self.sub5.set(res[8])
        self.sub6.set(res[9])
        self.sub7.set(res[10])
        
        #marks variables
        self.m1.set(res[11])
        self.m2.set(res[12])
        self.m3.set(res[13])
        self.m4.set(res[14])
        self.m5.set(res[15])
        self.m6.set(res[16])
        
        
        #evaluation variables
        self.total.set(res[18])
        self.percent.set(res[19])
        self.grade.set(res[20])

        self.top4=Toplevel()#for student result

        #widgets
        
        #frames
        self.fs=Frame(self.top4,height=500,bd=15,width=1000,relief=RIDGE)
        self.fs1=Frame(self.fs,height=250,bd=5,width=500,relief=RIDGE)
        self.fs2=Frame(self.fs,height=250,bd=5,width=500,relief=RIDGE)
        self.fs3=Frame(self.top4,height=250,bd=5,width=500,relief=RIDGE)
        self.fs31=Frame(self.fs3,height=250,bd=5,width=500,relief=RIDGE)
        self.fs32=Frame(self.fs3,height=250,bd=5,width=500,relief=RIDGE)


        

        #labels for student details
        
        self.labsn=Label(self.top4,font=24,fg='green',textvariable=self.stud_name)
        self.labstn=Label(self.top4,font=24,bg='powder blue',fg='green',textvariable=self.seat_no)
        self.labcrs=Label(self.top4,font=24,fg='green',textvariable=self.coursevar)
        

        #labels for displaying subject names
        self.labs1=Label(self.fs1,font=24,fg="green",textvariable=self.sub1,relief=RIDGE)
        self.labs2=Label(self.fs1,font=24,bg='powder blue',fg="green",textvariable=self.sub2,relief=RIDGE)
        self.labs3=Label(self.fs1,font=24,fg="green",textvariable=self.sub3,relief=RIDGE)
        self.labs4=Label(self.fs1,font=24,bg='powder blue',fg="green",textvariable=self.sub4,relief=RIDGE)
        self.labs5=Label(self.fs1,font=24,fg="green",textvariable=self.sub5,relief=RIDGE)
        self.labs6=Label(self.fs1,font=24,bg='powder blue',fg="green",textvariable=self.sub6,relief=RIDGE)
        self.labs7=Label(self.fs1,font=24,fg="green",textvariable=self.sub7,relief=RIDGE)

        #labels for displaying marks 
        self.labm1=Label(self.fs2,font=24,fg="green",textvariable=self.m1,relief=RIDGE)
        self.labm2=Label(self.fs2,font=24,bg='powder blue',fg="green",textvariable=self.m2,relief=RIDGE)
        self.labm3=Label(self.fs2,font=24,fg="green",textvariable=self.m3,relief=RIDGE)
        self.labm4=Label(self.fs2,font=24,bg='powder blue',fg="green",textvariable=self.m4,relief=RIDGE)
        self.labm5=Label(self.fs2,font=24,fg="green",textvariable=self.m5,relief=RIDGE)
        self.labm6=Label(self.fs2,font=24,bg='powder blue',fg="green",textvariable=self.m6,relief=RIDGE)
        self.labm7=Label(self.fs2,font=24,fg="green",textvariable=self.m7,relief=RIDGE)
        
        #eval-labels
        self.lst2=Label(self.fs31,font=24,fg='green',text='The Total is=',relief=RIDGE)
        self.lsp2=Label(self.fs31,font=24,bg='powder blue',fg='green',text='The Percent is=',relief=RIDGE)
        self.lsg2=Label(self.fs31,font=24,fg='green',text="The Grade is=",relief=RIDGE)
        self.lst1=Label(self.fs32,font=24,fg='green',text='The Total is=',textvariable=self.total,relief=RIDGE)
        self.lsp1=Label(self.fs32,font=24,bg='powder blue',fg='green',text='The Percent is=',textvariable=self.percent,relief=RIDGE)
        self.lsg1=Label(self.fs32,font=24,fg='green',text="The Grade is=",textvariable=self.grade,relief=RIDGE)
        
        #buttons
        self.back=Button(self.top4,font=24,text='Back',relief=RIDGE,command=lambda :  self.backf(self.top4))
        
        #packing
        self.top4.minsize(1024,768)
        
        #frames
        self.fs.pack(side=TOP,expand=YES,fill=BOTH)
        self.fs1.pack(side=LEFT,expand=YES,fill=BOTH)
        self.fs2.pack(side=LEFT,expand=YES,fill=BOTH)
        self.fs3.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.fs31.pack(side=LEFT,expand=YES,fill=BOTH)
        self.fs32.pack(side=RIGHT,expand=YES,fill=BOTH)

        #packing labels of fs-frame
        self.labsn.pack(side=TOP,expand=YES,fill=BOTH)
        self.labstn.pack(side=TOP,expand=YES,fill=BOTH)
        self.labcrs.pack(side=TOP,expand=YES,fill=BOTH)

        #packing labels of frame-fs1
        self.labs1.pack(expand=YES,fill=BOTH)
        self.labs2.pack(expand=YES,fill=BOTH)
        self.labs3.pack(expand=YES,fill=BOTH)
        self.labs4.pack(expand=YES,fill=BOTH)
        self.labs5.pack(expand=YES,fill=BOTH)
        self.labs6.pack(expand=YES,fill=BOTH)
        self.labs7.pack(expand=YES,fill=BOTH)
        
        #packing widgets of frame-fs2
        self.labm1.pack(expand=YES,fill=BOTH)
        self.labm2.pack(expand=YES,fill=BOTH)
        self.labm3.pack(expand=YES,fill=BOTH)
        self.labm4.pack(expand=YES,fill=BOTH)
        self.labm5.pack(expand=YES,fill=BOTH)
        self.labm6.pack(expand=YES,fill=BOTH)
        self.labm7.pack(expand=YES,fill=BOTH)
        
        #packing widgets of frame-fs3 fs31 fs32
        self.lst2.pack(side=TOP,expand=YES,fill=BOTH)
        self.lsp2.pack(side=TOP,expand=YES,fill=BOTH)
        self.lsg2.pack(side=TOP,expand=YES,fill=BOTH)
        self.lst1.pack(side=TOP,expand=YES,fill=BOTH)
        self.lsp1.pack(side=TOP,expand=YES,fill=BOTH)
        self.lsg1.pack(side=TOP,expand=YES,fill=BOTH)
        self.back.pack(side=BOTTOM,expand=YES,fill=BOTH)
     else:
          self.dbviewer.withdraw()
        
    def  create_acc(self):
        self.top5=Toplevel()#pendind to add signup widgets & database & button fuctionalities
        #frames
        self.fca=Frame(self.top5,height=500,bd=15,width=1000,relief=RIDGE)
        self.fca1=Frame(self.fca,height=250,bd=5,width=500,relief=RIDGE)
        self.fca2=Frame(self.fca,height=500,bd=5,width=1000,relief=RIDGE)

        #labels
        self.user=Label(self.fca1,font=24,text="enter username:",fg="green",relief=RIDGE)
        self.passwd=Label(self.fca1,font=24,text="password:",fg="green",relief=RIDGE)
        self.cpasswd=Label(self.fca1,font=24,text="confirm password:",fg="green",relief=RIDGE)

        #entries
        self.usern=Entry(self.fca2,font=24,bg='powder blue',fg="green",relief=RIDGE,textvariable=self.usernameval)
        self.passwdn=Entry(self.fca2,font=24,bg='powder blue',show="*",fg="green",relief=RIDGE,textvariable=self.passwordval)
        self.cpasswdn=Entry(self.fca2,font=24,bg='powder blue',fg="green",relief=RIDGE,textvariable=self.passwordval)

        #button
        self.signup=Button(self.top5,font=24,text='signup',relief=RIDGE,command=self.signupf)
        self.back1=Button(self.top5,font=24,text='Back',relief=RIDGE,command=lambda : self.backf(self.top5))

    

        #packing
        self.top5.minsize(1024,768)
        
        #frames
        self.fca.pack(side=TOP,expand=YES,fill=BOTH)
        self.fca1.pack(side=LEFT,expand=YES,fill=BOTH)
        self.fca2.pack(side=RIGHT,expand=YES,fill=BOTH)
        #labels
        self.user.pack(side=TOP,expand=YES,fill=BOTH)
        self.passwd.pack(side=TOP,expand=YES,fill=BOTH)
        self.cpasswd.pack(side=TOP,expand=YES,fill=BOTH)
        #entries
        self.usern.pack(side=TOP,expand=YES,fill=BOTH)
        self.passwdn.pack(side=TOP,expand=YES,fill=BOTH)
        self.cpasswdn.pack(side=TOP,expand=YES,fill=BOTH)
        #buttons
        self.signup.pack(side=BOTTOM,expand=YES,fill=BOTH)
        self.back1.pack(side=BOTTOM,expand=YES,fill=BOTH)
        

    def  signupf(self):
         #Drops if already exists
        cursor.execute("DROP TABLE IF EXISTS TEACHERLOG ")
        #creating teacherlog table
        cursor.execute("""CREATE TABLE TEACHERLOG(USERNAME TEXT ,PASSWORD TEXT NOT NULL,PRIMARY KEY(USERNAME))""")

        cursor.execute('INSERT INTO TEACHERLOG(USERNAME,PASSWORD) VALUES(?,?)',(self.usernameval.get(),self.passwordval.get()))
        try:
            db.commit()
        except:
             db.rollback()
        finally:
            
            self.dbopener() 


    def  backf (self,widget):
        self.widget=widget
        self.widget.withdraw()
         
    def  clearf(self):
        self.stud_name.set(0)
        self.seat_no.set(0)
        self.coursevar.set(0)
        self.sexval.set(0)
        
        #subject variables
        self.sub1.set(0)
        self.sub2.set(0)
        self.sub3.set(0)
        self.sub4.set(0)
        self.sub5.set(0)
        self.sub6.set(0)
        self.sub7.set(0)
        
        #marks variables
        self.m1.set(0)
        self.m2.set(0)
        self.m3.set(0)
        self.m4.set(0)
        self.m5.set(0)
        self.m6.set(0)
        self.m7.set(0)
        
        
        #evaluation variables
        self.total.set(0)
        self.percent.set(0)
        self.grade.set(0)

         
    def  undof(self):
        
         db.rollback()
         
         
    def  calf(self):
         #evaluating
        self.total.set(self.m1.get()+self.m2.get()+self.m3.get()+self.m4.get()+self.m5.get()+self.m6.get()+self.m7.get())
        self.percent.set(self.total.get()/7)
        self.per=float(self.percent.get())
        if (self.per >= 85.0):
            self.grade.set('o')
        elif (self.per < 85.0) and (self.per >=75.0):
            self.grade.set('A')
        elif (self.per < 75.0) and (self.per >=65.0):
            self.grade.set('B')
        elif (self.per < 65.0) and (self.per >=55.0):
            self.grade.set('C')
        elif (self.per < 55.0) and (self.per >=45.0):
            self.grade.set('D')
        elif (self.per < 45.0) and (self.per >=35.0):
            self.grade.set('E')
        else:
            self.grade.set('F')    
            
            
         
    def  savef(self):
        #drop if exists
        cursor.execute('DROP TABLE IF EXISTS studentresult')
        #creating table
        cursor.execute('''CREATE TABLE studentresult(studname TEXT NOT NULL,seatno INT NOT NULL,gender TEXT NOT NULL,course TEXT NOT NULL,
                 S1 TEXT, S2 TEXT,S3 TEXT,S4 TEXT,S5 TEXT,S6 TEXT,S7 TEXT,
                 M1 INTEGER,M2 INTEGER,M3 INTEGER,M4 INTEGER, M5 INTEGER,M6 INTEGER, M7 INTEGER,
                 TOTAL INTEGER,PERCENT REAL,GRADE TEXT, PRIMARY KEY(seatno))''')
        cursor.execute('INSERT INTO studentresult (studname,seatno,gender,course,S1,S2,S3,S4,S5,S6,S7,M1,M2,M3,M4,M5,M6,M7,TOTAL,PERCENT,GRADE)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,
                       (self.stud_name.get(),self.seat_no.get(),self.sexval.get(),self.coursevar.get(),
                        self.sub1.get(),self.sub2.get(),self.sub3.get(),self.sub4.get(),self.sub5.get(),self.sub6.get(),self.sub7.get(),
                        self.m1.get(),self.m2.get(),self.m3.get(),self.m4.get(),self.m5.get(),self.m6.get(),self.m7.get(),
                        self.total.get(),self.percent.get(),self.grade.get()))
        db.commit()
        
        
    def loginf(self):
        try:
            if (self.usernameval.get()!=0):
                 cursor.execute("SELECT * FROM TEACHERLOG WHERE USERNAME='%s'"%(self.usernameval.get()))
                 teacher=tuple()
                 teacher=cursor.fetchone()
                 if (self.passwordval.get()==teacher[1]):
                         self.dbopener()
                 else:
                         self.create_acc()
        except:
            print('invalid login credentials')
             
        finally:
            
            self.dbopener()
            
            
            
                       
                       
        
        
        
        
        


        
root=Tk()
root.geometry('1024x768')
a=resplay(root)
root.mainloop()
