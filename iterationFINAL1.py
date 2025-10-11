#NutriTeen- Internal Assessment Iteration 1

from tkinter import ttk

#additional non-core libraries - importation of modules
from tkinter import *
#from playsound import playsound
from tkinter import scrolledtext
from random import*
from tkinter import messagebox

#formatting constants
PX = 32
PY = 22
H = ("Times Roman", '14', "bold")
H1 = ("Arial", '14', "bold")
SH = ("Time", '12',)

#support class
#all four pages inherit it
class NavigationPage:

    #setting navigation
    def set_navigation(self, back_page, forward_page):
        self.back_page = back_page
        self.forward_page = forward_page
       
    #removing existing grid
    #showing the forward page grid
    def go_forward(self):
        self.frame.grid_remove()
        self.forward_page.frame.grid()
        self.forward_page.showing()

    #removing existing grid
    #showing the previous page grid
    def go_back(self):
        self.frame.grid_remove()
        self.back_page.frame.grid()
        self.back_page.showing()
   
    def showing(self):
        pass

#Class Login Page

class LoginPage(NavigationPage):      
    #This class inherits the support class
    def __init__(self, window):    
        self.frame = Frame(window)
        self.frame.grid(row=0, column=0)
       
        #Widgets for Login Page
       
        #Label
        self.title_label = Label(self.frame, text = "Welcome to NutriTeen",
                                bg = "black", fg = "white", width = 50, padx = PX, pady = PY,
                                font = H)
        self.title_label.grid(columnspan = 4)
       
        #Label
        self.description_label = Label(self.frame, text = "order your NutriTeen!", bg = "navy", fg = "white", width = 50, padx = PX, pady = PY,
                                font = H)
        self.description_label.grid( columnspan = 2)  
       
        #Label
        self.username_label = Label(self.frame, text = "username:", width = 10, pady = PY, padx = PX, font = SH)
        self.username_label.grid(row = 2, column = 0 )        
             
        #Entry
        self.username = Entry(self.frame, width = 15,)
        self.username.grid(row = 2, column = 1 )
       
        #Label
        self.password_label = Label(self.frame, text = "password:",width = 10, pady = PY, padx = PX, font = SH)
        self.password_label.grid(row = 3, column = 0)          
       
        #Entry
        self.password = Entry(self.frame, show = "*", width = 15 )
        self.password.grid(row = 3, column =1 )
       
        #Button    
        self.login = ttk.Button(self.frame, text = 'Login', command = self.go_forward,)
        self.login.grid(row = 4, columnspan = 2, )          
             
        #Label          
        self.description_label = Label(self.frame, text = "-------------------- New Here? --------------------", padx = 10, pady = 10)
        self.description_label.grid(row= 6,columnspan = 2)        

        #Button
        self.sign_up = ttk.Button(self.frame, text = 'Sign up', command = self.go_back)
        self.sign_up.grid(row = 7, columnspan = 2)
     
    def go_forward(self): #go_forward checks validity of the login details
        global user_name
        user_name = self.username.get()
        self.username.delete(0, END)
        user_password = self.password.get()
        self.password.delete(0, END)          
       
        #Searches for existing username in the user_list text file,
        #then if the given password does not match the username, error message is shown
        if user_name in user_list:
            if user_password != user_list[user_name]:
                messagebox.showerror("Incorrect password", "please try again")
                return
        else:
            messagebox.showerror("Incorrect username", "please try again")
            return
        super().go_forward() #means goes forward again to the order page - super() is an instantiated object
       
#Class Sign up Page

class SignupPage(NavigationPage):
    #This class inherits the support class  
    def __init__(self, window):        
        self.frame = Frame(window)
       
        #Widgets for Signup Page
       
        #label        
        self.top_label = Label(self.frame, text = "Create account",
                                    bg = "black", fg = "white", width = 50, padx = PX, pady = PY,
                                    font = H)
        self.top_label.grid(columnspan = 4)
       
        #label
        self.description_label = Label(self.frame, text = "Password must be 8 characters", bg = "navy", fg = "white", width = 50, padx = PX, pady = PY,
                                font = H)
        self.description_label.grid( columnspan = 2)        
       
        #label
        self.username_label = Label(self.frame, text = "username:", pady = 10, padx = 10)
        self.username_label.grid(row=3, column = 0)
       
        #entry
        self.username_entry = ttk.Entry(self.frame, width =20)
        self.username_entry.grid(row=3, column = 1)        
       
        #label
        self.password_label = Label(self.frame, text = "password:", pady = 10, padx = 10)                                                                
        self.password_label.grid(row=4, column = 0)
       
        #entry
        self.password_entry = ttk.Entry(self.frame,  show = "*", width =20)
        self.password_entry.grid(row=4, column = 1)          
       
        #label
        self.confirm_password_label = Label(self.frame, text = "confirm password:", pady = 10, padx = 10)
        self.confirm_password_label.grid(row=5, column = 0)
       
        #entry
        self.confirm_password_entry = ttk.Entry(self.frame, show = "*", width =20)
        self.confirm_password_entry.grid(row=5, column = 1)          
       
        #button  
        self.login_button = ttk.Button(self.frame, text = 'logout ', command = self.go_back)
        self.login_button.grid(row = 6, column = 0)
       
        #button
        self.order_button = ttk.Button(self.frame, text = 'Sign up', command = self.go_forward)
        self.order_button.grid(row = 6, column = 1)
       
    def go_forward(self): #go_forward checks whether user satisfies all conditions for sign up
        global user_name
        user_name = self.username_entry.get()
        self.username_entry.delete(0, END)                
        user_password = self.password_entry.get()
        self.password_entry.delete(0, END)
        confirm_password = self.confirm_password_entry.get()
        self.confirm_password_entry.delete(0, END)        

        if user_name in user_list:
            messagebox.showerror("Username taken", "please signup with different username")
            return
   
        if user_name == "guest":
            messagebox.showerror("Username taken", "please signup with different username")
            return
   
        if user_name == "":
            messagebox.showerror("invalid username","please enter characters!")
            return
        if user_password == "":
            messagebox.showerror("invalid password","please enter characters!")
            return        
        if len(user_password) < 8:
            messagebox.showerror("invalid password","password must be at least 8 characters long!")    
            return
        if confirm_password != user_password:
            messagebox.showerror("invalid confirm password","confirm password must match password!")
            return
       
       
        messagebox.showinfo("Successful Signup","Signup Complete")  

        #writes file to user list text file
        #user_list variable refers to the dictionary created to store all valid usernames and password,saved to (user_list.txt)
        user_list[user_name] = user_password
        with open('user_list.txt', 'w') as f:
            print(user_list, file=f)
        super().go_forward() #means goes forward again to the order page - super() is an instantiated object  

#----------------------Class Order Page-------------------------------------------------------------------

class OrderPage(NavigationPage):
    #This class inherits the support class
    def __init__(self, window):        
        self.frame = Frame(window)
       
        menu_items = list(menu.keys())
        self.orders = {} #each order is saved into the dictionary
       
        #Widgets for Login Page
        #label
        top_label = Label(self.frame, text = "Create Order",
                                    bg = "black", fg = "white", width = 20, padx = PX, pady = PY,
                                    font = H1)
        top_label.grid(columnspan = 3, row = 0)
       
        #label
        self.create = Label(self.frame, width = 5, padx = 130, pady = 1, text= "Down below,\n please click on your desired fillings", bg = "grey", fg = "white",
                                    )
        self.create.grid(columnspan= 3, row = 1)        
       
        #label
        self.cart_label = Label(self.frame, width = 20, padx = PX, pady = PY,text= "Your Cart", bg = "black", fg = "white",
                                    font = H1)
        self.cart_label.grid(column = 6, row = 0)
       
        #label
        self.remove_donut = Label(self.frame, width = 5, padx = 130, pady = 1, text= "To remove a filling in your cart, \n click on the filling below", bg = "grey", fg = "white",
                                    )
        self.remove_donut.grid(column = 5, columnspan= 2, row = 1)
    
        btn = Button(self.frame, text = menu_items[0], bg = "white",  command = lambda:self.order_command(menu_items[0]))
        btn.grid(row = 4, column = 0, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[1], bg = "white",   command = lambda:self.order_command(menu_items[1]))
        btn.grid(row = 4, column = 1, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[2], bg = "white",  command = lambda:self.order_command(menu_items[2]))
        btn.grid(row = 4, column = 2, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[3], bg = "white",  command = lambda:self.order_command(menu_items[3]))
        btn.grid(row = 5, column = 0, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[4], bg = "white",  command = lambda:self.order_command(menu_items[4]))
        btn.grid(row = 5, column = 1, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[5], bg = "white",  command = lambda:self.order_command(menu_items[5]))
        btn.grid(row = 5, column = 2,padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[6], bg = "white",  command = lambda:self.order_command(menu_items[6]))
        btn.grid(row = 6, column = 0, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[7], bg = "white",  command = lambda:self.order_command(menu_items[7]))
        btn.grid(row = 6, column = 1, padx = 5, pady = 5)
        btn = Button(self.frame, text = menu_items[8], bg = "white",  command = lambda:self.order_command(menu_items[8]))
        btn.grid(row = 6, column = 2, padx = 5, pady = 5)        
       
        #List box - containing your cart information
        self.lb_orders = Listbox(self.frame, width =50, height = 20 )
        self.lb_orders.grid(column = 6, columnspan = 5, row = 3, rowspan = 5)  
       
        self.lb_orders.bind("<<ListboxSelect>>", self.lb_click)              
       
        #Button
        self.login_button = ttk.Button(self.frame, text = 'Logout ', command = self.go_back)
        self.login_button.grid(row = 9, column = 0)  
       
        #Button
        self.place_order_button = ttk.Button(self.frame, text = 'Place Order', command = self.go_forward)
        self.place_order_button.grid(row = 9, column = 6)        
   
    def order_command(self, item):
        #adding to orders
        order_count = 0
        if item in self.orders:
            order_count = (self.orders[item] + 1)
        else:
            order_count = 1

        if order_count > 10 :
            messagebox.showerror("Maximum reached","Maximum order is 10!")
        else:
            self.orders[item] = order_count

        self.showing()

    def showing(self):
        #updating the list
        self.lb_orders.delete(0, 100)
        for order in self.orders:
            self.lb_orders.insert(END, order+" x "+str(self.orders[order]))

    def lb_click(self,event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            selected_key = list(self.orders.keys())[index]
            if self.orders[selected_key] > 1:
                self.orders[selected_key] = (self.orders[selected_key] -1)
            elif self.orders[selected_key] > 3:
                    self.orders[selected_key] = (self.orders[selected_key] -2)
            else:
                self.orders.pop(selected_key, None)
            self.showing()
    #lb_click

    def go_forward(self): #conditions before enabling user to place order and view their personal order history
        if not messagebox.askyesno("Confirm Order","Are you sure?"):
            return
        users_order_history = []
        if user_name in order_history:
            users_order_history = order_history[user_name]
        else:
            order_history[user_name] = users_order_history
       
        if len(self.orders) == 0 :
            if not messagebox.askyesno("Confirm Order","No order selected, continue to order history?"):
                return
        else:#only save the order if there is more than 0 donuts
            users_order_history.append(self.orders)
            self.orders = {}
            with open('order_history.txt', 'w') as f:
                print(order_history, file=f)
        super().go_forward() #means goes forward again to the order history page - super() is an instantiated object


    def go_back(self):
        self.orders = {}
        super().go_back()
       
#-----------------------Class Review Page ----------------------------------------------------------------------------

class OrderHistoryPage(NavigationPage):
    #This class inherits the support class
    def __init__(self, window):
        self.frame = Frame(window)

        #Widgets for Order History Page
       
        #Label
        review_label = Label(self.frame, text = "Order History", bg = "black", fg = "white", width = 50, padx = PX, pady = PY,
                                font = H)
        review_label.grid(columnspan = 2)  
       
        #Label
        scroll_label = Label(self.frame, text = "Please Scroll down to see most recent order", bg = "navy", fg = "white", width = 50, padx = PX, pady = PY,
                                font = H)
        scroll_label.grid(columnspan = 3)
       
        #Displays users order history
        self.text_description = Text(self.frame, width = 80, height = 20)
        self.text_description.grid(columnspan = 2, row= 2, )
       
        #Button
        home_button = ttk.Button(self.frame, text = "logout",command = self.go_back)
        home_button.grid(column = 0, row= 7, )
       
        #Button
        another_button = ttk.Button(self.frame, text = "place another order", command = self.go_forward)
        another_button.grid(column = 1, row = 7)                
       
    def showing(self):#Formatting of users order history in the Text
        self.text_description.delete(1.0, END)
        order_no = 0

        if user_name in order_history:
            users_order_history = order_history[user_name]

            for order in users_order_history:
                order_no = order_no +1
                self.text_description.insert(END, "\n\nOrder - "+str(order_no)+'\n')
                for order_item in order:
                    self.text_description.insert(END, order_item+" x "+str(order[order_item])+'\n')    

class NutriTeenWindow():
    def __init__(self):
             
        self.window =Tk()
        # creating fixed geometry of the
        # tkinter window with dimensions 660x500
        #self.window.geometry('660x500')    
        self.window.title("NutriTeen")      
       
        #all four pages/screens equal to its corresponding class      
        login_page = LoginPage(self.window)  
        signup_page = SignupPage(self.window)
        order_page = OrderPage(self.window)
        review_page = OrderHistoryPage(self.window)
       
        #ensures that all four pages/screens has the back and forward functionality
        #which is the support class also known as a base class
        #if not, user can not go to the previous page or the forward page and the widgets will not show
        #                        (back page  , forward page)
        login_page.set_navigation(signup_page, order_page)
        signup_page.set_navigation(login_page, order_page)
        order_page.set_navigation(login_page, review_page)
        review_page.set_navigation(login_page, order_page)
       
    def mainloop(self):
        self.window.mainloop()
 
#Main routine
if __name__ == "__main__":
    #menu of all 9 fillings in chronological order
    menu = {
        "lettuce": 1.00,
        "tomato": 1.00,
        "cheese": 1.00,
        "cucumber": 1.00,
        "chicken": 1.00,
        "ham": 1.00,
        "celery": 1.00,
        "avocado": 1.00,
        "egg": 1.00,
    }

    #text file containing order history in a dictionary
    try:
        order_history  = eval(open('order_history.txt', 'r').read())
        #If not found it creates this
    except FileNotFoundError:
        #default value
        order_history = {}
       
    #text file containing registered usernames and password    
    try:
        user_list  = eval(open('user_list.txt', 'r').read())
        #If not found it creates this
    except FileNotFoundError:
        #default value
        user_list = {"guest": "guest"}        
    user_name = "guest"
   
    window = NutriTeenWindow()    
    window.mainloop()

