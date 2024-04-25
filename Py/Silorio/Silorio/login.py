import tkinter as tk
from tkinter import *
from tkinter import messagebox

def light_dark_mode():
    current_bg = frame.cget('bg')

    if current_bg == '#fff':  # Switch to dark mode
        root.configure(bg='#444')  # Update background color
        frame.configure(bg='#444')  # Update frame background color
        Can2.configure(bg='#444')  # Update the canvas background color
        Can.configure(bg='#444')  # Update the canvas background color

        # Update the header and labels to white
        heading.config(fg='white')
        user.config(fg='white')
        code.config(fg='white')
        no_account_label.config(fg='white')
        sign_up_label.config(fg='white')

        # Update the login image with a dark background
        login_img = tk.PhotoImage(file='login-img-dark.png')
        Label(root, image=login_img).place(x=50, y=50)

        # Apply dark mode to the signup window
        dark_mode_signup()

    else:  # Switch to light mode
        root.configure(bg='#fff')  # Update background color
        frame.configure(bg='#fff')  # Update frame background color
        Can2.configure(bg='#fff')  # Update the canvas background color
        Can.configure(bg='#fff')  # Update the canvas background color

        # Update the header and labels to black
        heading.config(fg='#57a1f8')
        user.config(fg='black')
        code.config(fg='black')
        no_account_label.config(fg='black')
        sign_up_label.config(fg='#57a1f8')

        # Update the login image with a light background
        login_img = tk.PhotoImage(file='login-img-light.png')
        Label(root, image=login_img).place(x=50, y=50)

        # Apply light mode to the signup window
        light_mode_signup()

    # Update the button appearance based on the current mode
    if frame.cget('bg') == '#fff':
        dark_mode_button.config(text='Dark Mode')
    else:
        dark_mode_button.config(text='Light Mode')

    # Update the background color of the window, frame, and canvas
    root.config(bg=root.cget('bg'))
    frame.config(bg=frame.cget('bg'))
    Can.config(bg=Can.cget('bg'))
    Can2.config(bg=Can2.cget('bg'))

    # Update the text color of the username, password, and labels
    user.config(fg=root.cget('bg'))
    code.config(fg=root.cget('bg'))
    no_account_label.config(fg=root.cget('bg'))
    sign_up_label.config(fg=root.cget('bg'))

def light_mode_signup():
    signup_window.configure(bg='#f0f0f0')  # Update signup window background color
    username_label.config(bg='#f0f0f0', fg='black')  # Update username label color
    password_label.config(bg='#f0f0f0', fg='black')  # Update password label color
    username_entry.config(bg='#e0e0e0', fg='black')  # Update username entry color
    password_entry.config(bg='#e0e0e0', fg='black')  # Update password entry color
    signup_button.config(bg='#57a1f8', fg='white')  # Update signup button color

def dark_mode_signup():
    signup_window.configure(bg='#444')  # Update signup window background color
    username_label.config(bg='#444', fg='white')  # Update username label color
    password_label.config(bg='#444', fg='white')  # Update password label color
    username_entry.config(bg='#333', fg='white')  # Update username entry color
    password_entry.config(bg='#333', fg='white')  # Update password entry color
    signup_button.config(bg='#57a1f8', fg='white')  # Update signup button color

def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '123':
        screen = Toplevel(root)
        screen.title('Dashboard')
        screen.geometry('1400x850')

        menubar = tk.Menu(screen)
        screen.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')
        file_menu.add_command(label='Close')
        file_menu.add_separator()
        sub_menu = tk.Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Keyboard Shortcuts')
        sub_menu.add_command(label='Color Themes')
        file_menu.add_cascade(label="Preferences", menu=sub_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=root.destroy)

        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label='About')
        help_menu.add_command(label='User Guides...')

        menubar.add_cascade(label="Help", menu=help_menu)

        Can = tk.Canvas(screen, width=300, height=500)
        Can.pack(fill=tk.Y, side=tk.LEFT)

        # Resize the blue.png image
        blue_img = tk.PhotoImage(file="blue.png")
        blue_img = blue_img.zoom(3, 3)
        Can.create_image(140, 250, image=blue_img)

        profile_img = tk.PhotoImage(file="dog-profile.png")
        profile_img = profile_img.subsample(3, 3)
        Can.create_image(150, 140, image=profile_img)

        Can.create_text(150, 280, text="DASHBOARD", font=("Arial", 25), fill="white")

        Can2 = tk.Canvas(screen, width=1100, height=500)
        Can2.pack(fill=tk.Y, side=tk.RIGHT)

        Can2.create_rectangle(0, 0, 1100, 72, fill="blue")

        Can2.create_text(1000, 40, text="LOGOUT ", font=("Arial", 20), fill="white")

        sales_growth_img = PhotoImage(file="sales-growth.png")
        sales_growth_resized = sales_growth_img.subsample(3, 3)
        image21 = Can2.create_image(290, 250, image=sales_growth_resized)

        pie_graph2_img = PhotoImage(file="pie-graph.png")
        pie_graph2_resized = pie_graph2_img.subsample(2, 2)
        image22 = Can2.create_image(750, 270, image=pie_graph2_resized)

        Can2.create_rectangle(50, 470, 300, 750, fill="green", outline="")
        Can2.create_rectangle(350, 470, 600, 750, fill="yellow", outline="")
        Can2.create_rectangle(650, 470, 950, 750, fill="red", outline="blue")

        screen.mainloop()

    elif username != 'admin' and password == '123':
        messagebox.showerror("Invalid", "Username and password")

    elif password != '123':
        messagebox.showerror("Invalid", "Password")

def signup():
    global signup_window, username_label, password_label, username_entry, password_entry, signup_button

    signup_window = Toplevel(root)
    signup_window.title('Sign Up')
    signup_window.geometry('400x300')

    label_font = ('Arial', 12)
    entry_font = ('Arial', 10)

    username_label = Label(signup_window, text='Username:', font=label_font)
    username_label.pack(pady=10)

    username_entry = Entry(signup_window, font=entry_font, bd=1)
    username_entry.pack(pady=5)

    password_label = Label(signup_window, text='Password:', font=label_font)
    password_label.pack(pady=10)

    password_entry = Entry(signup_window, show='*', font=entry_font, bd=1)
    password_entry.pack(pady=5)

    signup_button = Button(signup_window, text='Sign Up', font=label_font, bg='#57a1f8', fg='white', bd=0, command=register_user)
    signup_button.pack(pady=20, padx=10, ipadx=10)

    light_dark_mode()  # Apply current mode to signup window

    signup_window.mainloop()

def register_user():
    new_username = username_entry.get()
    new_password = password_entry.get()

    # Add your user registration logic here
    # For example, you can store the new user in a database or file

    messagebox.showinfo('Success', 'User registered successfully!')

root = Tk()
root.title('Login')
root.geometry('925x500')

dark_mode_button = Button(root, text='Light/Dark Mode', command=light_dark_mode)
dark_mode_button.pack()

login_img = tk.PhotoImage(file='login-img-light.png')
Label(root, image=login_img).place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

user = Entry(frame, width=25, border=0, fg='black')
user.place(x=30, y=80)
user.insert(0, 'Username')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(frame, width=25, border=0, fg='black')
code.place(x=30, y=150)
code.insert(0, 'Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

no_account_label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
no_account_label.place(x=75, y=270)

sign_up_label = Label(frame, text="Sign up", fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 9))
sign_up_label.place(x=215, y=270)
sign_up_label.bind("<Button-1>", lambda event: signup())

root.mainloop()
