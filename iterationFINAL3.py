#NutriTeen - Iteration 3(Final version) - Karthiga Raveenthiran
#Purpose: A sandwich ordering app allowing users to login, create accounts, select ingredients with prices
#calculates total cost, and view order history
#------------------------------------------------
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ---------- Font & layout constants ----------
#Fonts chosen for professional readability and consistency across all pages.
PX, PY = 32, 22
H = ("Segoe UI Semibold", 20)   # main title font for clarity and emphasis
H1 = ("Segoe UI Semibold", 16)  # subheader font for page section titles
SH = ("Segoe UI", 11)           # small text font for readability
BG_MAIN = "#f8f9fa" #light neutral background for user comfort
BG_HEADER = "#000000" #main header background for contrast
BG_SUB = "#1e3a8a" #accent blue header bar
FG_WHITE = "white"

# ---------- Menu items and prices ----------
#Ingredient images and prices stored in dictionaries for maintainability.
menu = {
    "Lettuce": "lettuce.png",
    "Tomato": "tomato.png",
    "Cheese": "cheese.png",
    "Cucumber": "cucumber.png",
    "Chicken": "chicken.png",
    "Ham": "ham.png",
    "Celery": "celery.png",
    "Avocado": "avocado.png",
    "Egg": "egg.png",
}

prices = {
    "Lettuce": 1.00,
    "Tomato": 1.50,
    "Cheese": 2.00,
    "Cucumber": 1.20,
    "Chicken": 3.00,
    "Ham": 2.80,
    "Celery": 1.00,
    "Avocado": 2.50,
    "Egg": 1.80,
}
#Defaul user data and order storage
user_list = {"guest": "guest"}
order_history = {}
user_name = "guest"

# ---------- Reusable rounded blue button----------
#Function returns a consistent-looking button for all pages
#Supports consistency and reduced repetition of code.
def rounded_button(frame, text, command):
    return tk.Button(
        frame,
        text=text,
        font=("Segoe UI Semibold", 10),
        bg="#1e3a8a",
        fg="white",
        activebackground="#365fdc",
        activeforeground="white",
        relief="flat", #creates clean, modern flat style
        bd=0, #no border for smooth feel
        padx=12,
        pady=6,
        highlightthickness=0,
        borderwidth=0,
        command=command,
    )

# ---------- Navigation base ----------
#Handles transitions between pages to ensure reusability
#Inheritance is used so each page class has consistent navigation methods.
class NavigationPage:
    def set_navigation(self, back_page, forward_page):
        self.back_page = back_page
        self.forward_page = forward_page

    def go_forward(self):
        #Switches to next page
        self.frame.grid_remove()
        self.forward_page.frame.grid()
        self.forward_page.showing()

    def go_back(self):
        #Returns to previous page
        self.frame.grid_remove()
        self.back_page.frame.grid()
        self.back_page.showing()

    def showing(self):
        pass


# ---------- LOGIN PAGE ----------
#Allows existing users or guests to access the app
class LoginPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window, bg=BG_MAIN)
        self.frame.grid(row=0, column=0)

        #Headers - consistent width for balanced design
        tk.Label(self.frame, text="Welcome to NutriTeen", font=H, bg=BG_HEADER, fg=FG_WHITE,
                 width=50, padx=PX, pady=PY).grid(columnspan=2)
        tk.Label(self.frame, text="Order your NutriTeen!", bg=BG_SUB, fg=FG_WHITE,
                 width=50, padx=PX, pady=PY, font=H1).grid(columnspan=2)
        #Headers
        tk.Label(self.frame, text="Username:", width=10, pady=10, font=SH, bg=BG_MAIN).grid(row=2, column=0)
        self.username = ttk.Entry(self.frame, width=20)
        self.username.grid(row=2, column=1)
        #Username/password input fields
        tk.Label(self.frame, text="Password:", width=10, pady=10, font=SH, bg=BG_MAIN).grid(row=3, column=0)
        self.password = ttk.Entry(self.frame, show="*", width=20)
        self.password.grid(row=3, column=1)
        #Buttons with consistent rounded styling
        rounded_button(self.frame, "Login", self.go_forward).grid(row=4, columnspan=2, pady=10)
        rounded_button(self.frame, "Sign up", self.go_back).grid(row=5, columnspan=2, pady=5)

    def go_forward(self):
        #Validates login and navigates to order page
        global user_name
        user_name = self.username.get().strip()
        password = self.password.get().strip()
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

        if user_name in user_list and user_list[user_name] == password:
            super().go_forward()
        else:
            #Guest access provided for convenience
            messagebox.showinfo("Info", "Logging in as guest.")
            user_name = "guest"
            super().go_forward()


# ---------- SIGNUP PAGE ----------
#Creates new user accounts with validation checks for password strength.
class SignupPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window, bg=BG_MAIN)
        tk.Label(self.frame, text="Create Account", font=H, bg=BG_HEADER, fg=FG_WHITE,
                 width=50, padx=PX, pady=PY).grid(columnspan=2)
#       #Input fields for account creation
        tk.Label(self.frame, text="Username:", pady=10, padx=10, bg=BG_MAIN, font=SH).grid(row=1, column=0)
        self.username_entry = ttk.Entry(self.frame, width=20)
        self.username_entry.grid(row=1, column=1)
        
        tk.Label(self.frame, text="Password:", pady=10, padx=10, bg=BG_MAIN, font=SH).grid(row=2, column=0)
        self.password_entry = ttk.Entry(self.frame, show="*", width=20)
        self.password_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Confirm Password:", pady=10, padx=10, bg=BG_MAIN, font=SH).grid(row=3, column=0)
        self.confirm_entry = ttk.Entry(self.frame, show="*", width=20)
        self.confirm_entry.grid(row=3, column=1)

        rounded_button(self.frame, "Sign up", self.create_account).grid(row=4, column=1, pady=10)
        rounded_button(self.frame, "Back", self.go_back).grid(row=4, column=0, pady=10)

    def create_account(self):
        #Validation for new accounts 
        global user_name
        user_name = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()

        if not user_name or not password:
            messagebox.showerror("Error", "Enter username and password.")
            return
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long.")
            return
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        user_list[user_name] = password
        messagebox.showinfo("Success", "Account created!")
        super().go_forward()


# ---------- ORDER PAGE ----------
#Core functionality where users choose fillings and view running totals.
class OrderPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window, bg=BG_MAIN)
        self.orders = {} #Dictionary storing items and quantities
        self.images = {} #Stores image objects
        #Headers for both menu and cart sections
        tk.Label(self.frame, text="Create Order", font=H1, bg=BG_HEADER, fg=FG_WHITE,
                 width=25, padx=PX, pady=PY).grid(columnspan=3, row=0)
        tk.Label(self.frame, text="Your Cart", font=H1, bg=BG_HEADER, fg=FG_WHITE,
                 width=25, padx=PX, pady=PY).grid(column=5, row=0)
        #Subtext instructions
        tk.Label(self.frame, text="Select your fillings below", bg="#555", fg="white",
                 width=30, font=SH).grid(row=1, columnspan=3)
        tk.Label(self.frame, text="Click an item in the cart to remove it", bg="#555",
                 fg="white", width=35, font=SH).grid(row=1, column=5, columnspan=2)
        #Creates buttons for each ingredient with its image and price.
        for i, (item, file) in enumerate(menu.items()):
            try:
                img = Image.open(file).resize((80, 80))
                self.images[item] = ImageTk.PhotoImage(img)
                btn_text = f"{item}\n${prices[item]:.2f}"
                btn = tk.Button(self.frame, image=self.images[item], text=btn_text,
                                font=("Segoe UI", 10),
                                compound="top", relief="flat", bg="white",
                                activebackground="#e0f2fe",
                                command=lambda i=item: self.add_to_order(i))
                btn.grid(row=3 + i // 3, column=i % 3, padx=5, pady=5)
            except Exception:
                #If image file missing, text button still created.    
                tk.Button(self.frame, text=f"{item}\n${prices[item]:.2f}",
                          font=("Segoe UI", 10),
                          command=lambda i=item: self.add_to_order(i)).grid(row=3 + i // 3, column=i % 3)
        #Cart display box
        self.lb_orders = tk.Listbox(self.frame, width=45, height=14, font=("Segoe UI", 10))
        self.lb_orders.grid(column=5, columnspan=2, row=3, rowspan=5, padx=10)
        self.lb_orders.bind("<<ListboxSelect>>", self.remove_item)
        #Running total lable updates
        self.total_label = tk.Label(self.frame, text="Total: $0.00",
                                    font=("Segoe UI Semibold", 12), fg="green", bg=BG_MAIN)
        self.total_label.grid(row=8, column=5, sticky="w", pady=5)
        #Action buttons
        rounded_button(self.frame, "Place Order", self.place_order).grid(row=9, column=5, pady=5)
        rounded_button(self.frame, "Logout", self.go_back).grid(row=9, column=0, pady=5)
        #--Core functions controlling cart logic---
    def add_to_order(self, item):
        self.orders[item] = self.orders.get(item, 0) + 1
        if self.orders[item] > 3:
            messagebox.showerror("Limit reached", f"Maximum 3 servings for {item}.")
            self.orders[item] = 3
        self.showing()

    def calculate_total(self):
        #Calculates total price based on quantities
        return sum(prices[i] * q for i, q in self.orders.items())

    def showing(self):
        #Refreshes cart display and total cost label
        self.lb_orders.delete(0, tk.END)
        for k, v in self.orders.items():
            subtotal = prices[k] * v
            self.lb_orders.insert(tk.END, f"{k} x{v} - ${subtotal:.2f}")
        self.total_label.config(text=f"Total: ${self.calculate_total():.2f}")

    def remove_item(self, event):
        #Allows removing one quanitiy of an item on selection
        selection = event.widget.curselection()
        if selection:
            key = list(self.orders.keys())[selection[0]]
            self.orders[key] -= 1
            if self.orders[key] <= 0:
                self.orders.pop(key)
            self.showing()

    def place_order(self):
        #confirms order, stores it, and resets cart
        if not self.orders:
            messagebox.showerror("Empty Cart", "Please add items before ordering.")
            return
        total_cost = self.calculate_total()
        user_orders = order_history.get(user_name, [])
        order_copy = self.orders.copy()
        order_copy["Total"] = f"${total_cost:.2f}"
        user_orders.append(order_copy)
        order_history[user_name] = user_orders
        self.orders = {}
        self.showing()
        messagebox.showinfo("Order Placed", f"Your total is ${total_cost:.2f}.")
        super().go_forward()


# ---------- ORDER HISTORY PAGE ----------
#Displays all past orders for the current user.
class OrderHistoryPage(NavigationPage):
    def __init__(self, window):
        self.frame = tk.Frame(window, bg=BG_MAIN)
        tk.Label(self.frame, text="Order History", font=H, bg=BG_HEADER, fg=FG_WHITE,
                 width=50, padx=PX, pady=PY).grid(columnspan=2)
        tk.Label(self.frame, text="Most Recent Orders Appear Last", bg=BG_SUB, fg=FG_WHITE,
                 width=50, padx=PX, pady=PY, font=("Segoe UI Bold", 15)).grid(columnspan=2)
        #Text box to display history data
        self.text_description = tk.Text(self.frame, width=80, height=20,
                                        relief="flat", bd=2, font=("Segoe UI", 10))
        self.text_description.grid(columnspan=2, row=2, pady=10)
        #Buttons for navigation
        rounded_button(self.frame, "Place Another Order", self.go_forward).grid(row=3, column=1, pady=5)
        rounded_button(self.frame, "Logout", self.go_back).grid(row=3, column=0, pady=5)

    def showing(self):
        #Loads and formats previous orders for the logged-in user
        self.text_description.delete(1.0, tk.END)
        if user_name in order_history and order_history[user_name]:
            for i, order in enumerate(order_history[user_name], 1):
                self.text_description.insert(tk.END, f"Order {i}:\n")
                for k, v in order.items():
                    if k == "Total":
                        self.text_description.insert(tk.END, f"--- {v}\n\n")
                    else:
                        self.text_description.insert(tk.END, f"{k} x{v}\n")
        else:
            self.text_description.insert(tk.END, "No previous orders found.\n")


# ---------- MAIN APP ----------
#Creates main window, links all pages, and initiates event loop.
class NutriTeenWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("NutriTeen Sandwich Ordering App")
        #Instantiates all pages  
        login_page = LoginPage(self.window)
        signup_page = SignupPage(self.window)
        order_page = OrderPage(self.window)
        history_page = OrderHistoryPage(self.window)
        #Define navigation paths between pages
        login_page.set_navigation(signup_page, order_page)
        signup_page.set_navigation(login_page, order_page)
        order_page.set_navigation(login_page, history_page)
        history_page.set_navigation(login_page, order_page)

    def mainloop(self):
        #Runs the full Tkinter GUI loop
        self.window.mainloop()

#------RUN PROGRAM-------
#Entry point for program execution
if __name__ == "__main__":
    app = NutriTeenWindow()
    app.mainloop()
