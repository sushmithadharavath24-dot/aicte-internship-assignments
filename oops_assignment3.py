#program1:bank account class
import datetime  
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    def display(self):
        print("\nAccount Details")
        print("Name:", self.name)
        print("Balance:", self.balance)
        print("Date:", datetime.datetime.now()) 
name = input("Enter Name: ")
balance = int(input("Enter Initial Balance: "))
acc = BankAccount(name, balance)
while True:
    print("\n1 Deposit")
    print("2 Withdraw")
    print("3 Display")
    print("4 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        amt = int(input("Enter amount: "))
        acc.deposit(amt)
    elif choice == "2":
        amt = int(input("Enter amount: "))
        acc.withdraw(amt)
    elif choice == "3":
        acc.display()
    elif choice == "4":
        break
#program2:Library Management System
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print("Book Added")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book Removed")
        else:
            print("Book Not Found")
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book Issued")
        else:
            print("Book Not Available")
    def return_book(self, book):
        self.books.append(book)
        print("Book Returned")
    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)
lib = Library()
while True:
    print("\n1 Add Book")
    print("2 Remove Book")
    print("3 Issue Book")
    print("4 Return Book")
    print("5 Display Books")
    print("6 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        book = input("Enter book name: ")
        lib.add_book(book)
    elif choice == "2":
        book = input("Enter book name: ")
        lib.remove_book(book)
    elif choice == "3":
        book = input("Enter book name: ")
        lib.issue_book(book)
    elif choice == "4":
        book = input("Enter book name: ")
        lib.return_book(book)
    elif choice == "5":
        lib.display_books()
    elif choice == "6":
        break
  #program3:Calculator Class with Exception Handling
  class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
calc = Calculator()
while True:
    print("\n1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")
    choice = input("Enter choice: ")
    if choice == "5":
        break
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == "1":
            print("Result:", calc.add(a, b))
        elif choice == "2":
            print("Result:", calc.subtract(a, b))
        elif choice == "3":
            print("Result:", calc.multiply(a, b))
        elif choice == "4":
            print("Result:", calc.divide(a, b))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
#program4:Billing System (OOP-based)
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity
class Bill:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def calculate_total(self):
        total = 0
        for p in self.products:
            total += p.total_price()
        return total
    def display_bill(self):
        print("\n------ FINAL BILL ------")
        print("Name   Price   Qty   Total")
        for p in self.products:
            print(p.name, "   ", p.price, "   ", p.quantity, "   ", p.total_price())
        total = self.calculate_total()
        tax = total * 0.1  
        final = total + tax
        print("------------------------")
        print("Total:", total)
        print("Tax (10%):", tax)
        print("Final Amount:", final)
bill = Bill()
while True:
    print("\n1 Add Product")
    print("2 Show Bill")
    print("3 Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter product name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        p = Product(name, price, quantity)
        bill.add_product(p)
    elif choice == "2":
        bill.display_bill()
    elif choice == "3":
        break
