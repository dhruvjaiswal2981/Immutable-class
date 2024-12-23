from datetime import date
from typing import List
from copy import deepcopy

class Address:
    """
    A class to represent an address.
    """

    def __init__(self , street: str , city: str, state: str, zip_code:str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return f"Address(street='{self.street}' , city='{self.city}' , state='{self.state}' , zip_code = '{self.zip_code}')"
    
    def __eq__(self, other):
        return (
            isinstance(other, Address) and
            self.street == other.street and
            self.city == other.city and
            self.state == other.state and
            self.zip_code == other.zip_code 
        )
    
class ImmutablePerson:

    """
    Immutable class to represent a person
    """
    def __init__(self , name:str , id:str , date_of_joining:date , addresses: List[Address]):
        self._name = name
        self._id = id
        self._date_of_joining = date_of_joining

        # Deep copy of addresses to ensure immutability
        self._addresses = deepcopy(addresses)

    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def date_of_joining(self):
        return self._date_of_joining
    
    @property
    def addresses(self):
        # Returning a copy to ensure immutability
        return deepcopy(self._addresses)
    
    def __repr__(self):
        return (f"ImmutablePerson(name='{self.name}' , id='{self.id}', "
                f"date_of_joining={self.date_of_joining}, addresses={self.addresses})")
    
        
        

# Example Usage:


if __name__ == "__main__":
    addr1 = Address("123 Main" , "Springfield" , "IL" , "62701")
    addr2 = Address("456 Elm St" , "Springfield" , "IL" , "62702")
    person = ImmutablePerson("John Doe" , "ID123" , date(2024 , 12 , 1), [ addr1 , addr2])
    print(person)


    # Attempting to modify the addresses list
    addresses = person.addresses
    addresses.append(Address("789 Maple St", "Springfield" , "IL", "62703"))

    # The original person's addresses remain unchanged
    print(person)