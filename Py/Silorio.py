import tkinter
from tkinter import messagebox

top = tkinter.Tk()

window = tkinter.Tk()

window.title("Login Form")
window.geometry("1000x500")

first_name = tkinter.Label(window, text="First Name: ")
first_name.grid(row=0, column=0)
first_nameEntry = tkinter.Entry(window)
first_nameEntry.grid(row=0, column=1)

middle_name = tkinter.Label(window, text="Middle Name: ")
middle_name.grid(row=1, column=0)
middle_nameEntry = tkinter.Entry(window)
middle_nameEntry.grid(row=1, column=1)

last_name = tkinter.Label(window, text="Last Name: ")
last_name.grid(row=2, column=0)
last_nameEntry = tkinter.Entry(window)
last_nameEntry.grid(row=2, column=1)

country = tkinter.Label(window, text="Country: ")
country.grid(row=3, column=0)
country_var = tkinter.StringVar(window)
country_var.set("Select Country")
country_combobox = tkinter.OptionMenu(window, country_var, "India", "USA", "UK", "Canada", "Philippines")
country_combobox.grid(row=3, column=1)

gender = tkinter.Label(window, text="Gender: ")
gender.grid(row=4, column=0)
gender_var = tkinter.StringVar(window)
gender_var.set("Male")
male = tkinter.Radiobutton(window, text="Male", variable=gender_var, value="Male")
male.grid(row=4, column=1)
female = tkinter.Radiobutton(window, text="Female", variable=gender_var, value="Female")
female.grid(row=4, column=2)

hobbies = tkinter.Label(window, text="Hobbies: ")
hobbies.grid(row=5, column=0)
hobbies_var = tkinter.StringVar(window)
hobbiesList = ["Reading", "Writing", "Sports", "Drawing", "Coding"]
hobbies_checkList = tkinter.Checkbutton(window, text=hobbiesList[0], variable=hobbies_var, onvalue=hobbiesList[0],)
hobbies_checkList.grid(row=5, column=1)

for i in range(1, len(hobbiesList)):
  hobbies_checkList = tkinter.Checkbutton(window, text=hobbiesList[i], variable=hobbies_var, onvalue=hobbiesList[i],)
  hobbies_checkList.grid(row=5, column=i+1)

submit = tkinter.Button(window, text="Submit")
submit.grid(row=10, column=1)

def submit_data():
  first_name = first_nameEntry.get()
  middle_name = middle_nameEntry.get()
  last_name = last_nameEntry.get()
  country = country_var.get()
  gender = gender_var.get()
  hobbies = hobbies_var.get()

  message = f"First Name: {first_name}\n"
  message += f"Middle Name: {middle_name}\n"
  message += f"Last Name: {last_name}\n"
  message += f"Country: {country}\n"
  message += f"Gender: {gender}\n"
  message += f"Hobbies: {hobbies}"

  messagebox.showinfo("Submitted Data", message)
  submit.config(command=submit_data)


window.mainloop()