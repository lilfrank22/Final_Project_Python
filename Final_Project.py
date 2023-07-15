import tkinter

#Import widgets to use for drop down
from tkinter import ttk
from tkinter import messagebox #import message package
from PIL import ImageTk, Image #import image package

myimage= ImageTk.PhotoImage(Image.open("Special Police Badge"))

#define output 
def enter_data():
    firstname=first_name_entry.get()
    lastname=last_name_entry.get()

    if firstname and lastname:
    
        title=title_combobox.get()
        phonenumber=phone_entry.get()
        street=street_entry.get()
        city=city_entry.get()
        state=state_entry.get()
        zip=zip_entry.get()
        current_status=current_status_var.get() #get status based on current checkbox status
        yearsservice=years_service_spinbox.get()
        hourlycupay=hourly_cu_pay_combobox.get()
    
    
  
        print("Title: ", title,"  ","First Name: ","  ", firstname,"  ", "Last Name: ", lastname,"Telephone: ", phonenumber)
        print("Telephone: ", phonenumber)
        print("")
        print("Street: ",street, "City: ",city, "State: ",state, "Zip: ",zip)
        print("")
        print("Current Status: ", current_status)
        print("")
        print("Years of Service: ",yearsservice, "Hourly Pay: ",hourlycupay)
        print("*******************************")

    else:
        tkinter.messagebox.showwarning(title="Error", message="First and Last name must be entered.")

#Create window for everything to run inside
window = tkinter.Tk()

#Title for window
window.title("Officer Data Entry Form")


#Frame of window
frame = tkinter.Frame(window)
frame.pack()

#Saving user info
user_info_frame =tkinter.LabelFrame(frame, text="User Information")

user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

#list user can choose from
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Mrs","Ms","Miss", "Captain","Seargant"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

phone_label = tkinter.Label(user_info_frame, text="Phone Number")
phone_label.grid(row=0, column=3)

phone_entry = tkinter.Entry(user_info_frame)
phone_entry.grid(row=1, column=3)

street_label = tkinter.Label(user_info_frame, text="Street")
street_label.grid(row=2, column=0)
city_label = tkinter.Label(user_info_frame, text="City")
city_label.grid(row=2, column=1)


street_entry = tkinter.Entry(user_info_frame)
city_entry = tkinter.Entry(user_info_frame)
street_entry.grid(row=3, column=0)
city_entry.grid(row=3, column=1)

state_label = tkinter.Label(user_info_frame, text="State")
state_label.grid(row=2, column=2)
zip_label = tkinter.Label(user_info_frame, text="Zip")
zip_label.grid(row=2, column=3)


state_entry = tkinter.Entry(user_info_frame)
zip_entry = tkinter.Entry(user_info_frame)
state_entry.grid(row=3, column=2)
zip_entry.grid(row=3, column=3)

#Spread out fields
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Second Window Saving Officer Information
status_frame = tkinter.LabelFrame(frame, text="Additional Information")
status_frame.grid(row=1, sticky="news", padx=20, pady=20)

#Status box to show active
current_status_label = tkinter.Label(status_frame, text="Current Status")

current_status_var=tkinter.StringVar(value="Not Registered") #binding checkbox to allow entry to be saved and printed
current_status_check = tkinter.Checkbutton(status_frame, text="Active", variable=current_status_var, onvalue="Active", offvalue="Not Active") #onvalue is status of when box is checked, offvalue is value when box is not checked, stored in StringVar based on check


current_status_label.grid(row=0, column=0)
current_status_check.grid(row=1, column=0)

#Spinbox for years of service
years_service_label=tkinter.Label(status_frame, text="Years of Service")
years_service_spinbox=tkinter.Spinbox(status_frame, from_=0, to="infinity")

years_service_label.grid(row=0, column=1)
years_service_spinbox.grid(row=1, column=1)

#Spinbox for years of service
hourly_cu_pay_label=tkinter.Label(status_frame, text="Hourly Pay")
hourly_cu_pay_combobox=ttk.Combobox(status_frame, values=["","$30.00","$40.00","$50.00","$60.00"])

hourly_cu_pay_label.grid(row=0, column=2)
hourly_cu_pay_combobox.grid(row=1, column=2)

#Spread out fields
for widget in status_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button for entering data
button = tkinter.Button(frame, text="Enter Data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=10, pady=10)

#Create exit button


#create loop to run as long as application is running
window.mainloop()
