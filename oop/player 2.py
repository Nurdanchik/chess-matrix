# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return f'Ваш баланс был пополнен на {amount}. Ваш текущий баланс: {self.balance}'
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             left = self.balance - amount
#             return f'Выполнено. С вашего счета было снято {amount}. Осталось {left}'

#         else:
#             return 'Недостаточно средств.'
    
# zalkar = BankAccount('Zaka', 1000)
# print(zalkar.deposit(1000))
# print(zalkar.withdraw(2200))

# class Contact:
#     all_contacts = []

#     def __init__(self, name, lastname, phone_number):
#         self.name = name
#         self.lastname = lastname
#         self.phone_number = phone_number
#         self.add_contact()

#     def add_contact(self):
#         Contact.all_contacts.append((self.name, self.lastname, self.phone_number))

# class Friend(Contact):
#     def __init__(self, name, lastname, phone_number):
#         super().__init__(name, lastname, phone_number)

#     def play_football_with_me(self):
#         pass 

# class ContactList(list):
#     def search_by_name(self, whom):
#         to_return = []
#         for contact in Contact.all_contacts:
#             if whom == contact[0]:  # Сравниваем имена
#                 to_return.append(contact)
#         return to_return

# contact1 = Contact("Иван", "Иванов", "123456789")
# contact2 = Contact("Петр", "Петров", "987654321")
# contact_list = ContactList()
# result = contact_list.search_by_name("Иван")
# print(result)

