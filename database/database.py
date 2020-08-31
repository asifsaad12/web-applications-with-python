from tkinter import*
import sqlite3

root=Tk()
root.title("my database")


##create a database or connect to one
con=sqlite3.connect('student_books.db')

##create a cursor
c=con.cursor()
c.execute("""CREATE TABLE students(name text,roll integer,city text,zipcode integer)""")

def upgrade():
    con=sqlite3.connect('student_books.db')
    c=con.cursor()

    #top=Toplevel()
    #Label(top,text=name.get()).pack()
    #Label(top,text=roll.get()).pack()
    #Label(top,text=home.get()).pack()
    #Label(top,text=zipcode.get()).pack()
    #Label(top,text=edit_box.get()).pack()

    c.execute("""UPDATE students SET name=:name,roll=:roll,city=:city,zipcode=:zipcode WHERE oid=:oid""",
        {'name':name.get(),'roll':roll.get(),'city':home.get(),'zipcode':zipcode.get(),'oid':val})
    
    name.delete(0,END)
    roll.delete(0,END)
    home.delete(0,END)
    zipcode.delete(0,END)

    con.commit()
    con.close()





def update():

    con=sqlite3.connect('student_books.db')
    c=con.cursor()
    global val 
    val=edit_box.get()
    c.execute("SELECT * FROM students WHERE oid= " + edit_box.get())
    records=c.fetchall()
    con.commit()
    con.close()

    for record in records:
        name.insert(0,record[0])
        roll.insert(0,record[1])
        home.insert(0,record[2])
        zipcode.insert(0,record[3])

    edit_box.delete(0,END)





##delete an element of a database
def delete():
    con=sqlite3.connect('student_books.db')

    c=con.cursor()


    #delete a record
    c.execute("DELETE from students WHERE oid = " + delete_box.get())
    delete_box.delete(0,END)

    con.commit()
    con.close()

    name.delete(0,END)
    roll.delete(0,END)
    home.delete(0,END)
    zipcode.delete(0,END)



def fun(record1):
    top=Toplevel()
    top.title("records of database")
    Label(top,text=record1,width=50).pack()


#query function
def query():
    con=sqlite3.connect('student_books.db')

    c=con.cursor()


    c.execute("SELECT *,oid FROM students")

    recordval=c.fetchall()

    printvalue=''
    for record in recordval:

        printvalue+=str(record)+'\n'

    fun(printvalue)


    con.commit()

    con.close()



def submit():

    con=sqlite3.connect('student_books.db')

    c=con.cursor()


    c.execute("INSERT INTO students VALUES (:name,:roll,:city,:zipcode)",
    {'name':name.get(),
    'roll':roll.get(),
    'city':home.get(),
    'zipcode':zipcode.get()
    })

    con.commit()

    con.close()

    name.delete(0,END)
    roll.delete(0,END)
    home.delete(0,END)
    zipcode.delete(0,END)






name=Entry(root,width=70)
name.grid(row=0,column=1,pady=(10,0))
roll=Entry(root,width=70)
roll.grid(row=1,column=1)
home=Entry(root,width=70)
home.grid(row=2,column=1)
zipcode=Entry(root,width=70)
zipcode.grid(row=3,column=1)
delete_box=Entry(root,width=70)
delete_box.grid(row=6,column=1,pady=(0,10))
edit_box=Entry(root,width=70)
edit_box.grid(row=8,column=1,pady=(0,10))



name_label=Label(root,text='name')
name_label.grid(row=0,column=0,pady=(10,0))
roll_label=Label(root,text='roll')
roll_label.grid(row=1,column=0)
home_label=Label(root,text='home city')
home_label.grid(row=2,column=0)
zipcode_label=Label(root,text='zip code')
zipcode_label.grid(row=3,column=0)
delete_label=Label(root,text='delete id')
delete_label.grid(row=6,column=0,pady=(0,10))
edit_label=Label(root,text='update id')
edit_label.grid(row=8,column=0,pady=(0,10))


submit_btn=Button(root,text='submit your data here',command=submit)
submit_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=5,ipadx=183)

qry_btn=Button(root,text='show the database',command=query)
qry_btn.grid(row=5,column=0,columnspan=2,padx=5,pady=5,ipadx=192)


##create a delete button
delete_btn=Button(root,text='delete the inserted in above entry',command=delete)
delete_btn.grid(row=7,column=0,columnspan=2,padx=5,pady=5,ipadx=153)

#create a edit button
edit_btn=Button(root,text='show the selected id in above entry',command=update)
edit_btn.grid(row=9,column=0,columnspan=2,padx=5,pady=5,ipadx=150)



upgrade_btn=Button(root,text='save the upgraded records',command=upgrade)
upgrade_btn.grid(row=10,column=0,columnspan=2,padx=5,pady=5,ipadx=173)


con.commit()
##close connection
con.close()

root.mainloop()