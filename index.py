from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk


#
screen=Tk()
screen.title("JSECMB ")
screen.geometry("20000x1000")

def next():
    screen = tk.Tk()
    screen.title("hello")
    screen.configure(bg="blue")
    screen.geometry("20000x1000")
    def school():
        screen = tk.Tk()
        screen.geometry("20000x1000")
        # screen.config()
        # screen.split()
        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()



            if  " ":
                messagebox.showinfo("Welcome","Registation successfull")
            elif  Name=="":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
        # #
            with open(Name + ".txt", "w") as f:
                 f.write("name=" + Name + "\n")
                 f.write("Age=" + Age + "\n")
                 f.write("Phone=" + Phone + "\n")
                 f.write("Email=" + Email + "\n")
                 f.write("Address=" + Address + "\n")
                 f.write("Education=" + Education + "\n")
                 f.write("Skill=" + Skill + "\n")
                 f.write("Experience=" + Experience + "\n")
                 f.write("District=" + District + "\n")
                 f.write("Block=" + Block + "\n")
                 f.write("State=" + State + "\n")
                 f.write("Profession=" + Profession + "\n")
                 f.write("Cast=" + Cast + "\n")
                 f.write("Gender=" + Gender + "\n")
                 # f.write("Uplode_CV=" + Uplode_CV + "\n")
                 f.write("values=" + values + "\n")

        # #
        # #     # with open( Uplode+ ".pdf","w") as f:
        # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

        # def uplode():
        #     # pass
        #     # image_names()= uplode( ".jpg ", ".pdf")
        #     file = filedialog.askopenfilename()
        #     file_name = file.name
        #     Label.config(text=file)

        # label
        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['computer teacher requirement in DPS school', 'Python development teacher requirement in DPS school',
                         'Chemistry teacher requirement in DAV school', 'Physics teacher requirement in DAV school','Assistance professor requirement in DPS school']
        com.place(x=300, y=600)


    Button(screen,text="SCHOOL" ,font="20",bg="green" , command=school).place(x=115,y=460)

    def show():
        screen =Tk()
        screen.title("hello")
        screen.geometry("2000x1000")

        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()

            if " ":
                messagebox.showinfo("Welcome", "Registation successfull")
            elif Name == "":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
            # #
            with open(Name + ".txt", "w") as f:
                f.write("name=" + Name + "\n")
                f.write("Age=" + Age + "\n")
                f.write("Phone=" + Phone + "\n")
                f.write("Email=" + Email + "\n")
                f.write("Address=" + Address + "\n")
                f.write("Education=" + Education + "\n")
                f.write("Skill=" + Skill + "\n")
                f.write("Experience=" + Experience + "\n")
                f.write("District=" + District + "\n")
                f.write("Block=" + Block + "\n")
                f.write("State=" + State + "\n")
                f.write("Profession=" + Profession + "\n")
                f.write("Cast=" + Cast + "\n")
                f.write("Gender=" + Gender + "\n")
                # f.write("Uplode_CV=" + Uplode_CV + "\n")
                f.write("values=" + values + "\n")

            # #
            # #     # with open( Uplode+ ".pdf","w") as f:
            # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

            # def uplode():
            #     # pass
            #     # image_names()= uplode( ".jpg ", ".pdf")
            #     file = filedialog.askopenfilename()
            #     file_name = file.name
            #     Label.config(text=file)

            # label

        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['Data Entry operator requirement in Relince', 'Accountent requirement in Relince',
                         'Assistance mennager requirement', 'Management Requirement in Aditya vision',
                         'Gard requirement in aditya vision']
        com.place(x=300, y=600)

    Button(screen, text="SHOW ROOM", font="20",bg="green", command=show).place(x=100, y=520)
    def COLLEGE():
        screen =Tk()
        screen.title("hello")
        screen.geometry("2000x1000")

        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()

            if " ":
                messagebox.showinfo("Welcome", "Registation successfull")
            elif Name == "":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
            # #
            with open(Name + ".txt", "w") as f:
                f.write("name=" + Name + "\n")
                f.write("Age=" + Age + "\n")
                f.write("Phone=" + Phone + "\n")
                f.write("Email=" + Email + "\n")
                f.write("Address=" + Address + "\n")
                f.write("Education=" + Education + "\n")
                f.write("Skill=" + Skill + "\n")
                f.write("Experience=" + Experience + "\n")
                f.write("District=" + District + "\n")
                f.write("Block=" + Block + "\n")
                f.write("State=" + State + "\n")
                f.write("Profession=" + Profession + "\n")
                f.write("Cast=" + Cast + "\n")
                f.write("Gender=" + Gender + "\n")
                # f.write("Uplode_CV=" + Uplode_CV + "\n")
                f.write("values=" + values + "\n")

            # #
            # #     # with open( Uplode+ ".pdf","w") as f:
            # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

            # def uplode():
            #     # pass
            #     # image_names()= uplode( ".jpg ", ".pdf")
            #     file = filedialog.askopenfilename()
            #     file_name = file.name
            #     Label.config(text=file)

            # label

        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['computer teacher requirement in LND college', 'Python development teacher requirement in MS college',
                         'Math teacher requirement in LNd college', 'C++ teacher requirement in SNS college',
                         'Gegraphy teacher requirement in SKS college motihari']
        com.place(x=300, y=600)

    Button(screen, text="COLLEGE", font="20",bg="green", command=COLLEGE).place(x=600, y=460)
    def medical():
        screen =Tk()
        screen.title("hello")
        screen.geometry("2000x1000")

        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()

            if " ":
                messagebox.showinfo("Welcome", "Registation successfull")
            elif Name == "":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
            # #
            with open(Name + ".txt", "w") as f:
                f.write("name=" + Name + "\n")
                f.write("Age=" + Age + "\n")
                f.write("Phone=" + Phone + "\n")
                f.write("Email=" + Email + "\n")
                f.write("Address=" + Address + "\n")
                f.write("Education=" + Education + "\n")
                f.write("Skill=" + Skill + "\n")
                f.write("Experience=" + Experience + "\n")
                f.write("District=" + District + "\n")
                f.write("Block=" + Block + "\n")
                f.write("State=" + State + "\n")
                f.write("Profession=" + Profession + "\n")
                f.write("Cast=" + Cast + "\n")
                f.write("Gender=" + Gender + "\n")
                # f.write("Uplode_CV=" + Uplode_CV + "\n")
                f.write("values=" + values + "\n")

            # #
            # #     # with open( Uplode+ ".pdf","w") as f:
            # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

            # def uplode():
            #     # pass
            #     # image_names()= uplode( ".jpg ", ".pdf")
            #     file = filedialog.askopenfilename()
            #     file_name = file.name
            #     Label.config(text=file)

            # label

        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['Data Entry operator requirement dr prakesh khetan', 'Accountent requirement in Rahaminia',
                         'Assistance mennager requirement in sambhu saran', 'Management Requirement in santosh kumar',
                         'Gard requirement in Dr manoj kumar']
        com.place(x=300, y=600)

    Button(screen, text="   MEDICAL", font="20",bg="green", command=medical).place(x=600, y=520)
    def computer():
        screen =Tk()
        screen.title("hello")
        screen.geometry("2000x1000")

        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()

            if " ":
                messagebox.showinfo("Welcome", "Registation successfull")
            elif Name == "":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
            # #
            with open(Name + ".txt", "w") as f:
                f.write("name=" + Name + "\n")
                f.write("Age=" + Age + "\n")
                f.write("Phone=" + Phone + "\n")
                f.write("Email=" + Email + "\n")
                f.write("Address=" + Address + "\n")
                f.write("Education=" + Education + "\n")
                f.write("Skill=" + Skill + "\n")
                f.write("Experience=" + Experience + "\n")
                f.write("District=" + District + "\n")
                f.write("Block=" + Block + "\n")
                f.write("State=" + State + "\n")
                f.write("Profession=" + Profession + "\n")
                f.write("Cast=" + Cast + "\n")
                f.write("Gender=" + Gender + "\n")
                # f.write("Uplode_CV=" + Uplode_CV + "\n")
                f.write("values=" + values + "\n")

            # #
            # #     # with open( Uplode+ ".pdf","w") as f:
            # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

            # def uplode():
            #     # pass
            #     # image_names()= uplode( ".jpg ", ".pdf")
            #     file = filedialog.askopenfilename()
            #     file_name = file.name
            #     Label.config(text=file)

            # label

        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['Data Entry operator requirement in LND college', 'java developer requirement in appycrown',
                         'Assistance operator requirement in aditya vision', 'server controler requirement Aditya vision',
                         'Gard requirement in Ms college']
        com.place(x=300, y=600)

    Button(screen, text="COMPUTER", font="20",bg="green", command=computer).place(x=1200, y=460)
    def electric():
        screen =Tk()
        screen.title("hello")
        screen.geometry("2000x1000")

        def register():
            Name = Name_info.get()
            Age = Age_info.get()
            Phone = Phone_info.get()
            Email = Email_info.get()
            Address = Address_info.get()
            Education = Education_info.get()
            Skill = Skill_info.get()
            Experience = Experience_info.get()
            District = District_info.get()
            Block = Block_info.get()
            State = State_info.get()
            Profession = Profession_info.get()
            Cast = Cast_info.get()
            Gender = Gender_info.get()
            Uplode = Uplode_info.get()
            values = values_info.get()

            if " ":
                messagebox.showinfo("Welcome", "Registation successfull")
            elif Name == "":
                messagebox.showerror("Error", "Please Enter your name")
            elif Age == "":
                messagebox.showerror("Error", "Please Enter your Age")
            elif Phone == "":
                messagebox.showerror("Error", "Please Enter your Phone")
            elif Email == "":
                messagebox.showerror("Error", "Please Enter your Email")
            elif Address == "":
                messagebox.showerror("Error", "Please Enter your Address")
            elif Education == "":
                messagebox.showerror("Error", "Please Enter your Education")
            elif Skill == "":
                messagebox.showerror("Error", " Please Enter your Skill")
            elif Experience == "":
                messagebox.showerror("Error", "Please Enter your Experience")
            elif District == "":
                messagebox.showerror("Error", "Please Enter your District")
            elif Block == "":
                messagebox.showerror("Error", "Please Enter your Block")
            elif State == "":
                messagebox.showerror("Error", " Please Enter your  State ")
            elif Profession == "":
                messagebox.showerror("Error", "Please Enter your   Profession  ")
            elif Cast == "":
                messagebox.showerror("Error", "Please Enter your    Cast  ")
            elif Gender == "":
                messagebox.showerror("Error", " Please Enter your    Gender  ")
            elif values == "":
                messagebox.showerror("Error", "Please Enter your   Avaliable jobs ")

            else:
                Label(screen, text="Registation successfull", font="40", fg="green").place(x=800, y=700)
            # #
            with open(Name + ".txt", "w") as f:
                f.write("name=" + Name + "\n")
                f.write("Age=" + Age + "\n")
                f.write("Phone=" + Phone + "\n")
                f.write("Email=" + Email + "\n")
                f.write("Address=" + Address + "\n")
                f.write("Education=" + Education + "\n")
                f.write("Skill=" + Skill + "\n")
                f.write("Experience=" + Experience + "\n")
                f.write("District=" + District + "\n")
                f.write("Block=" + Block + "\n")
                f.write("State=" + State + "\n")
                f.write("Profession=" + Profession + "\n")
                f.write("Cast=" + Cast + "\n")
                f.write("Gender=" + Gender + "\n")
                # f.write("Uplode_CV=" + Uplode_CV + "\n")
                f.write("values=" + values + "\n")

            # #
            # #     # with open( Uplode+ ".pdf","w") as f:
            # #     #  f.write("Uplode_CV=" + Uplode + "\n")

        def clear():
            # pass
            name_entry.delete(0, END)
            Age_entry.delete(0, END)
            Phone_entry.delete(0, END)
            Email_entry.delete(0, END)
            Address_entry.delete(0, END)
            Education_entry.delete(0, END)
            Skill_entry.delete(0, END)
            Experience_entry.delete(0, END)
            District_entry.delete(0, END)
            Block_entry.delete(0, END)
            State_entry.delete(0, END)
            Profession_entry.delete(0, END)
            Cast_entry.delete(0, END)
            Gender_entry.delete(0, END)

            # def uplode():
            #     # pass
            #     # image_names()= uplode( ".jpg ", ".pdf")
            #     file = filedialog.askopenfilename()
            #     file_name = file.name
            #     Label.config(text=file)

            # label

        Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(
            fill="both")

        Label(screen, text="Name", font="20").place(x=30, y=70)
        Label(screen, text="Age", font="20").place(x=30, y=140)
        Label(screen, text="Phone", font="20").place(x=30, y=210)
        Label(screen, text="Email", font="20").place(x=30, y=280)
        Label(screen, text="Address", font="20").place(x=30, y=350)
        Label(screen, text="Education", font="20").place(x=30, y=420)
        Label(screen, text="Skill", font="20").place(x=30, y=500)
        Label(screen, text="Experience", font="20").place(x=880, y=70)
        Label(screen, text="District", font="20").place(x=900, y=140)
        Label(screen, text="Block", font="20").place(x=900, y=210)
        Label(screen, text="State", font="20").place(x=900, y=280)
        Label(screen, text="Profession", font="20").place(x=880, y=350)
        Label(screen, text="Cast", font="20").place(x=900, y=420)
        Label(screen, text="Gender", font="20").place(x=900, y=500)
        Label(screen, text="Avaliavle Jobs", font="20").place(x=140, y=598)
        # Label(screen,text="CV/Resume",font="20").place(x=800,y=608)
        # Label(screen,text="Image",font="20").place(x=1000,y=700)

        # entry
        Name_info = StringVar()
        Age_info = StringVar()
        Phone_info = StringVar()
        Email_info = StringVar()
        Address_info = StringVar()
        Education_info = StringVar()
        Skill_info = StringVar()
        Experience_info = StringVar()
        District_info = StringVar()
        Block_info = StringVar()
        State_info = StringVar()
        Profession_info = StringVar()
        Cast_info = StringVar()
        Gender_info = StringVar()
        Uplode_info = StringVar()
        values_info = StringVar()
        name_entry = Entry(screen, font="10", textvariable=Name_info)
        name_entry.place(x=140, y=75)
        Age_entry = Entry(screen, font="10", textvariable=Age_info)
        Age_entry.place(x=140, y=140)
        Phone_entry = Entry(screen, font="10", textvariable=Phone_info)
        Phone_entry.place(x=140, y=210)
        Email_entry = Entry(screen, font="10", textvariable=Email_info)
        Email_entry.place(x=140, y=280)
        Address_entry = Entry(screen, font="10", textvariable=Address_info)
        Address_entry.place(x=140, y=350)
        Education_entry = Entry(screen, font="10", textvariable=Education_info)
        Education_entry.place(x=140, y=420)
        Skill_entry = Entry(screen, font="10", textvariable=Skill_info)
        Skill_entry.place(x=140, y=500)
        Experience_entry = Entry(screen, font="10", textvariable=Experience_info)
        Experience_entry.place(x=1000, y=75)
        District_entry = Entry(screen, font="10", textvariable=District_info)
        District_entry.place(x=1000, y=140)
        Block_entry = Entry(screen, font="10", textvariable=Block_info)
        Block_entry.place(x=1000, y=210)
        State_entry = Entry(screen, font="10", textvariable=State_info)
        State_entry.place(x=1000, y=280)
        Profession_entry = Entry(screen, font="10", textvariable=Profession_info)
        Profession_entry.place(x=1000, y=350)
        Cast_entry = Entry(screen, font="10", textvariable=Cast_info)
        Cast_entry.place(x=1000, y=420)
        Gender_entry = Entry(screen, font="10", textvariable=Gender_info)
        Gender_entry.place(x=1000, y=500)
        # Image_entry=file(screen , font="10",textvariable=Pincode_info)
        # Image_entry.place(x=900,y=700)
        # response = sms.send_number(
        #     {
        #         "from": VONAGE_BRAND_Name,
        #         "to": TO_NUMBER,
        #         "text": "Hello there from Vonage SMS API",
        #     }
        # )
        #
        # if response["messages"][0]["status"] == "0":
        #     print("Message Details: ", response)
        #     print("Message sent successfully.")
        # else:
        #     print(f"Message failed with error: {response['messages'][0]['error-text']}")

        # button
        Button(screen, text="Register", font="20", command=register).place(x=1200, y=700)
        Button(screen, text="clear", font="20", command=clear).place(x=1400, y=700)
        # Button(screen, text="Uplode", font="20", command=uplode, width=20, textvariable=Uplode_info).place(x=920, y=600)

        # combobox
        var = StringVar()
        com = ttk.Combobox(screen, width=30, font=8, textvariable=values_info)
        com['values'] = ['Data Entry operator requirement in ICIC bank', 'Accountent requirement HDFC bank',
                         'Assistance mennager requirement in ICIC bank', 'Management Requirement in IDBI bank',
                         'Ansurance staff requirement in HDFC']
        com.place(x=300, y=600)

    Button(screen, text="BANK", font="20",bg="green",command=electric).place(x=1230, y=520)
    Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(fill="both")
    Label(screen,text="I have created a website to find jobs in Motihari East Champaran Bihar.  With the help of this website, you can see which company you have lost while sitting at home.  ",font="20",fg="white",bg="blue").place(x=20, y=100)
    Label(screen,text=" For which positions are the jobs vacant in the business?  Now you can apply for this post sitting at home and if you have any work, you can find the job with the help ",font="20",fg="white",bg="blue").place(x=20, y=130)
    Label(screen,text=" of this website which earlier you used to go and give resume.  After that you would get a call saying yes now come and give me more experience.  Tell us what all you  ",font="20",fg="white",bg="blue").place(x=20, y=160)
    Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.",font="20",fg="white",bg="blue").place(x=20, y=190)


# label
Label(screen, text="JOB SEARCH EAST CHAMPARAN  MOTIHARI BIHAR", font="50", bg="yellow", fg="white").pack(fill="both")
Label(screen, text="I have created a website to find jobs in Motihari East Champaran Bihar.  With the help of this website, you can see which company you have lost while sitting at home.  ", font="20").place(x=20, y=70)
Label(screen,text=" For which positions are the jobs vacant in the business?  Now you can apply for this post sitting at home and if you have any work, you can find the job with the help " ,font="20").place(x=20, y=100)
Label(screen, text=" of this website which earlier you used to go and give resume.  After that you would get a call saying yes now come and give me more experience.  Tell us what all you  ", font="20").place(x=20, y=130)
Label(screen, text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.", font="20").place(x=20, y=160)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=500)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=520)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=540)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=560)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=580)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=600)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=620)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=640)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=660)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=680)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=700)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=720)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=740)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=200)
Label(screen,text="have, but don't have.  You will be contacted soon.  Your interview will be conducted online.  By providing you with the help of this website, you can do it.this is very nice slide" , font="20", bg="black").place(x=5,y=410)
Label(screen,text="Contect:-",font="20").place(x=200,y=600)
Label(screen,text="Name - Raushan Kumar",font="20").place(x=200,y=640)
Label(screen,text="Email - kumarraushan91628@gmail.com",font="20").place(x=200,y=680)
Label(screen,text="Join us:-",font="20").place(x=1000,y=620)
Label(screen,text="https://www.linkedin.com/in/raushan-kumar-149902227  ",font="20").place(x=900,y=660)
Label(screen,text="With the help of this website, you can know how many companies are there in which city and for which post the vacancy is available in that company.  You can easily go to  ",font="20").place(x=5,y=240)
Label(screen,text="that companyby looking at your skill and you will not have to face any problem in finding a job. So, you can easily search for a job in a city and can easily get it whenever",font="20").place(x=5,y=280)
Label(screen, text= " you want with the help of this website.",font="20").place(x=5,y=320)
#
# # button
Button(screen, text="NEXT", font="20", command=next,bg="green").place(x=700, y=450)
screen.mainloop()
