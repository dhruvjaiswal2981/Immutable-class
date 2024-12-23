# ImmutablePerson Example

This project demonstrates the implementation of an immutable `ImmutablePerson` class, where the object's properties cannot be modified after creation. Additionally, it includes an `Address` class to represent individual addresses.

## Features

- **Address Class**
  - Represents an address with `street`, `city`, `state`, and `zip_code`.
  - Supports comparison (`__eq__`) and readable string representation (`__repr__`).

- **ImmutablePerson Class**
  - Represents a person with a name, ID, date of joining, and a list of addresses.
  - Enforces immutability by:
    - Using private attributes (`_name`, `_id`, `_date_of_joining`, `_addresses`).
    - Providing only getter methods for access.
    - Ensuring deep copies of the addresses list when accessed or modified.

## Tech Language 

- Python 3.8 or above.

## Usage

1. Import the `Address` and `ImmutablePerson` classes in your script.
2. Create instances of the `Address` class to represent individual addresses.
3. Pass the addresses to the `ImmutablePerson` constructor to create an immutable person instance.

### Example Code

    ```python
    from datetime import date
    from your_module_name import Address, ImmutablePerson

    # Create address instances
    addr1 = Address("123 Main", "Springfield", "IL", "62701")
    addr2 = Address("456 Elm St", "Springfield", "IL", "62702")

    # Create an immutable person
    person = ImmutablePerson("John Doe", "ID123", date(2024, 12, 1), [addr1, addr2])

    # Display the person object
    print(person)

    # Attempt to modify the addresses list
    addresses = person.addresses
    addresses.append(Address("789 Maple St", "Springfield", "IL", "62703"))

    # Confirm immutability
    print(person)

    ```

### Output 

    ```bash
    ImmutablePerson(name='John Doe', id='ID123', date_of_joining=2024-12-01, addresses=[Address(street='123 Main', city='Springfield', state='IL', zip_code='62701'), Address(street='456 Elm St', city='Springfield', state='IL', zip_code='62702')])
    ImmutablePerson(name='John Doe', id='ID123', date_of_joining=2024-12-01, addresses=[Address(street='123 Main', city='Springfield', state='IL', zip_code='62701'), Address(street='456 Elm St', city='Springfield', state='IL', zip_code='62702')])


