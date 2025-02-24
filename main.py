from datetime import datetime
from typing import List, Union, Dict
 
class Hotel:
    def __init__(self):
        self.reservations: Dict[str, 'HotelReservation'] = {}
        self.customers: Dict[str, 'Customer'] = {}
 
class Customer:
    def __init__(self, id: str, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
 
    def __str__(self) -> str:
        return f"ID: {self.id}, Name: {self.name} {self.surname}"
 
class HotelReservation:
    def __init__(self, customer: Customer, reservation_id: str, room: str, check_in: datetime, check_out: datetime):
        self.customer = customer
        self.reservation_id = reservation_id
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
 
    def __str__(self) -> str:
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
 
    @classmethod
    def add_reservation(cls) -> None:
        customer_id = cls._get_input("Enter the customer's ID: ")
        if cls.find_customer(customer_id) == "Customer not found":
            print("Customer not found.")
            return
 
        reservation_id = cls._get_input("Enter the reservation ID: ")
        if reservation_id in cls.hotel.reservations:
            print(f"Reservation ID {reservation_id} already exists!")
            return
 
        try:
            check_in = cls._parse_date(cls._get_input("Enter the check-in date (DD/MM): "))
            check_out = cls._parse_date(cls._get_input("Enter the check-out date (DD/MM): "))
            if check_out <= check_in:
                print("Error: Check-out date must be after check-in date.")
                return
            cls.hotel.reservations[reservation_id] = HotelReservation(
                cls.hotel.customers[customer_id], reservation_id, cls._get_input("Enter the room: "), check_in, check_out
            )
            print(f"Reservation ID {reservation_id} added successfully!")
        except ValueError as e:
            print(e)
 
    @classmethod
    def display_reservations(cls) -> None:
        cls._print_list(list(cls.hotel.reservations.values()), "No reservations found.")
 
    @classmethod
    def find_reservation_by_cid(cls, customer_id: str) -> List[HotelReservation]:
        return [r for r in cls.hotel.reservations.values() if r.customer.id == customer_id] or ["No reservations found."]
 
    @classmethod
    def find_reservation_by_rid(cls, reservation_id: str) -> Union[HotelReservation, str]:
        return cls.hotel.reservations.get(reservation_id, "Reservation not found")
 
    @classmethod
    def delete_reservation(cls, reservation_id: str) -> None:
        if cls.hotel.reservations.pop(reservation_id, None):
            print(f"Reservation ID {reservation_id} deleted successfully!")
        else:
            print("Reservation not found.")
    
    @classmethod
    def total_nights(cls, reservation_id: str) -> Union[int, str]:
        if not (reservation := cls.find_reservation_by_rid(reservation_id)) or isinstance(reservation, str):
            return "Reservation not found"
        return reservation.total_nights()
 
    def main() -> None:
        options = {
            "1": ("Add a customer", HotelManager.add_customer),
            "2": ("Display customers", HotelManager.display_customers),
            "3": ("Find a customer", lambda: print(HotelManager.find_customer(HotelManager._get_input("Enter the ID: ")))),
            "4": ("Add a reservation", HotelManager.add_reservation),
            "5": ("Display reservations", HotelManager.display_reservations),
            "6": ("Find reservations by customer ID",
                lambda: HotelManager._print_list(HotelManager.find_reservation_by_cid(HotelManager._get_input("Enter the customer's ID: ")),
                                              "No reservations found for this customer.")),
            "7": ("Delete a reservation", lambda: HotelManager.delete_reservation(HotelManager._get_input("Enter the reservation ID: "))),
            "8": ("Total nights", lambda: print(f"Total nights: {HotelManager.total_nights(HotelManager._get_input('Enter the reservation ID: '))}")),
            "9": ("Find a reservation by ID", lambda: print(HotelManager.find_reservation_by_rid(HotelManager._get_input("Enter the reservation ID: ")))),
            "10": ("Exit", lambda: None)
        }
 
    while True:
        print("\nHotel Management System:")
        print("\n".join(f"  {k}. {v[0]}" for k, v in options.items()))
        if (choice := HotelManager._get_input("Enter your choice: ")) == "10":
            print("Exiting...")
            break
        options.get(choice, (None, lambda: print("Invalid choice.")))[1]()
 
    if _name_ == "_main_":
        main()
