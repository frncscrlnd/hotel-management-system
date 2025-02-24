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