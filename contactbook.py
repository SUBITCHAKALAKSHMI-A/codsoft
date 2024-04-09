contact_name = []
contact_number = []

def update_contact():
    name_to_update = input("Enter the name of the contact you want to update: ")
    if name_to_update in contact_name:
        index = contact_name.index(name_to_update)
        update_choice = input("Do you want to update the name, number, or both? (name/number/both): ").lower()
        
        if update_choice == "name":
            new_name = input("Enter the new name: ")
            contact_name[index] = new_name
            print("Contact name updated successfully.")

        elif update_choice == "number":
            new_number = input("Enter the new number: ")
            contact_number[index] = new_number
            print("Contact number updated successfully.")

        elif update_choice == "both":
            new_name = input("Enter the new name: ")
            new_number = input("Enter the new number: ")
            contact_name[index] = new_name
            contact_number[index] = new_number
            print("Contact name and number updated successfully.")

        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

num = int(input("Enter the number of contacts to create: "))
for i in range(num):
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact_name.append(name)
    contact_number.append(number)

print("The contact names and numbers are: ")
print("Name:\t\t Contact number:")
for i in range(num):
    if len(contact_number[i]) == 10:
        print("{}\t\t{}".format(contact_name[i].upper(), contact_number[i]))
    else:
        print("Invalid contact number")

update_option = input("Do you want to update any contact? (yes/no): ").lower()
if update_option == "yes":
    update_contact()

# Print the updated contact names and numbers
print("\nUpdated contact names and numbers:")
print("Name:\t\t Contact number:")
for i in range(num):
    if len(contact_number[i]) == 10:
        print("{}\t\t{}".format(contact_name[i].upper(), contact_number[i]))
    else:
        print("Invalid contact number")
