# NutriTeen - Basic Version 
# Iteration 1
#Purpose: This first iteration establishes the foundational interface and basic navigation
#between pages (Login, Signup, and Order.) The goal is to test layout structure and user flow.

from tkinter import *
from tkinter import ttk, messagebox

#----Support class for navigation----
#The NavigationPage class allows consistent navigation logic between pages.
#It produces reusable methods to move forward and backward between frames.
#Helps maintain clear, modular code for later iterations when more pages are added.

class NavigationPage:
    def set_navigation(self, back_page=None, forward_page=None):
        self.back_page = back_page
        self.forward_page = forward_page

    def go_forward(self):
        #Switches to the next frame (e.g. login -> order)
        self.frame.grid_remove()
        self.forward_page.frame.grid()

    def go_back(self):
        #Returns to the previous frame (e.g. signup -> login)
        self.frame.grid_remove()
        self.back_page.frame.grid()

# -------------------------------------------
# Login Page
# -------------------------------------------
#The LoginPage is the first screen users interact with.
#Allows navigation between login, signup, and order pages but does not yet validate credentials.
#Purpose: To test visual layout and button functionality before implementing database logic.

class LoginPage(NavigationPage):
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.grid(row=0, column=0)

        Label(self.frame, text="Welcome to NutriTeen!", font=("Arial", 16, "bold")).grid(columnspan=2, pady=20)
        Label(self.frame, text="Username:").grid(row=1, column=0, pady=5)
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Password:").grid(row=2, column=0, pady=5)
        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        ttk.Button(self.frame, text="Login", command=self.go_forward).grid(row=3, columnspan=2, pady=10)
        Label(self.frame, text="New here?").grid(row=4, columnspan=2, pady=5)
        ttk.Button(self.frame, text="Sign Up", command=self.go_back).grid(row=5, columnspan=2)


# Signup Page
#This simulates account creation.
#Currently provides a message confirmation only, no data storage.
#Purpose: To test layout, navigation, and inital user feedback using messagebox popups.

class SignupPage(NavigationPage):
    def __init__(self, window):
        self.frame = Frame(window)

        Label(self.frame, text="Create a New Account", font=("Arial", 16, "bold")).grid(columnspan=2, pady=20)
        Label(self.frame, text="Username:").grid(row=1, column=0, pady=5)
        self.username_entry = Entry(self.frame)
        self.username_entry.grid(row=1, column=1, pady=5)

        Label(self.frame, text="Password:").grid(row=2, column=0, pady=5)
        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        ttk.Button(self.frame, text="Sign Up", command=self.signup).grid(row=3, columnspan=2, pady=10)
        ttk.Button(self.frame, text="Back to Login", command=self.go_back).grid(row=4, columnspan=2, pady=5)

    def signup(self):
        #Displays a success message to simulate account creation.
        #Future improvement: Save user details for authentication.
        messagebox.showinfo("Success", "Account created successfully!")
        self.go_back()


#-----Order Page---------
#The OrderPage is an interface for placing a food order
#Introduces interactive elements (buttons, listbox) for user input.
#This demonstrates interactivity and begin shaping the app's core functionality.        
        
class OrderPage(NavigationPage):
    def __init__(self, window):
        self.frame = Frame(window)

        Label(self.frame, text="Place Your Order", font=("Arial", 16, "bold")).grid(columnspan=3, pady=10)

        #Basic menu 
        self.menu = ["Lettuce", "Tomato", "Cheese", "Ham", "Egg"]
        self.cart = []

        Label(self.frame, text="Menu Items:").grid(row=1, column=0, pady=10)
        for i, item in enumerate(self.menu):
            Button(self.frame, text=item, width=10, command=lambda i=item: self.add_to_cart(i)).grid(row=2+i, column=0, pady=3)

        Label(self.frame, text="Your Cart:").grid(row=1, column=1)
        self.cart_box = Listbox(self.frame, width=25, height=10)
        self.cart_box.grid(row=2, column=1, rowspan=5, padx=10)

        ttk.Button(self.frame, text="Place Order", command=self.place_order).grid(row=8, column=1, pady=10)
        ttk.Button(self.frame, text="Logout", command=self.go_back).grid(row=9, column=1, pady=5)

    def add_to_cart(self, item):
        #Adds a selected item to the cart and updates the listbox display.
        self.cart.append(item)
        self.cart_box.insert(END, item)

    def place_order(self):
        #Displays order confirmation and resets the cart.
        messagebox.showinfo("Order Placed", f"Order placed: {', '.join(self.cart)}")
        self.cart.clear()
        self.cart_box.delete(0, END)


#-----Main Window Controller----
#The NutriTeenWindow class manages all pages and initialises navigation links.
#Ensures a smooth user flow between logic, signup, and order interfaces.
        

class NutriTeenWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("NutriTeen Basic Prototype")
        #initialises pages
        login_page = LoginPage(self.window)
        signup_page = SignupPage(self.window)
        order_page = OrderPage(self.window)

        #establishes navigation paths between pages
        login_page.set_navigation(signup_page, order_page)
        signup_page.set_navigation(login_page)
        order_page.set_navigation(login_page)

    def mainloop(self):
        self.window.mainloop()

#----Run the App----
#This lauches the basic NutriTeen prototype.

if __name__ == "__main__":
    app = NutriTeenWindow()
    app.mainloop()
