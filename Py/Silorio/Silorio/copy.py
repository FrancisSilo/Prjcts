import tkinter as tk
from tkinter import *
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = False

        # Define light and dark mode themes
        self.light_mode = {
            'bg': 'white',
            'fg': 'black',
            'entry_bg': '#eee',
            'entry_fg': 'black',
            'btn_bg': '#ddd',
            'btn_fg': 'black'
        }

        self.dark_mode = {
            'bg': '#333',
            'fg': 'white',
            'entry_bg': '#555',
            'entry_fg': 'white',
            'btn_bg': '#444',
            'btn_fg': 'white'
        }

        # Call the create_widgets method to build the UI
        self.create_widgets()

        # Apply light mode by default
        self.apply_theme(self.light_mode)

    def create_widgets(self):
        # Create UI elements
        self.label_username = tk.Label(self.root, text='Username')
        self.label_username.pack()

        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack()

        self.label_password = tk.Label(self.root, text='Password')
        self.label_password.pack()

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(self.root, text='Login', command=self.login)
        self.login_button.pack()

        self.sign_up_label = tk.Label(self.root, text="Don't have an account? Sign up", fg='#57a1f8', cursor="hand2")
        self.sign_up_label.pack()
        self.sign_up_label.bind("<Button-1>", lambda event: self.signup())

    def apply_theme(self, theme):
        # Apply theme to UI elements
        self.root.config(bg=theme['bg'])

        widgets = [self.label_username, self.entry_username, self.label_password, self.entry_password, self.login_button, self.sign_up_label]

        for widget in widgets:
            widget.config(bg=theme['bg'], fg=theme['fg'])

    def toggle_theme(self):
        # Toggle between light and dark mode
        if self.is_dark_mode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)

        self.is_dark_mode = not self.is_dark_mode

    def login(self):
        # Perform login authentication
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == 'admin' and password == '123':
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def signup(self):
        # Handle user signup
        signup_form = SignupForm(self.root)

    def show_dashboard(self):
        # Show the dashboard window
        dashboard_window = tk.Toplevel(self.root)
        dashboard_window.title("Dashboard")
        dashboard_window.geometry("400x300")

        dashboard_label = tk.Label(dashboard_window, text="Welcome to the Dashboard!")
        dashboard_label.pack()

        logout_button = tk.Button(dashboard_window, text="Logout", command=dashboard_window.destroy)
        logout_button.pack()

class SignupForm:
    def __init__(self, root):
        self.root = root
        self.signup_window = tk.Toplevel(self.root)
        self.signup_window.title('Sign Up')
        self.signup_window.geometry('300x200')

        self.label_username = tk.Label(self.signup_window, text='Username')
        self.label_username.pack()

        self.entry_username = tk.Entry(self.signup_window)
        self.entry_username.pack()

        self.label_password = tk.Label(self.signup_window, text='Password')
        self.label_password.pack()

        self.entry_password = tk.Entry(self.signup_window, show="*")
        self.entry_password.pack()

        self.sign_up_button = tk.Button(self.signup_window, text='Sign Up', command=self.register_user)
        self.sign_up_button.pack()

    def register_user(self):
        # Perform user registration
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Add your user registration logic here
        # For example, you can store the new user in a database or file

        messagebox.showinfo('Success', 'User registered successfully!')
        self.signup_window.destroy()

def main():
    root = Tk()
    root.title('Login')
    root.geometry('300x250')

    global app
    app = LoginApp(root)

    dark_mode_button = Button(root, text='Light/Dark Mode', command=app.toggle_theme)
    dark_mode_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
