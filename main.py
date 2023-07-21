# Define a list to store customer data
customers = []

# Define a function for customer registration
def register_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone number: ")
   
    # Create a dictionary to store customer information
    customer = {
        "name": name,
        "email": email,
        "phone": phone,
        "support_tickets": []
    }
   
    # Add the customer to the list
    customers.append(customer)
    print("Customer registered successfully!")

# Define a function for creating support tickets
def create_support_ticket():
    email = input("Enter customer email: ")
    message = input("Enter support ticket message: ")
   
    # Find the customer with the provided email
    customer = next((c for c in customers if c["email"] == email), None)
   
    if customer:
        # Add the support ticket to the customer's support_tickets list
        customer["support_tickets"].append(message)
        print("Support ticket created successfully!")
    else:
        print("Customer not found!")

# Define a function to display customer details
def display_customer_details():
    email = input("Enter customer email: ")
   
    # Find the customer with the provided email
    customer = next((c for c in customers if c["email"] == email), None)
   
    if customer:
        print("Customer Details:")
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print(f"Phone: {customer['phone']}")
        print("Support Tickets:")
        for index, ticket in enumerate(customer['support_tickets'], 1):
            print(f"{index}. {ticket}")
    else:
        print("Customer not found!")

# Main program loop
while True:
    print("\n1. Register Customer")
    print("2. Create Support Ticket")
    print("3. Display Customer Details")
    print("4. Exit")
   
    choice = input("Enter your choice (1/2/3/4): ")
   
    if choice == "1":
        register_customer()
    elif choice == "2":
        create_support_ticket()
    elif choice == "3":
        display_customer_details()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
