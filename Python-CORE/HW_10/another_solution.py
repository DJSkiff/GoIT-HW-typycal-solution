from collections import UserDict
from typing import Optional, List


class Field:
    """Fields of records in contact book : name , phone/phones , etc."""

    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    """Phone of the contact"""

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __str__(self):
        return f"Phone:{self.value}"


class Record:
    """Records(contacts) in users contact book.
    Only one name , but it can be more than one phone"""

    def __init__(self, name: str, phones: List[str] = None) -> None:
        if phones is None:
            self.phones = []
        else:
            self.phones = [Phone(p) for p in phones]
        self.name = Name(name)

    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phones:
            if p.value == phone:
                return p

    def delete_phone(self, phone: str) -> None:
        phone_to_delete = self.find_phone(phone)
        self.phones.remove(phone_to_delete) if phone_to_delete else None

    def edit_phone(self, old_phone, new_phone) -> None:
        new_phone = Phone(new_phone)
        phone_to_remove = self.find_phone(old_phone)
        if phone_to_remove:
            self.phones.remove()
            self.phones.append(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def __repr__(self) -> str:
        return f"Contact name: {self.name.value}, phones {[p.value for p in self.phones]}"


class AddressBook(UserDict):
    """All contacts data"""

    def add_record(self, rec: Record) -> None:
        # new_record = Record(record[0], record[1:])
        self.data[rec.name.value] = rec

    def find_record(self, value: str) -> Optional[Record]:
        return self.data.get(value)

    def delete_record(self, value: str) -> None:
        self.data.pop(value)

    def __str__(self):
        return str(self.data)


def main():
    book = AddressBook()
    rec = Record('Volodymyr')

    book.add_record(Record("Yehor", ("063 666 99 66", "048 722 22 22")))
    book.add_record(Record("Pavel"))  # "063 666 66 66", "048 222 22 22"
    book.add_record(rec)
    print(book)

    record = book.find_record("Pavel")
    book.delete_record("Yehor")

    print("#" * 10)
    print(book)
    print(record)
    print("\n")
    print("#" * 10)
    record.delete_phone("048 222 22 22")
    record.edit_phone("095 666 66 66", "067 666 66 66")
    record.add_phone('035 890 67 87')
    record.add_phone('789 567 45 34')
    print(record)


if __name__ == '__main__':
    main()
