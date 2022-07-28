# Contact Book
# Generate contact book using user inputs and add new contact edit or delete existing contacts and view details.
from numpy import delete
from person_info import *
logo = """
  ,---.     ,--.   ,--.                                ,-----.                ,--.
 /  O  \  ,-|  | ,-|  |,--.--. ,---.  ,---.  ,---.     |  |) /_  ,---.  ,---. |  |,-.
|  .-.  |' .-. |' .-. ||  .--'| .-. :(  .-' (  .-'     |  .-.  \| .-. || .-. ||     /
|  | |  |\ `-' |\ `-' ||  |   \   --..-'  `).-'  `)    |  '--' /' '-' '' '-' '|  \  \
`--' `--' `---'  `---' `--'    `----'`----' `----'     `------'  `---'  `---' `--'`--'
                                                                                       """

print(logo)
contact = {0: {"Name": "Myself", "Phone": "1232221023",
               "Email": "jin@python.com"}, 0: {"Name": "Myself", "Phone": "1232221023",
                                               "Email": "jin@python.com"}, }
system_on = True
while system_on:
    print("\n     === Contact book ===      ")
    print("\n1.) Add New Contact")
    print("2.) Search Contact")
    print("3.) Display Contacts")
    print("4.) Edit Contact")
    print("5.) Delete Contact")
    print("6.) Exit")
    user_option = input("Enter your choice: ")
    if user_option == "1":
        name = input("\nWhat is the name?: ").title()
        phone_number = input("What is the phone number?: ")
        email = input("What is the email? ")
        person = PersonInfo(name, phone_number, email)
        person.add_items(contact, name, phone_number, email)
        print(f"{name}'s information has been added to the contact book.")
    elif user_option == "2":
        search_contact(contact)
    elif user_option == "3":
        if contact == {}:
            print("Contact book empty.")
        else:
            print("\n    === Current Contacts ===       ")
            print(contact)
    elif user_option == "4":
        edit_contact(contact)
    elif user_option == "5":
        delete_info(contact)
        # which_user = input(
        #     "Which user's info would you like to delete?: ").title()
        # contact = {a: b for a, b in contact.items() if b['Name'] != which_user}
        # print(f"{which_user} deleted from the contact book. ")
    elif user_option == "6":
        print("Good bye!")
        system_on = False
