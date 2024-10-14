import customer

def main():
    name = input('Name: ')
    address = input('Address: ')
    phone = input('Phone: ')
    customer_number = input('Customer Number: ')
    mail = input('Include in mailing list? (y/n): ')

    mailing_list = mail.lower() == 'y'

    # Create a Customer instance.
    my_customer = customer.Customer(name, address, phone, customer_number, mailing_list)

    # Display Customer information.
    print('\nCustomer Information')
    print('--------------------')
    print('Name:', my_customer.get_name())
    print('Address:', my_customer.get_address())
    print('Phone:', my_customer.get_phone())
    print('Customer Number:', my_customer.get_customer_number())
    print('Mailing List:', 'Yes' if my_customer.get_mailing_list() else 'No')

if __name__ == "__main__":
    main()
