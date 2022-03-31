from collections import UserDict

class Field():
    pass



class AddressBook(UserDict, Field):
    def add_record (self, user):
        self.data[Record.user_name] = Record.user_phone

    def print_dict(self, *args):
        print (self.data)


    

    

class Name(Field):
    def __init__(self, n, s=None):
        self.name = n
        self.surname = s
    


class Phone(Field):
    phone = None


class Record(AddressBook, Field):
    user_name = Name(input ("Enter user Name: "))
    user_phone = []

    def add_phone(self, phone):
        p = Phone()
        p.phone = phone
        self.user_phone.append(p)
        def surname (surname):           
            if surname == None:
                return ""
            else:
                return surname
        result = print (f"for {self.user_name.name} {surname(self.user_name.surname)} add new phone {phone}." )

        
    def del_phone (self, phone):
        for phones in self.user_phone:
            if phones.phone == phone:
                self.user_phone.remove(phones)
                print (f"Phone {phone} successfully deleted")

    def change_phone (self, phone_one, phone_two):
        for phones in self.user_phone:
            if phones.phone == phone_one:
                phones.phone = phone_two
                print ("Phone successfully updated")
            else:
                print (f"{phone_one} is not found!")
                

    def print_all_phones(self):
        for i in self.user_phone:
            print (i.phone)

    def surname (self):
        print (self.user_name.surname())


r = Record()
r.add_phone ("111111")
r.add_phone ("222222")
r.print_all_phones()
#r.del_phone("111111")
#r.print_all_phones()
#r.change_phone ("111111", "9")
#r.change_phone ("222222", "9")
#r.print_all_phones()

sd = AddressBook()
sd.add_record(r)
sd.print_dict ()

#ar = AddressBook()
#ar.add_record()
#r.surname()

