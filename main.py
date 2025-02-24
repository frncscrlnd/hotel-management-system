from datetime import datetime
from typing import List, Union, Dict
 
class Hotel:
    def _init_(self):
        self.reservations: Dict[str, 'HotelReservation'] = {}
        self.customers: Dict[str, 'Customer'] = {}
 
class Customer:
    def _init_(self, id: str, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
 
    def _str_(self) -> str:
        return f"ID: {self.id}, Name: {self.name} {self.surname}"
 
class HotelReservation:
    def _init_(self, customer: Customer, reservation_id: str, room: str, check_in: datetime, check_out: datetime):
        self.customer = customer
        self.reservation_id = reservation_id
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
 
    def _str_(self) -> str:
        return (f"Customer ID: {self.customer.id}, Reservation ID: {self.reservation_id}, "
                f"Room: {self.room}, Check-in: {self.check_in.strftime('%d/%m')}, "
                f"Check-out: {self.check_out.strftime('%d/%m')}")
 
    def total_nights(self) -> int:
        return (self.check_out - self.check_in).days
    

class HotelManager:
    hotel = Hotel()
    _current_year = datetime.now().year  # Cached at class level for all methods

    @classmethod
    def _get_input(cls, prompt: str) -> str:
        """Centralized input validation."""
        while not (value := input(prompt).strip()):
            print("Input cannot be empty.")
        return value

    @classmethod
    def _parse_date(cls, date_str: str) -> datetime:
        try:
            return datetime.strptime(f"{date_str}/{cls._current_year}", "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD/MM.")

    @classmethod
    def _print_list(cls, items: list, empty_msg: str) -> None:
        """Reusable list printing."""
        print(empty_msg) if not items else [print(f"  {item}") for item in items]

    @classmethod
    def add_customer(cls) -> None:
        id = cls._get_input("Enter the ID: ")
        if id in cls.hotel.customers:
            print(f"Customer ID {id} already exists!")
            return
        cls.hotel.customers[id] = Customer(id, cls._get_input("Enter the name: "), cls._get_input("Enter the surname: "))
        print(f"Customer ID {id} added successfully!")

    @classmethod
    def display_customers(cls) -> None:
        cls._print_list(list(cls.hotel.customers.values()), "No customers found.")

    @classmethod
    def find_customer(cls, id: str) -> Union[Customer, str]:
        return cls.hotel.customers.get(id, "Customer not found")