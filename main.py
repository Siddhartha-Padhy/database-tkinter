from tkinter import *
import tkinter
from PIL import Image,ImageTk
import mysql.connector
import sqlite3

root=Tk()
root.iconbitmap('C:/Users/Dell/OneDrive/Desktop/Projects/Python/tkinter/iconex.ico')
root.config(background="#077b8a")
root.geometry("485x600")
root.title("Data Base Interface")
root.maxsize(485,600)

# Entries
f_name=Entry(root,width=40,borderwidth=3, relief="sunken")
l_name=Entry(root,width=40,borderwidth=3, relief="sunken")
address=Entry(root,width=40,borderwidth=3, relief="sunken")
city=Entry(root,width=40,borderwidth=3, relief="sunken")
state=Entry(root,width=40,borderwidth=3, relief="sunken")
select_rec=Entry(root,width=40,borderwidth=3, relief="sunken")

head_text=Label(root,text="Address Records",bg="#d72631",fg="#5c3c92",font=("helvetica",20,"bold"),borderwidth=3, relief="ridge").grid(column=0,row=0,columnspan=2,pady=25,ipadx=125,ipady=18)

# Labels
f_name_lab=Label(root,text="First Name:",bg="#077b8a",fg="black").grid(column=0,row=1,padx=5)
l_name_lab=Label(root,text="Last Name:",bg="#077b8a",fg="black").grid(column=0,row=2,padx=5)
address_lab=Label(root,text="Address:",bg="#077b8a",fg="black").grid(column=0,row=3,padx=5)
city_lab=Label(root,text="City:",bg="#077b8a",fg="black").grid(column=0,row=4,padx=5)
state_lab=Label(root,text="State:",bg="#077b8a",fg="black").grid(column=0,row=5,padx=5)
select_rec_lab=Label(root,text="ID for modification:",bg="#077b8a",fg="black").grid(column=0,row=8,padx=5)

#database
conn=sqlite3.connect('address_book.db')
c=conn.cursor()
# Uncomment the below code when running for first time then comment it out again
# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text
#     )""")

# Functions
def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("DELETE from addresses WHERE oid="+select_rec.get())
    select_rec.delete(0,END)
    conn.commit()
    conn.close()

def edit():
    top=Toplevel()
    top.title("Edit Details")
    top.geometry("485x600")
    top.maxsize(485,600)
    top.iconbitmap('C:/Users/Dell/OneDrive/Desktop/Projects/Python/tkinter/iconex.ico')
    top.config(background="#077b8a")

    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    record_id=select_rec.get()
    c.execute("SELECT * FROM addresses WHERE oid="+record_id)
    records=c.fetchall()

    f_name_edit=Entry(top,width=40,borderwidth=3, relief="sunken")
    l_name_edit=Entry(top,width=40,borderwidth=3, relief="sunken")
    address_edit=Entry(top,width=40,borderwidth=3, relief="sunken")
    city_edit=Entry(top,width=40,borderwidth=3, relief="sunken")
    state_edit=Entry(top,width=40,borderwidth=3, relief="sunken")

    for record in records:
        f_name_edit.insert(0,record[0])
        l_name_edit.insert(1,record[1])
        address_edit.insert(2,record[2])
        city_edit.insert(3,record[3])
        state_edit.insert(4,record[4])

    def save():
        conn=sqlite3.connect('address_book.db')
        c=conn.cursor()
        c.execute("""UPDATE addresses SET
            first_name=:first,
            last_name=:last,
            address=:address,
            city=:city,
            state=:state
            WHERE oid=:oid""",
            {
                'first':f_name_edit.get(),
                'last':l_name_edit.get(),
                'address':address_edit.get(),
                'city':city_edit.get(),
                'state':state_edit.get(),
                'oid':record_id
            })
        conn.commit()
        conn.close()
        top.destroy()

    head_text=Label(top,text="Modify Record",bg="#d72631",fg="#5c3c92",font=("helvetica",20,"bold"),borderwidth=3, relief="ridge").grid(column=0,row=0,columnspan=2,pady=25,ipadx=125,ipady=18)

    f_name_lab=Label(top,text="First Name:",bg="#077b8a",fg="black").grid(column=0,row=1,padx=5)
    l_name_lab=Label(top,text="Last Name:",bg="#077b8a",fg="black").grid(column=0,row=2,padx=5)
    address_lab=Label(top,text="Address:",bg="#077b8a",fg="black").grid(column=0,row=3,padx=5)
    city_lab=Label(top,text="City:",bg="#077b8a",fg="black").grid(column=0,row=4,padx=5)
    state_lab=Label(top,text="State:",bg="#077b8a",fg="black").grid(column=0,row=5,padx=5)


    f_name_edit.grid(column=1,row=1,padx=5)
    l_name_edit.grid(column=1,row=2,padx=5)
    address_edit.grid(column=1,row=3,padx=5)
    city_edit.grid(column=1,row=4,padx=5)
    state_edit.grid(column=1,row=5,padx=5)

    save_btn=Button(top,text="Save",bg="blue",fg="white",command=save).grid(column=0,row=6,columnspan=2,pady=15,ipadx=20)

def show():
    showcase=Toplevel()
    showcase.title("Records")
    showcase.geometry("485x600")
    showcase.iconbitmap('C:/Users/Dell/OneDrive/Desktop/Projects/Python/tkinter/iconex.ico')
    showcase.config(background="#077b8a")

    head_text=Label(showcase,text="Records",bg="#d72631",fg="#5c3c92",font=("helvetica",20,"bold"),borderwidth=3, relief="ridge").grid(column=0,row=0,columnspan=2,pady=25,ipadx=184,ipady=18)

    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print(records)

    show_records=""
    for record in records:
        show_records+= str(record[5])+": "+ record[0] +" "+ record[1] +"\n\t"+ record[2] + ", "+record[3] + ", " +record[4] + "\n"
    
    show_lab=Label(showcase,text=show_records,justify=LEFT,bg="#077b8a",font=("helvetica",13))
    show_lab.grid(row=11,column=0,columnspan=2)

    conn.commit()
    conn.close()



def submit():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get()
    })

    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)

# Placing the stuffs
f_name.grid(column=1,row=1,padx=5)
l_name.grid(column=1,row=2,padx=5)
address.grid(column=1,row=3,padx=5)
city.grid(column=1,row=4,padx=5)
state.grid(column=1,row=5,padx=5)
select_rec.grid(column=1,row=8,padx=5)

sub_btn=Button(root,text="Submit",bg="green",fg="white",command=submit).grid(column=0,row=6,columnspan=2,pady=10,ipadx=60)

show_btn=Button(root,text="Show",bg="blue",fg="white",command=show).grid(column=0,row=7,columnspan=2,pady=5,ipadx=64)

edit_btn=Button(root,text="Edit",bg="blue",fg="white",command=edit).grid(column=0,row=9,pady=10,ipadx=70,columnspan=2)

delete_btn=Button(root,text="Delete",bg="red",fg="white",command=delete).grid(column=0,row=10,pady=10,ipadx=62,columnspan=2)

conn.commit()
conn.close()

root.mainloop(0)