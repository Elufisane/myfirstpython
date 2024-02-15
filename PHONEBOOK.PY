phonebook = {'Alice Smith': {'phone_number': '844-695-8195', 'email': 'alice.smith@yahoo.com'}, 'Bob Jones': {'phone_number': '133-235-2620', 'email': 'bob.jones@yahoo.com'}, 'Charlie Brown':
  {'phone_number': '975-319-6150', 'email': 'charlie.brown@yahoo.com'}, 'Diana Garcia': {'phone_number': '390-989-4289', 'email': 'diana.garcia@yahoo.com'}, 'Emma Wilson': {'phone_number': '394-713-7881', 'email': 'emma.wilson@hotmail.com'}, 'Frank Lee': {'phone_number': '536-888-5856', 'email': 'frank.lee@yahoo.com'}, 'George Miller': {'phone_number': '779-778-7419', 'email': 'george.miller@hotmail.com'}, 'Helen White': {'phone_number': '398-740-9626', 'email': 'helen.white@yahoo.com'}, 'Isaac Thompson': {'phone_number': '900-764-5905', 'email': 'isaac.thompson@hotmail.com'}, 'James Davis': {'phone_number': '139-129-8252', 'email': 'james.davis@hotmail.com'}, 'Katherine Lopez': {'phone_number': '380-662-9556', 'email': 'katherine.lopez@gmail.com'}, 'Mark Robinson': {'phone_number': '277-616-1762', 'email': 'mark.robinson@hotmail.com'}, 'Nicole Williams': {'phone_number': '896-710-3192', 'email': 'nicole.williams@hotmail.com'}, 'Olivia Moore': {'phone_number': '857-550-8320', 'email': 'olivia.moore@gmail.com'}, 'Peter Clark': {'phone_number': '197-161-4389', 'email': 'peter.clark@gmail.com'}, 'Richard Baker': {'phone_number': '565-319-5041', 'email': 'richard.baker@yahoo.com'}, 'Sarah Allen': {'phone_number': '839-332-3839', 'email': 'sarah.allen@hotmail.com'}, 'Thomas Garcia': {'phone_number': '395-946-1814', 'email': 'thomas.garcia@yahoo.com'}, 'Victoria Hernandez': {'phone_number': '742-184-2957', 'email': 'victoria.hernandez@yahoo.com'}, 
 'William Johnson': {'phone_number': '476-588-3094', 'email': 'william.johnson@hotmail.com'}}

for _ in range(1, 10 ):
      print("\nPhonebook Menu:")
      print("1. View all contacts")
      print("2. Save a contact")
      print("3. Delete a contact")
      
     
      
      
      userinput = (input("Enter 1-3: "))
      
      if userinput == "1":
          if phonebook:
           print(f"\nphonebook: ")
           for name, phonenumber in phonebook.items():
               print(f"{name}: {phonenumber}")
          else:
              print("Empty")  
      
      elif userinput == "2":
          name = input("Enter the Full name: ")
          phone_number = input("Enter the Phone number: ")
          Email = input("Enter the Email: ")
          contact = {'phone_number': phone_number, 'email': Email}
          phonebook[name] = contact
          print("\nContact saved successfully.")

      elif userinput == "3":
          delname = input("Enter the name of the contact you want to delete: ")
          if delname in phonebook:
              del phonebook[delname]
              print("\nContact deleted successfully.")
          else:
               print("\nContact not found.")

       
      else  :
          print("Invalid Input, please try again.")


# delete = input("Enter ")
            
# phonebook.pop(delete)

# print(f"Successful {phonebook}")
          
