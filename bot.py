from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        if (len(phone) == 10 and phone.isdigit()):
            self.value = phone
        else:
            raise ValueError('Wrong number, expect 10 digits')

    def update_phone(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError('Wrong number, expect 10 digits')


class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone = self.find_phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        phone.update_phone(new_phone)

    def find_phone(self, f_phone) -> Phone:
        phone = list(filter(lambda phone: phone.value == f_phone, self.phones))
        if (not phone):
            return None

        return phone[0]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


book = AddressBook()

john_record = Record("John")
print('john_record', john_record)
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

print('john_record', john_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543212")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223331")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

john.remove_phone('5555555555')
# Видалення запису Jane
book.delete("Jane")
# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)
