class PersonInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.items = {}

    def add_items(self, contact, name, phone, email):
        user_id = len(contact)
        contact[user_id] = {
            "Name": name, "Phone": phone, "Email": email
        }


def search_contact(contact):
    not_correct_info = False
    while not not_correct_info:
        search = input(
            "\n1) Search Name\n2) Search Phone\n3) Search Email\n4) Go to main menu\n")
        if search == "1":
            search_name = input("What is the name?: ").title()
            for name_id, name_info in contact.items():
                if search_name in name_info["Name"]:
                    print(
                        f"\nHere is {search_name}'s contact info: \nUser_ID:{name_id} {name_info}")
                    not_correct_info = True
            if search_name not in name_info["Name"]:
                print(f"\n{search_name} not in contact. Try again.")
                continue
        elif search == "2":
            search_phone = input("What is the phone number?: ")
            for name_id, name_info in contact.items():
                if search_phone == name_info["Phone"]:
                    print(
                        f"Here is what we found: \nUser_ID:{name_id} {name_info}")
                    not_correct_info = True
            if search_phone not in name_info["Phone"]:
                print(f"{search_phone} not in contact. Try again.")
                continue
        elif search == "3":
            search_email = input("What is the email?: ")
            for name_id, name_info in contact.items():
                if search_email == name_info["Email"]:
                    print(
                        f"Here is what we found: \nUser_ID:{name_id} {name_info}")
                    not_correct_info = True
            if search_email not in name_info["Email"]:
                print(f"{search_email} not in contact. Try again.")
                continue
        elif search == "4":
            not_correct_info = True


def edit_contact(contact):
    not_correct_info = False
    while not not_correct_info:
        print(f"\nHere is the current list of contacts:\n{contact}")
        edit_option = input(
            "1) Edit Name\n2) Edit Phone\n3) Edit Email\n4) Go to main menu\n")
        if edit_option == "1":
            target_name = input("Which name would like to change?: ").title()
            edited_name = input(f"Edit) Name: {target_name} to ---> ").title()
            for name_id, name_info in contact.items():
                if target_name in name_info["Name"]:
                    contact[name_id]["Name"] = edited_name
                    print(
                        f"{target_name} has been changed to {edited_name}.")
                    not_correct_info = False

        elif edit_option == "2":
            target_phone = input(
                "Who's phone number would like to change?: ").title()
            for name_id, name_info in contact.items():
                if target_phone in name_info["Name"]:
                    editted_phone = input(
                        f"Change {target_phone}'s current Phone Number to ---> ")
                    for name_id, name_info in contact.items():
                        contact[name_id]["Phone"] = editted_phone
                        print(
                            f"{target_phone}'s phone number has been changed to {editted_phone}.")
                        not_correct_info = True
                else:
                    print(f"{target_phone} not in contact book. Try again.\n")
                    continue
        elif edit_option == "3":
            target_name = input(
                "Who's email would like to change?: ").title()
            for name_id, name_info in contact.items():
                if target_name in name_info["Name"]:
                    editted_email = input(
                        f"Change {target_name}'s current Email to ---> ")
                    for name_id, name_info in contact.items():
                        contact[name_id]["Email"] = editted_email
                        print(
                            f"{target_name}'s email has been changed to {editted_email}.")
                        not_correct_info = True
                else:
                    print(f"{target_name} not in contact book. Try again.\n")
                    continue

        elif edit_option == "4":
            not_correct_info = True


def delete_info(contact):
    confirmed = True
    while confirmed:
        which_user = input(
            "Which user's info would you like to delete? (or 'q' for main menu): ").title()
        for name_id, name_info in contact.items():
            if which_user in name_info["Name"]:
                print(f"\nUser_ID:{name_id} {name_info}")
                confirmation = input("1) Confirm to Delete\n2)Cancel\n")
                if confirmation == "1":
                    contact = {a: b for a, b in contact.items()
                               if b['Name'] != which_user}
                    print(f"{which_user} deleted from the contact book. ")
                    confirmed = False
                    break

            elif confirmation == "2":
                print("Deleting user info cancelled")
                confirmed = False
                break
            elif which_user not in name_info["Name"]:
                print(f"{which_user} not found in Contact Book.")
                break
        if which_user == "q":
            print("Exiting")
            confirmed = False
