import tkinter


#Import tkinter library/modules
from tkinter import * #Input all from tkinter
from tkinter import ttk
from tkinter import messagebox #Message Box Module
from tkinter import colorchooser #Choose colors
from tkinter import PhotoImage #PhotoImage Module
from tkinter.font import Font #Font Module

#Define the iconphoto for use in the title bar frame to show Police Badge icon
def iconphoto():
    iconphoto(self, default = False, *args)

def endProgam():
    window.destroy()

#define user input information to get from fields data is input into
def enter_data():
    title=title_combobox.get() #get information from user input
    firstname=first_name_entry.get()#get information from user input
    lastname=last_name_entry.get()#get information from user input
    phonenumber=phone_entry.get()#get information from user input
    street=street_entry.get() #get information from user input
    city=city_entry.get()#get information from user input
    state=state_entry.get()#get information from user input
    zip=zip_entry.get()#get information from user input
    current_status=current_status_var.get() #get information from user input
    yearsservice=years_service_spinbox.get()#get information from user input
    hourlycupay=hourly_cu_pay_combobox.get()#get information from user input

   
#Loop confirms the user has input information in the fields or error is returned and information can't be entered
    if firstname and lastname and street and city and state and zip:
    
#Getting information that user has put into the system
        title=title_combobox.get() #get information from user input
        firstname=first_name_entry.get()#get information from user input
        lastname=last_name_entry.get()#get information from user input
        phonenumber=phone_entry.get()#get information from user input
        street=street_entry.get() #get information from user input
        city=city_entry.get()#get information from user input
        state=state_entry.get()#get information from user input
        zip=zip_entry.get()#get information from user input
        current_status=current_status_var.get() #get information from user input
        yearsservice=years_service_spinbox.get()#get information from user input
        hourlycupay=hourly_cu_pay_combobox.get()#get information from user input
    
    
  #Print out information on screen from user input
        print("Title: ", title) #Prints output to screen title description and actual data input by user
        print("First Name: ", firstname)#Prints output to screen title description and actual data input by user
        print("Last Name: ", lastname)#Prints output to screen title description and actual data input by user
        print("Telephone: ", phonenumber)#Prints output to screen title description and actual data input by user
        print("Street: ",street,)#Prints output to screen title description and actual data input by user
        print("City: ",city)#Prints output to screen title description and actual data input by user
        print("State: ",state)#Prints output to screen title description and actual data input by user
        print("Zip: ",zip)#Prints output to screen title description and actual data input by user
        print(" ")# space entered between rows printing
        print("Current Status: ", current_status)#Prints output to screen title description and actual data input by user
        print("Years of Service: ",yearsservice)#Prints output to screen title description and actual data input by user
        print("Hourly Pay: ",hourlycupay)#Prints output to screen title description and actual data input by user
        print("******************************************")#Outputs to screen a separation line between output of user input data

        
    else:
        tkinter.messagebox.showwarning(title="Error", message="All fields must be completed.  If not active do not check the active box.")#Create error box to appear if fname and/or lname are blank
     
   
#Create primary window frame for everything to run inside
window = tkinter.Tk()

#Change/Set Title Bar ICON on primary frame to show a POLICE BADGE instead of the standard feather
photo = PhotoImage(file = "C:\PYTHON_FINAL_PROJECT\\PoliceBadge.png")#Photo image to appear in icon
window.iconphoto(False, photo)

#Title for window frame
window.title("Officer Import Form")

#Create frame of window
frame = tkinter.Frame(window)
frame.pack()#pack place for grid

#Create label frame and label it User Information
user_info_frame =tkinter.LabelFrame(frame, text="User Information")#Create label frame name: User Information
user_info_frame.grid(row=0, column=0, padx=20, pady=20)#Pack place for grid and align (news = north,east,west,south): User Information

#Title: Combobox list user can choose from
title_label = tkinter.Label(user_info_frame, text="Title")#Set frame label placement to appear
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Mrs","Ms","Miss", "Captain","Seargant"]) #Set Combobox information
title_label.grid(row=0, column=0)#Set label placement to appear
title_combobox.grid(row=1, column=0)#Set user combobox placement to appear

#First and last name labels
first_name_label = tkinter.Label(user_info_frame, text="First Name")#Create label name: First Name
first_name_label.grid(row=0, column=1)#Set label placement to appear: first name
last_name_label = tkinter.Label(user_info_frame, text="Last Name")#Create label name: Last Name
last_name_label.grid(row=0, column=2)#Set label placement to appear: last name

#First and last name entry
first_name_entry = tkinter.Entry(user_info_frame)#Set frame first name appears in: first name
last_name_entry = tkinter.Entry(user_info_frame)#Set frame last name appears in: last name
first_name_entry.grid(row=1, column=1)#set user entry placement to appear: first name
last_name_entry.grid(row=1, column=2)#set user entry placement to appear: last name


#Telephone number label
phone_label = tkinter.Label(user_info_frame, text="Phone Number")#Set frame label placement to appear
phone_label.grid(row=0, column=3)#Set placement of label to appear in frame

#Telephone number entry
phone_entry = tkinter.Entry(user_info_frame)#Set frame user entry will appear in
phone_entry.grid(row=1, column=3)#Set placement of user entry box to appear in frame

#Street, City, State, Zip Code label creation
street_label = tkinter.Label(user_info_frame, text="Street")#Set frame label placement to appear
street_label.grid(row=2, column=0)#Set placement of label to appear in frame
city_label = tkinter.Label(user_info_frame, text="City")#Set frame label placement to appear
city_label.grid(row=2, column=1)#Set placement of label to appear in frame

#Street, City, State, Zip Code user box creation
street_entry = tkinter.Entry(user_info_frame)#set frame user entry placement to appear: street
city_entry = tkinter.Entry(user_info_frame)#set frame user entry placement to appear: city
street_entry.grid(row=3, column=0)#Set placement of user entry to appear in frame: street
city_entry.grid(row=3, column=1)#Set placement of user entry box to appear in frame: city

#State and Zip Code label creation
state_label = tkinter.Label(user_info_frame, text="State")#Set frame label placement to appear: state
state_label.grid(row=2, column=2)#Set placement of label to appear in frame: state
zip_label = tkinter.Label(user_info_frame, text="Zip")#Set frame label placement to appear: zip code
zip_label.grid(row=2, column=3)#Set placement of label to appear in frame: zip code

#State and Zip Code user box creation
state_entry = tkinter.Entry(user_info_frame)#set frame user entry placement to appear: state
state_entry.grid(row=3, column=2)#set user entry placement within frame to appear: state
zip_entry = tkinter.Entry(user_info_frame)#set frame user entry placement to appear: zip code                   
zip_entry.grid(row=3, column=3)#set user entry placement within frame to appear: zip code

#Spread out frame info for spacing
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Second Window Saving Officer Information
status_frame = tkinter.LabelFrame(frame, text="Additional Information")#Create label frame name: Additional Information
status_frame.grid(row=1, sticky="news", padx=20, pady=20)#pack place for grid and align (news = north,east,west,south): Additional Information

#Status box to show active
current_status_label = tkinter.Label(status_frame, text="Current Status")#Set frame label placement to appear: Current Status

current_status_var=tkinter.StringVar(value="Not Registered") #binding checkbox to allow entry to be saved and printed
current_status_check = tkinter.Checkbutton(status_frame, text="Active", variable=current_status_var, onvalue="Active", offvalue="Not Active") #Create button that allows you to use check box and sotre value: onvalue is status of when box is checked, offvalue is value when box is not checked, stored in StringVar based on check

current_status_label.grid(row=0, column=0)#set placement of label to appear in frame
current_status_check.grid(row=1, column=0)#set placement of label to appear in frame: check box

#Spinbox for years of service
years_service_label=tkinter.Label(status_frame, text="Years of Service")#Set frame label to appear: Years of Service
years_service_spinbox=tkinter.Spinbox(status_frame, from_=0, to="infinity")#Set spinbox values to choose from

years_service_label.grid(row=0, column=1)#Set frame for label placement to appear
years_service_spinbox.grid(row=1, column=1)#Set spinbox placement to appear

#Combobox for years of service
hourly_cu_pay_label=tkinter.Label(status_frame, text="Hourly Pay")#Set frame label to appear: Hourly Pay
hourly_cu_pay_combobox=ttk.Combobox(status_frame, values=["","$30.00","$40.00","$50.00","$60.00"])#Set spinbox values to choose from

hourly_cu_pay_label.grid(row=0, column=2)#Set frame for label placement to appear
hourly_cu_pay_combobox.grid(row=1, column=2)#Set spinbox placement to appear


#Spread out frame info for spacing
for widget in status_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Button to press to have data accepted once user is finished entering data
button = tkinter.Button(frame, text="Press Button to Enter Data", command=enter_data)#Created button within a frame with command to enter the data
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)  #Set the placement of the button


#Create frame of window
frame = tkinter.Frame(window)
frame.pack()#pack place for grid


#Create Exit Button to end program input
img=PhotoImage(file=("C:\PYTHON_FINAL_PROJECT\\PoliceBadge.png"))#Define image to be on the Exit button
sizedimage=img.subsample(1, 6)#Size the image to be on the Exit button

#Created button for exiting program; "compound" manages where image is located on button, ".pack(side=TOP)" manages where the text is placed on the button
exit_button = tkinter.Button(window, text = "Press the Shield Button to End Program", command = endProgam, image=sizedimage, compound=BOTTOM).pack(side=TOP)#Created exit button with command to end the program
#exit_button.pack()#Set placement of the button

#Create loop to run as long as application is running
window.mainloop()
