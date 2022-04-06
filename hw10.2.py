from collections import UserDict

class Field():
    pass

class AddressBook(UserDict):

    def add_record (self,k, v):
        super().__setitem__(k, v)

   

class Name(Field):
    def __init__(self, n, s=None):
        self.name = n
        self.surname = s

    def __repr__(self):
        return f"{self.name}"

class Phone(Field):
    phone = None
    def __init__(self, phone = None):
        self.phone = phone

    def __repr__(self):
        return f"{self.phone}"

class Record():
    
    def __init__ (self, name, phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone (self, phone):
        self.phones.append(phone)
        print (f"for {self.name} add new phone {phone}." )
        
    def del_phone (self, phone):
        for p in self.phones:
            if p == phone:
                self.phones.remove(p)
                print (f"Phone {p} successfully deleted")

    def change_phone (self, phone_one, phone_two):
        i = 0                                                          # Лічильник для проходження і заміни елемента в списку
        for p in self.phones:
            
            if p == phone_one:
                self.phones[i] = phone_two
                print ("Phone successfully updated")
            i += 1
        else:
            print (f"Phone {phone_one} is not found!")
                

    def print_all_phones(self, ):
        for p in self.phones:
            print (f"{p}")

user = Phone ("06655")
user_name = Name ("Vadym")
vadym_r = Record (user_name, user)
phone = Phone ("063-710-61-94")
vadym_r.add_phone (phone)
actual_phone = Phone ("050-352-352-3")
vadym_r.change_phone (user, actual_phone)
new_phone = Phone ("0-800-000-0000")
vadym_r.change_phone (new_phone, actual_phone)
vadym_r.print_all_phones()
vadym_r.add_phone (user)
vadym_r.print_all_phones()
vadym_r.del_phone (user)
vadym_r.print_all_phones()
vadym_page = AddressBook ()
vadym_page.add_record (vadym_r.name, vadym_r.phones)
print (vadym_page)