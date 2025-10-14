#NutriTeen Internal Assessment - Karthiga Raveenthiran 
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

#helps define typography across all frames
PX, PY = 32, 22
H = ("Times Roman", 14, "bold")#used for main headers
H1 = ("Arial", 14, "bold")#used for subheaders
SH = ("Time", 12)#used for smaller labels

# A dictionary linking ingredients to their respective image files
# This makes it easy to add/remove ingredients without changing core code logic
menu = {
    "lettuce": "lettuce.png",
    "tomato": "tomato.png",
    "cheese": "cheese.png",
    "cucumber": "cucumber.png",
    "chicken": "chicken.png",
    "ham": "ham.png",
    "celery": "celery.png",
    "avocado": "avocado.png",
    "egg": "egg.png",
}

#User credentials and order history stored in dictionaries
#This allows for quick data retrieval during the session
user_list = {"guest": "guest"}
order_history = {}
user_name = "guest"

#Navigation Page
#Parent class that manages page transitions between Logic, Signup, Order and History pages. 
class NavigationPage:
    def set_navigation(self, back_page, forward_page):
        self.back_page = back_page
        self.forward_page = forward_page

    def go_forward(self):
        #removes current frame and displays the next one - supports smooth transition.
        self.frame.grid_remove()
        self.forward_page.frame.grid()
        self.forward_page.showing()

    def go_back(self):
        #handles backward navigation - allows users to revisit screens.
        self.frame.grid_remove()
        self.back_page.frame.grid()
        self.back_page.showing()

    def showing(self):
        pass # overridden by child classes when page content needs to be updated.

#----LOGIN PAGE ----- #
#allows users to securely login or access as a guest.
    #Focuses on simplicity and intuitive layout for accessibility.
class LoginPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window)
        self.frame.grid(row=0, column=0)
        
        #Header section for brand name
        tk.Label(self.frame, text="Welcome to NutriTeen", font=H, bg="black", fg="white",
                 width=50, padx=PX, pady=PY).grid(columnspan=4)
        tk.Label(self.frame, text="order your NutriTeen!", bg="navy", fg="white",
                 width=50, padx=PX, pady=PY, font=H).grid(columnspan=2)

        # Tagline to improve user engagement
        tk.Label(self.frame, text="order your NutriTeen!", bg="navy", fg="white",
                 width=50, padx=PX, pady=PY, font=H).grid(columnspan=2)

        #Input fields for username and password - clear labels 
        tk.Label(self.frame, text="username:", width=10, pady=PY, padx=PX, font=SH).grid(row=2, column=0)
        self.username = ttk.Entry(self.frame, width=15)
        self.username.grid(row=2, column=1)

        tk.Label(self.frame, text="password:", width=10, pady=PY, padx=PX, font=SH).grid(row=3, column=0)
        self.password = ttk.Entry(self.frame, show="*", width=15)
        self.password.grid(row=3, column=1)

        #Buttons for clear next-step actions
        ttk.Button(self.frame, text='Login', command=self.go_forward).grid(row=4, columnspan=2)
        ttk.Button(self.frame, text='Sign up', command=self.go_back).grid(row=7, columnspan=2)

    def go_forward(self):
        global user_name
        user_name = self.username.get()
        self.username.delete(0, tk.END)
        password = self.password.get()
        self.password.delete(0, tk.END)
        
        #Validation check for user authentication
        if user_name in user_list and user_list[user_name] == password:
            super().go_forward()
        else:
            #Allows guests to continue without needing credentials (convenient for user)
            messagebox.showinfo("Info", "Logging in as guest")
            user_name = "guest"
            super().go_forward()

# ---------------- SIGNUP PAGE ---------------- #
#Allows new users to register an account with password confirmation aiding data accuracy.
class SignupPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window)
        tk.Label(self.frame, text="Create account", font=H, bg="black", fg="white",
                 width=50, padx=PX, pady=PY).grid(columnspan=4)
#Input fields for creating new account
        tk.Label(self.frame, text="username:", pady=10, padx=10).grid(row=3, column=0)
        self.username_entry = ttk.Entry(self.frame, width=20)
        self.username_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="password:", pady=10, padx=10).grid(row=4, column=0)
        self.password_entry = ttk.Entry(self.frame, show="*", width=20)
        self.password_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="confirm password:", pady=10, padx=10).grid(row=5, column=0)
        self.confirm_password_entry = ttk.Entry(self.frame, show="*", width=20)
        self.confirm_password_entry.grid(row=5, column=1)
#Clear button layout improves navigation flow
        ttk.Button(self.frame, text='Sign up', command=self.go_forward).grid(row=6, column=1)
        ttk.Button(self.frame, text='logout', command=self.go_back).grid(row=6, column=0)

    def go_forward(self):
        global user_name
        user_name = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
#Validation ensures data integrity and prevents user errors.
        if not user_name or not password:
            messagebox.showerror("Error", "Enter username and password")
            return
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return
#Saves user credentials in global dictionary
        user_list[user_name] = password
        messagebox.showinfo("Success", "Account created!")
        super().go_forward()

# ---------------- ORDER PAGE ---------------- #
#lets users create and customise sandwich orders
class OrderPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window)
        self.orders = {} #Tracks current order data
        self.images = {}
#Interface headings for clarity 
        tk.Label(self.frame, text="Create Order", font=H1, bg="black", fg="white", width=20, padx=PX, pady=PY).grid(columnspan=3, row=0)
        tk.Label(self.frame, text="Your Cart", font=H1, bg="black", fg="white", width=20, padx=PX, pady=PY).grid(column=6, row=0)
        tk.Label(self.frame, text="Select your fillings below", width=30, bg="grey", fg="white").grid(row=1, columnspan=3)
        tk.Label(self.frame, text="To remove a filling click below", width=30, bg="grey", fg="white").grid(row=1, column=5, columnspan=2)

        # Add buttons with images in the same layout - major difference compared to Iteration 1
        for i, (item, file) in enumerate(menu.items()):
            img = Image.open(file).resize((80, 80))
            self.images[item] = ImageTk.PhotoImage(img)
            btn = tk.Button(self.frame, image=self.images[item], text=item, compound="top",
                            command=lambda i=item: self.order_command(i))
            btn.grid(row=4 + i // 3, column=i % 3, padx=5, pady=5)
        #Listbox represents user's "cart" and updates
        self.lb_orders = tk.Listbox(self.frame, width=50, height=20)
        self.lb_orders.grid(column=6, columnspan=5, row=3, rowspan=5)
        self.lb_orders.bind("<<ListboxSelect>>", self.lb_click)

        ttk.Button(self.frame, text='Logout', command=self.go_back).grid(row=9, column=0)
        ttk.Button(self.frame, text='Place Order', command=self.go_forward).grid(row=9, column=6)

    def order_command(self, item):
        #Adds selected items in the user's order and serves limits for fillings (mirrors real-world ordering apps)
        if item in self.orders:
            if self.orders[item] >= 3:
                messagebox.showerror("Limit reached", f"Maximum 3 servings for {item}.")
                return
            self.orders[item] += 1
        else:
            self.orders[item] = 1
        self.showing()

    def showing(self):
    #Refreshes order list to reflect real-time updates in cart.
        self.lb_orders.delete(0, tk.END)
        for k, v in self.orders.items():
            self.lb_orders.insert(tk.END, f"{k} x{v}")

    def lb_click(self, event):
    #allows user to remove/reduce servings from their cart directly.
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            key = list(self.orders.keys())[index]
            if self.orders[key] > 1:
                self.orders[key] -= 1
            else:
                self.orders.pop(key)
            self.showing()

    def go_forward(self):
        #confirms order an stores it in user-specific history
        if not messagebox.askyesno("Confirm Order", "Are you sure?"):
            return

        users_order_history = order_history.get(user_name, [])

        if len(self.orders) == 0:
            if not messagebox.askyesno("Confirm Order", "No order selected, continue to order history?"):
                return
        else:
            # Save current order for reference in future sessions
            users_order_history.append(self.orders.copy())
            order_history[user_name] = users_order_history
            self.orders = {}

        messagebox.showinfo("Order Complete", "Your order has been placed!")
        super().go_forward()

# ---------------- ORDER HISTORY ---------------- #
#Displays a record of all previous orders, thus enhancing user satisfaction.
class OrderHistoryPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window)
        tk.Label(self.frame, text="Order History", font=H, bg="black", fg="white", width=50, padx=PX, pady=PY).grid(columnspan=2)
        tk.Label(self.frame, text="Please scroll down to see most recent order", bg="navy", fg="white", width=50, padx=PX, pady=PY).grid(columnspan=3)

        self.text_description = tk.Text(self.frame, width=80, height=20)
        self.text_description.grid(columnspan=2, row=2)

        ttk.Button(self.frame, text="Place Another Order", command=self.go_forward).grid(row=7, column=1)
        ttk.Button(self.frame, text="Logout", command=self.go_back).grid(row=7, column=0)

    def showing(self):
        #Clears text box and displays updated order history in chronological order
        self.text_description.delete(1.0, tk.END)
        if user_name in order_history:
            orders_list = order_history[user_name]
            for i, order in enumerate(orders_list, 1):
                self.text_description.insert(tk.END, f"Order {i}:\n")
                for k, v in order.items():
                    self.text_description.insert(tk.END, f"{k} x{v}\n")
                self.text_description.insert(tk.END, "\n")

# ---------------- MAIN APP ---------------- #
#Creates and connects all page objects, defining navigation flow between all connecting pages.
class NutriTeenWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NutriTeen")
        #Instantiate all pages and define navigation paths.

        login_page = LoginPage(self.window)
        signup_page = SignupPage(self.window)
        order_page = OrderPage(self.window)
        history_page = OrderHistoryPage(self.window)

        login_page.set_navigation(signup_page, order_page)
        signup_page.set_navigation(login_page, order_page)
        order_page.set_navigation(login_page, history_page)
        history_page.set_navigation(login_page, order_page)

    def mainloop(self):
        self.window.mainloop()

# ---------------- RUN APP ---------------- #
if __name__ == "__main__":
    app = NutriTeenWindow()
    app.mainloop()


