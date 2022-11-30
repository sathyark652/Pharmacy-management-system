from tkinter import  *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql

def insert():
    id=e_id.get();
    fname=e_fname.get();
    lname=e_lname.get();
    gender=e_gender.get();
    dob=e_dob.get();
    phone=e_phone.get();
    address=e_address.get();
    if(id=="" or fname==""  or lname==""or gender =="" or dob=="" or phone =="" or address==""):
        Messagebox.showinfo("insert status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="sathya",password="Sathya652",database="pharmacy_ms")
        cursor=con.cursor()
        cursor.execute("insert into customer values(' "+ id +" ' ,' "+ fname +" ',' "+ lname +" ',' "+ gender +" ',' "+ dob +" ',' "+ phone +" ',' "+ address +" ')")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_dob.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_address .delete(0, 'end')
        show()
        Messagebox.showinfo("insert status","inserted succesfully");
        con.close();
        
def delete():
    if(e_id.get()  ==  ""):
        Messagebox.showinfo("delete status","Id is mandatory for delete")
    else:
        con = mysql.connect(host="localhost",user="sathya",password="Sathya652",database="pharmacy_ms")
        cursor = con.cursor()
        cursor.execute("delete from customer  where cust_id= ' "+ e_id.get() +" ' ")
        cursor.execute("commit");
        
        e_id.delete(0, 'end')
        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_dob.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_address .delete(0, 'end')
        show()
        Messagebox.showinfo("delete status","delete succesfully");
        con.close();

def update():
    id=e_id.get();
    fname=e_fname.get();
    lname=e_lname.get();
    gender=e_gender.get();
    dob=e_dob.get();
    phone=e_phone.get();
    address=e_address.get();
    if(id=="" or fname=="" ): 
        Messagebox.showinfo("update status","all fields are required")
    else:
        con=mysql.connect(host="localhost",user="sathya",password="Sathya652",database="pharmacy_ms")
        cursor=con.cursor()
        cursor.execute("update customer set fname=' "+ fname +" ' where cust_id=' "+id+" ' ")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_fname.delete(0, 'end')
        e_lname.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_dob.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_address .delete(0, 'end')
        show()
        Messagebox.showinfo("update status","update succesfully");
        con.close();

def get():
    if(e_id.get() == ""):
        Messagebox.showinfo("fetch status","fetched succesfully");
    else:
        con=mysql.connect(host="localhost",user="sathya",password="Sathya652",database="pharmacy_ms")
        cursor=con.cursor()
        cursor.execute("select * from customer where cust_id = ' "+e_id.get()+" ' ")
        rows=cursor.fetchall()

        for row in rows:
            e_fname.insert(0, row[1])
            e_lname.insert(0, row[2])
            e_gender.insert(0, row[3])
            e_dob.insert(0, row[4])
            e_phone.insert(0, row[5])
            e_address.insert(0, row[6]) 
            
        con.close();

def show():
     con=mysql.connect(host="localhost",user="sathya",password="Sathya652",database="pharmacy_ms")
     cursor=con.cursor()
     cursor.execute("select * from customer")
     rows=cursor.fetchall()
     list.delete(0, list.size())
     
     for row in rows:
        insertData= str(row[0])+'          '+row[1]  + '       '+row[2] + '      ' + row[3] +'      '+str(row[4])+'     '+str(row[5])+'     '+ row[6]
        list.insert(list.size()+1,insertData)
    



root = Tk()
root.geometry("900x600")
root.title("PHARMACY MANAGEMENT SYSTEM")

id = Label(root,text='Enter customer Id',font=('bold',10))
id.place(x=20,y=50)

fname = Label(root,text='Enter first name',font=('bold',10))
fname.place(x=20,y=70)

lname = Label(root,text='Enter last name',font=('bold',10))
lname.place(x=20,y=90)

gender = Label(root,text='Enter Gender',font=('bold',10))
gender.place(x=20,y=120)

dob = Label(root,text='Enter date of birth',font=('bold',10))
dob.place(x=20,y=140)

phone = Label(root,text='Enter Phone number',font=('bold',10))
phone.place(x=20,y=160)

address = Label(root,text='Enter Address',font=('bold',10))
address.place(x=20,y=180)

e_id=Entry()
e_id.place(x=150,y=50)

e_fname=Entry()
e_fname.place(x=150,y=70)

e_lname=Entry()
e_lname.place(x=150,y=90)

e_gender=Entry()
e_gender.place(x=150,y=120)

e_dob=Entry()
e_dob.place(x=150,y=140)

e_phone=Entry()
e_phone.place(x=150,y=160)

e_address=Entry()
e_address.place(x=150,y=180)


insert=Button(root,text='insert',font=('italic',10),bg='white',command=insert)
insert.place(x=20,y=220)

delete=Button(root,text='delete',font=('italic',10),bg='white',command=delete)
delete.place(x=70,y=240)

update=Button(root,text='update',font=('italic',10),bg='white',command=update)
update.place(x=130,y=260)

get=Button(root,text='get',font=('italic',10),bg='white',command=get)
get.place(x=190,y=280)

list=Listbox(root,height=20,width=90)
list.place(x=350,y=200)
show()

root.mainloop()














