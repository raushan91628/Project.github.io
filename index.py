from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("PPWP ")
screen.geometry("20000x1000")

def register():
    Name=Name_info.get()
    Age = Age_info.get()
    Phone = Phone_info.get()
    Email = Email_info.get()
    Address = Address_info.get()
    Adhar = Adhar_info.get()
    State=State_info.get()
    Pincode=Pincode_info.get()
    District= District_info.get()
    Block = Block_info.get()
    PoliceStation = PoliceStation_info.get()
    Profession = Profession_info.get()
    Cast =  Cast_info.get()
    Gender =Gender_info.get()

    if Name == "":
        messagebox.showerror("Error", "Enter your name")
    elif Age == "":
        messagebox.showerror("Error", "Enter your Age")
    elif Phone == "":
        messagebox.showerror("Error", "Enter your Phone")
    elif Email == "":
        messagebox.showerror("Error", "Enter your Email")
    elif Address == "":
        messagebox.showerror("Error", "Enter your Address")
    elif Adhar == "":
        messagebox.showerror("Error", "Enter your Adhar")
    elif State == "":
        messagebox.showerror("Error", "Enter your State")
    elif Pincode =="":
        messagebox.showerror("Error", "Enter your Pincode")
    elif District == "":
        messagebox.showerror("Error", "Enter your District")
    elif Block == "":
        messagebox.showerror("Error", "Enter your Block")
    elif  PoliceStation == "":
        messagebox.showerror("Error", "Enter your  PoliceStation ")
    elif  Profession  == "":
        messagebox.showerror("Error", "Enter your   Profession  ")
    elif  Cast == "":
        messagebox.showerror("Error", "Enter your    Cast  ")
    elif  Gender == "":
        messagebox.showerror("Error", "Enter your    Gender  ")

    else:
        Label(screen,text="Registation successfull",font="40" ,fg="green").place(x=1000,y=700)

    with open(Name+ ".txt","w") as f:
     f.write("name=" + Name + "\n")
     f.write("Age=" + Age + "\n")
     f.write("Phone=" + Phone + "\n")
     f.write("Email=" + Email + "\n")
     f.write("Address=" + Address + "\n")
     f.write("Adhar=" + Adhar + "\n")
     f.write("State=" + State + "\n")
     f.write("Pincode=" + Pincode + "\n")
     f.write("District=" + District + "\n")
     f.write("Block=" + Block + "\n")
     f.write("PoliceStation=" + PoliceStation + "\n")
     f.write("Profession=" + Profession+ "\n")
     f.write("Cast=" + Cast + "\n")
     f.write("Gender=" + Gender + "\n")


    def clear():
        pass


#label
Label(screen,text="PPWP",font="50",bg="yellow",fg="white").pack(fill="both")

Label(screen,text="Name",font="20").place(x=30,y=70)
Label(screen,text="Age",font="20").place(x=30,y=140)
Label(screen,text="Phone",font="20").place(x=30,y=210)
Label(screen,text="Email",font="20").place(x=30,y=280)
Label(screen,text="Address",font="20").place(x=30,y=350)
Label(screen,text="Adhar",font="20").place(x=30,y=420)
Label(screen,text="State",font="20").place(x=30,y=500)
Label(screen,text="Pincode",font="20").place(x=900,y=70)
Label(screen,text="District",font="20").place(x=900,y=140)
Label(screen,text="Block",font="20").place(x=900,y=210)
Label(screen,text="PoliceStation",font="20").place(x=860,y=280)
Label(screen,text="Profession",font="20").place(x=880,y=350)
Label(screen,text="Cast",font="20").place(x=900,y=420)
Label(screen,text="Gender",font="20").place(x=900,y=500)
#Label(screen,text="Image",font="20").place(x=1000,y=700)


#entry
Name_info=StringVar()
Age_info=StringVar()
Phone_info=StringVar()
Email_info=StringVar()
Address_info=StringVar()
Adhar_info=StringVar()
State_info=StringVar()
Pincode_info=StringVar()
District_info=StringVar()
Block_info=StringVar()
PoliceStation_info=StringVar()
Profession_info=StringVar()
Cast_info=StringVar()
Gender_info=StringVar()
name_entry=Entry(screen , font="10",textvariable=Name_info)
name_entry.place(x=140,y=75)
Age_entry=Entry(screen , font="10",textvariable=Age_info)
Age_entry.place(x=140,y=140)
Phone_entry=Entry(screen , font="10",textvariable=Phone_info)
Phone_entry.place(x=140,y=210)
Email_entry=Entry(screen , font="10",textvariable=Email_info)
Email_entry.place(x=140,y=280)
Address_entry=Entry(screen , font="10",textvariable=Address_info)
Address_entry.place(x=140,y=350)
Adhar_entry=Entry(screen , font="10",textvariable=Adhar_info)
Adhar_entry.place(x=140,y=420)
State_entry=Entry(screen , font="10",textvariable=State_info)
State_entry.place(x=140,y=500)
Pincode_entry=Entry(screen , font="10",textvariable=Pincode_info)
Pincode_entry.place(x=1000,y=75)
District_entry=Entry(screen , font="10",textvariable=District_info)
District_entry.place(x=1000,y=140)
Block_entry=Entry(screen , font="10",textvariable=Block_info)
Block_entry.place(x=1000,y=210)
PoliceStation_entry=Entry(screen , font="10",textvariable=PoliceStation_info)
PoliceStation_entry.place(x=1000,y=280)
Profession_entry=Entry(screen , font="10",textvariable=Profession_info)
Profession_entry.place(x=1000,y=350)
Cast_entry=Entry(screen , font="10",textvariable=Cast_info)
Cast_entry.place(x=1000,y=420)
Gender_entry=Entry(screen , font="10",textvariable=Gender_info)
Gender_entry.place(x=1000,y=500)
# Image_entry=file(screen , font="10",textvariable=Pincode_info)
# Image_entry.place(x=900,y=700)

#button
# Button(screen , text="uplode" , font="20", command=uploded).place(x=1000 , y=700)
Button(screen , text="Register" , font="20", command=register).place(x=1200 , y=700)
Button(screen , text="clear" , font="20"  ).place(x=1400 , y=700)
mainloop()
