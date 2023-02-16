# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass

        # This is a constructor that initializes the attributes of the class.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''

    # The function get_cost() returns the cost of the item
    # return: The cost of the item
    def get_cost(self):
        return self.cost

    # get Function  It returns the quantity of the item.
    def get_quantity(self):
        # return: The quantity of the item
        return self.quantity

    # The __str__ function is a special function that is called when you print an object
    def __str__(self):
        return f"""
Country:   {self.country}
Code:      {self.code}
product:   {self.product}
cost:      {self.cost}
quantity:  {self.quantity}
"""


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Shoe_list = [] is a list that will be used to store a list of objects of shoes.
shoe_list = []


# ==========Functions outside the class==============

# This function reads in the shoes data from the file 'shoes' and returns a list of lists
def read_shoes_data():
    try:
        # This is a context manager that opens the file and closes it automatically.
        with open("inventory.txt", "r") as read_shoes_data_file:

            # Skipping the first line of the file.
            next(read_shoes_data_file)
            print(read_shoes_data_file.readline())

            # Reading the file line by line.
            for file_read in read_shoes_data_file:
                # print(file_read)

                # Removing the new line character from the file and splitting the data into a list.
                get_data = file_read.strip('\n').split(",")

                # This is called unpacking. It is unpacking the list into individual variables.
                country, code, product, cost, quantity = get_data

                # Converting the cost to a float.
                cost = float(cost)

                # Converting the quantity to an integer.
                quantity = int(quantity)

                # Creating an object of the class Shoe.
                shoe = Shoe(country, code, product, cost, quantity)

                # Adding the shoe object to the list.
                shoe_list.append(shoe)

    # This is a try-except block. It is used for error handling.
    except FileNotFoundError:
        print("File not found.")
    except:
        print("An error occurred.")

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

 # This is a function that captures the user input and stores it in the variables.
# define capture shoe function
def capture_shoes():
    # This is a function that captures the user input and stores it in the variables.
    country = input("Enter your Country : ")
    code = input("Enter Your Code : ")
    product = input("Enter Your Product Name : ")

    # The above code is asking the user to input a value for cost.
    while True:
        try:
            cost = float(input("Enter Your cost Value: "))
            break
        # The above code is asking the user to input a number for the cost of the item. If the user inputs a string, the
        # code will print "Invalid input. Please enter a valid number for the cost."
        except ValueError:
            print("Invalid input. Please enter a valid number for the cost.")
    while True:
        try:
            # Asking the user to enter the quantity of the product.
            quantity = int(input("Enter You Quantity in  number : "))
            break

        # The above code is checking to see if the user input is a valid number. If it is not, it will print an error
        # message.
        except ValueError:
            print("Invalid input. Please enter a valid number for the quantity.")

    # Creating an object of the class Shoe.
    shoe = Shoe(country, code, product, cost, quantity)

    # This is a string that is formatted using the f-string.
    add_dict = f"{country},{code},{product},{cost},{quantity}"

    # print(add_dict)

    # This is a context manager that opens the file and closes it automatically.
    with open("inventory.txt", 'a') as add_file:
        # Adding a new line to the file.
        add_file.write("\n" + add_dict)
        print("added successfully.")


# This function prints out all the shoes in the shoe_list
def view_all():
    # Iterating over the shoe_list and printing the details of the shoes returned from the __str__ function.
    for show_shoe in shoe_list:
        print(show_shoe)

    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def re_stock():
    # Finding the shoe object with the lowest quantity.
    low_quantity = min(shoe_list, key=lambda x: x.quantity)

    # This is a string that is formatted using the f-string.
    add_quantity = input(f"""The quantity of {low_quantity.product} has the lowest quantity 
Select one the following options
..............................................................
Yes -  Enter the new quantity you want to add to Update
..............................................................
No  - To return to Main Menu
..............................................................
>>::""").capitalize()

    # This is a conditional statement that checks if the user wants to add the quantity of the shoe with the lowest
    # quantity.
    if add_quantity == "Yes":
        while True:
            try:
                new_qty = int(input(f"Enter New {low_quantity.product} Quantity : "))
                break
            except ValueError:
                print("Invalid Quantity, Please Enter a valid quantity")

        # Updating the quantity of the shoe with the lowest quantity.
        low_quantity.quantity = new_qty
        print(f"{low_quantity.product}  Quantity Re-stock Successfully")

    # if user select no return back to menu
    elif add_quantity == "No":
        main_menu()

    # use tryand exception to catch error
    try:
        with open("inventory.txt", 'w') as re_stock_file:

            # This is writing the header of the file.
            re_stock_file.write("country, code, product,cost, quantity\n")

            # Iterating over the shoe_list and printing the details of the shoes returned from the __str__ function.
            for shoe_re_in_stock in shoe_list:
                # This is writing the details of the shoes to the file.
                re_stock_file.write(f"{shoe_re_in_stock.country},{shoe_re_in_stock.code},{shoe_re_in_stock.product},\
{shoe_re_in_stock.cost},{shoe_re_in_stock.quantity}\n")
    except:
        print()
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


# This is a function that captures the user input and stores it in the variables.
def seach_shoe():
    # ask for input code
    code = input("Enter the code of the shoe you want to search for: ")
    try:
        # opens the file and closes it automatically.
        with open("inventory.txt", "r") as inventory_file:

            # Iterating over the file and reading the file line by line.
            for line in inventory_file:
                # Removing the new line character from the file and splitting the data into a list.
                data = line.strip().split(",")

                # Checking if the code entered by the user is equal to the code in the file.
                if data[1] == code:
                    # print data by search code
                    print(f"""..............................
Country:    {data[0]}
Code:       {data[1]}
product:    {data[2]}
Cost:       {data[3]}
quantity:    {data[4]}
..............................""")

                    # This is a try-except block. It is used for error handling.
                    return
            print("Shoe not found.")
    except FileNotFoundError:
        print("File not found.")
    except:
        print("An error occurred.")

    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''


# def value_per_item():
#     total_value = 0
#     for shoe_value in shoe_list:
#         cal_shoe = shoe_value.cost * shoe_value.quantity
#         print(f"{shoe_value.product} worthy of {cal_shoe}")
#         total_value += cal_shoe
#         print(f"Total value for each item is : {total_value}")

# The function take value for each item
def value_per_item():
    # Iterating over the shoe_list and printing the details of the shoes returned from the __str__ function.
    for shoe_value in shoe_list:
        # Calculating the value of the shoe.
        value = shoe_value.get_cost() * shoe_value.get_quantity()

        # print out total value
        print(f"The value of {shoe_value.product} is : {value}")

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    # This is a list comprehension. It is creating a list of the quantities of the shoes.
    high_quantity = max(shoe.get_quantity() for shoe in shoe_list)
    for max_show in shoe_list:

        # This is a conditional statement that checks if the quantity of the shoe is equal to the highest quantity.
        if max_show.get_quantity() == high_quantity:
            # print  highest product ang quauntity
            print(f"{max_show.product} is for sale with the highest quantity of {max_show.get_quantity()}.")

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


# ==========Main Menu=============

# This function will open the file inventory.txt and read the data from this file, then create a shoes object with this
# data and append this object into the shoes list. One line in this file represents data to create one object of shoes.
# You must use the try-except in this function for error handling. Remember to skip the first line using your code.
read_shoes_data()


def main_menu():
    # This function is used to display the main menu of the program.
    menu_choice = input(f"""Select one of the following Options below:
CS - To capture Shoes
VA - To view all shoes list
L -  To lowest shoe quantity
S -  To search shoe from the list
V -  To get total value of the shoes
H -  To get highest quantity in the product
Q - Exit
>>::""").lower()

    # This is a conditional statement that checks if the user has entered the option to capture shoes.
    if menu_choice == "cs":
        capture_shoes()

    # This is a conditional statement that checks if the user has entered the option to view all shoes.
    elif menu_choice == "va":
        view_all()

    # This is a conditional statement that checks if the user has entered the option to re-stock the shoe with the
    # lowest quantity.
    elif menu_choice == "l":
        re_stock()

    # This is a conditional statement that checks if the user has entered the option to search for a shoe.
    elif menu_choice == "s":
        seach_shoe()

    # This is a conditional statement that checks if the user has entered the option to get the total value of the
    # shoes.
    elif menu_choice == "v":
        value_per_item()

    # This is a conditional statement that checks if the user has entered the option to get the highest quantity of
    # the shoes.
    elif menu_choice == "h":
        highest_qty()

    # This is a conditional statement that checks if the user has entered the option to exit the program.
    elif menu_choice == "q":
        quit()

    # This is a conditional statement that checks if the user has entered the option to exit the program.
    else:
        print("Invalid Choice, Please try again")


'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

# A while loop that will run the main_menu function until the user enters 'q' to quit.
while True:
    main_menu()
