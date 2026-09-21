# ============================================================
#                  RAILSATHI
#             RAILWAY RESERVATION SYSTEM
# ============================================================

# -------------------- CONSTANTS -----------------------------

MAX_SEATS = 5
START_PNR = 1001


# ============================================================
#                    PASSENGER CLASS
# ============================================================

class Passenger:
    def __init__(self, pnr, name, age, train_no, source, destination):
        self.pnr = pnr
        self.name = name
        self.age = age
        self.train_no = train_no
        self.source = source
        self.destination = destination


# ============================================================
#                 LINKED LIST NODE
# ============================================================

class Node:
    def __init__(self, passenger):
        self.passenger = passenger
        self.next = None


# ============================================================
#                 CONFIRMED PASSENGER LIST
# ============================================================

class PassengerLinkedList:

    def __init__(self):
        self.head = None

    # Insert passenger at the end
    def insert(self, passenger):
        new_node = Node(passenger)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Delete passenger using PNR
    def delete(self, pnr):

        if self.head is None:
            return None

        # If first passenger has the PNR
        if self.head.passenger.pnr == pnr:
            deleted = self.head.passenger
            self.head = self.head.next
            return deleted

        current = self.head

        while current.next is not None:

            if current.next.passenger.pnr == pnr:
                deleted = current.next.passenger
                current.next = current.next.next
                return deleted

            current = current.next

        return None

    # Linear Search
    def search(self, pnr):

        current = self.head

        while current is not None:

            if current.passenger.pnr == pnr:
                return current.passenger

            current = current.next

        return None

    # Convert linked list into Python list
    def to_list(self):

        passengers = []
        current = self.head

        while current is not None:
            passengers.append(current.passenger)
            current = current.next

        return passengers

    # Display linked list
    def display(self):

        if self.head is None:
            print("\nNo confirmed passengers.")
            return

        print("\n" + "=" * 75)
        print("                 CONFIRMED PASSENGERS")
        print("=" * 75)

        current = self.head

        while current is not None:

            p = current.passenger

            print(
                f"PNR: {p.pnr} | "
                f"Name: {p.name} | "
                f"Age: {p.age} | "
                f"Train: {p.train_no} | "
                f"{p.source} -> {p.destination}"
            )

            current = current.next

        print("=" * 75)


# ============================================================
#                       QUEUE
# ============================================================

class WaitingQueue:

    def __init__(self):
        self.queue = []

    # Enqueue
    def enqueue(self, passenger):
        self.queue.append(passenger)

    # Dequeue
    def dequeue(self):

        if len(self.queue) == 0:
            return None

        return self.queue.pop(0)

    # Search waiting passenger
    def search(self, pnr):

        for passenger in self.queue:

            if passenger.pnr == pnr:
                return passenger

        return None

    # Remove passenger from waiting queue
    def remove(self, pnr):

        for i in range(len(self.queue)):

            if self.queue[i].pnr == pnr:
                return self.queue.pop(i)

        return None

    # Display queue
    def display(self):

        if len(self.queue) == 0:
            print("\nWaiting list is empty.")
            return

        print("\n" + "=" * 75)
        print("                    WAITING LIST")
        print("=" * 75)

        position = 1

        for passenger in self.queue:

            print(
                f"{position}. "
                f"PNR: {passenger.pnr} | "
                f"Name: {passenger.name} | "
                f"Age: {passenger.age}"
            )

            position += 1

        print("=" * 75)


# ============================================================
#                         STACK
# ============================================================

class CancellationStack:

    def __init__(self):
        self.stack = []

    # Push
    def push(self, passenger):
        self.stack.append(passenger)

    # Pop
    def pop(self):

        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    # Display stack
    def display(self):

        if len(self.stack) == 0:
            print("\nNo cancellation history.")
            return

        print("\n" + "=" * 75)
        print("                 CANCELLATION HISTORY")
        print("=" * 75)

        for passenger in reversed(self.stack):

            print(
                f"PNR: {passenger.pnr} | "
                f"Name: {passenger.name} | "
                f"Train: {passenger.train_no}"
            )

        print("=" * 75)


# ============================================================
#                    BUBBLE SORT
# ============================================================

def bubble_sort(passengers):

    n = len(passengers)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if passengers[j].pnr > passengers[j + 1].pnr:

                passengers[j], passengers[j + 1] = (
                    passengers[j + 1],
                    passengers[j]
                )

    return passengers


# ============================================================
#                    BINARY SEARCH
# ============================================================

def binary_search(passengers, pnr):

    low = 0
    high = len(passengers) - 1

    while low <= high:

        mid = (low + high) // 2

        if passengers[mid].pnr == pnr:
            return passengers[mid]

        elif passengers[mid].pnr < pnr:
            low = mid + 1

        else:
            high = mid - 1

    return None


# ============================================================
#                 DISPLAY SORTED PASSENGERS
# ============================================================

def display_sorted_passengers(passengers):

    if len(passengers) == 0:
        print("\nNo passengers available.")
        return

    sorted_passengers = bubble_sort(passengers.copy())

    print("\n" + "=" * 75)
    print("                 SORTED PASSENGERS")
    print("=" * 75)

    for passenger in sorted_passengers:

        print(
            f"PNR: {passenger.pnr} | "
            f"Name: {passenger.name} | "
            f"Age: {passenger.age} | "
            f"Train: {passenger.train_no}"
        )

    print("=" * 75)


# ============================================================
#                    BOOK TICKET
# ============================================================

def book_ticket(confirmed_list, waiting_queue, next_pnr):

    print("\n" + "=" * 75)
    print("                       BOOK TICKET")
    print("=" * 75)

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Age: "))
    train_no = input("Enter Train Number: ")
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")

    passenger = Passenger(
        next_pnr,
        name,
        age,
        train_no,
        source,
        destination
    )

    confirmed_count = len(confirmed_list.to_list())

    if confirmed_count < MAX_SEATS:

        confirmed_list.insert(passenger)

        print("\nTicket booked successfully!")
        print("PNR Number:", next_pnr)
        print("Status: CONFIRMED")

    else:

        waiting_queue.enqueue(passenger)

        print("\nAll confirmed seats are occupied.")
        print("Passenger added to waiting list.")
        print("PNR Number:", next_pnr)
        print("Status: WAITING")

    return next_pnr + 1


# ============================================================
#                    CANCEL TICKET
# ============================================================

def cancel_ticket(
    confirmed_list,
    waiting_queue,
    cancellation_stack
):

    print("\n" + "=" * 75)
    print("                    CANCEL TICKET")
    print("=" * 75)

    pnr = int(input("Enter PNR Number: "))

    passenger = confirmed_list.delete(pnr)

    # Confirmed passenger found
    if passenger is not None:

        cancellation_stack.push(passenger)

        print("\nTicket cancelled successfully.")
        print("Passenger:", passenger.name)
        print("PNR:", passenger.pnr)

        # Move first waiting passenger to confirmed list
        waiting_passenger = waiting_queue.dequeue()

        if waiting_passenger is not None:

            confirmed_list.insert(waiting_passenger)

            print("\nWaiting-list passenger promoted!")
            print("Passenger:", waiting_passenger.name)
            print("PNR:", waiting_passenger.pnr)
            print("Status: CONFIRMED")

        return

    # Check waiting list
    waiting_passenger = waiting_queue.remove(pnr)

    if waiting_passenger is not None:

        cancellation_stack.push(waiting_passenger)

        print("\nWaiting-list ticket cancelled successfully.")
        print("Passenger:", waiting_passenger.name)
        print("PNR:", waiting_passenger.pnr)

        return

    print("\nPNR not found.")


# ============================================================
#                    SEARCH PASSENGER
# ============================================================

def search_passenger(confirmed_list, waiting_queue):

    print("\n" + "=" * 75)
    print("                    SEARCH PASSENGER")
    print("=" * 75)

    pnr = int(input("Enter PNR Number: "))

    # Linear search in linked list
    passenger = confirmed_list.search(pnr)

    if passenger is not None:

        print("\nPassenger Found!")
        print("PNR         :", passenger.pnr)
        print("Name        :", passenger.name)
        print("Age         :", passenger.age)
        print("Train No.   :", passenger.train_no)
        print("Source      :", passenger.source)
        print("Destination :", passenger.destination)
        print("Status      : CONFIRMED")

        return

    # Search waiting list
    passenger = waiting_queue.search(pnr)

    if passenger is not None:

        print("\nPassenger Found!")
        print("PNR         :", passenger.pnr)
        print("Name        :", passenger.name)
        print("Age         :", passenger.age)
        print("Train No.   :", passenger.train_no)
        print("Source      :", passenger.source)
        print("Destination :", passenger.destination)
        print("Status      : WAITING")

        return

    print("\nPassenger not found.")


# ============================================================
#                BINARY SEARCH PASSENGER
# ============================================================

def binary_search_passenger(confirmed_list):

    passengers = confirmed_list.to_list()

    if len(passengers) == 0:

        print("\nNo confirmed passengers.")
        return

    # Sort first
    passengers = bubble_sort(passengers)

    pnr = int(input("\nEnter PNR Number for Binary Search: "))

    passenger = binary_search(passengers, pnr)

    if passenger is not None:

        print("\nPassenger Found using Binary Search!")

        print("PNR         :", passenger.pnr)
        print("Name        :", passenger.name)
        print("Age         :", passenger.age)
        print("Train No.   :", passenger.train_no)
        print("Source      :", passenger.source)
        print("Destination :", passenger.destination)

    else:

        print("\nPassenger not found.")


# ============================================================
#                    MAIN MENU
# ============================================================

def main():

    confirmed_list = PassengerLinkedList()
    waiting_queue = WaitingQueue()
    cancellation_stack = CancellationStack()

    next_pnr = START_PNR

    while True:

        print("\n")
        print("=" * 75)
        print("                         RAILSATHI")
        print("                 RAILWAY RESERVATION SYSTEM")
        print("=" * 75)

        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Search Passenger")
        print("4. Display Confirmed Passengers")
        print("5. Display Waiting List")
        print("6. Sort Passengers")
        print("7. Binary Search Passenger")
        print("8. Cancellation History")
        print("9. Exit")

        print("=" * 75)

        choice = input("Enter your choice: ")

        if choice == "1":

            next_pnr = book_ticket(
                confirmed_list,
                waiting_queue,
                next_pnr
            )

        elif choice == "2":

            cancel_ticket(
                confirmed_list,
                waiting_queue,
                cancellation_stack
            )

        elif choice == "3":

            search_passenger(
                confirmed_list,
                waiting_queue
            )

        elif choice == "4":

            confirmed_list.display()

        elif choice == "5":

            waiting_queue.display()

        elif choice == "6":

            display_sorted_passengers(
                confirmed_list.to_list()
            )

        elif choice == "7":

            binary_search_passenger(
                confirmed_list
            )

        elif choice == "8":

            cancellation_stack.display()

        elif choice == "9":

            print("\nThank you for using RailSathi!")
            print("Have a safe journey! 🚆")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
#                     PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
