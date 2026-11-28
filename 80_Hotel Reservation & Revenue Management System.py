class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night


class Customer:
    def __init__(self, name):
        self.name = name
        self.booking_history = []


class Booking:
    def __init__(self, booking_id, customer, room, check_in, check_out, total_cost):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.total_stay = check_out - check_in
        self.total_cost = total_cost
        self.status = "Active"


class Hotel:
    def __init__(self):
        self.rooms = []
        self.customers = {}
        self.bookings = []
        self.next_booking_id = 1

    def add_rooms(self):
        room_count = int(input("Enter how many rooms you want to add: "))

        for i in range(room_count):
            print(f"\nRoom {i + 1}")
            room_number = input("Enter room number: ")
            room_type = input("Enter room type: ")
            price = float(input("Enter price per night: "))

            room = Room(room_number, room_type, price)
            self.rooms.append(room)

        print("Room inventory added.")

    def get_customer(self, name):
        if name not in self.customers:
            self.customers[name] = Customer(name)

        return self.customers[name]

    def is_room_available(self, room, check_in, check_out):
        for booking in self.bookings:
            if booking.room.room_number == room.room_number and booking.status == "Active":
                # Overlap check: [check-in, check-out)
                if check_in < booking.check_out and check_out > booking.check_in:
                    return False

        return True

    def add_booking(self):
        name = input("Enter customer name: ")
        room_type = input("Enter room type: ")
        check_in = int(input("Enter check-in day: "))
        check_out = int(input("Enter check-out day: "))

        if check_out <= check_in:
            print("Rejected: Check-out day must be later than check-in.")
            return

        total_stay = check_out - check_in

        matching_rooms = [
            room for room in self.rooms
            if room.room_type.lower() == room_type.lower()
        ]

        if not matching_rooms:
            print("Room type not found.")
            return

        available_rooms = [
            room for room in matching_rooms
            if self.is_room_available(room, check_in, check_out)
        ]

        if not available_rooms:
            print("Rejected: No available room for these dates.")
            return

        # Automatically select the first available room of that type
        room = available_rooms[0]
        customer = self.get_customer(name)

        base_cost = room.price_per_night * total_stay

        # Long-stay discount: 15% for 7+ nights
        discount = 0
        if total_stay >= 7:
            discount = base_cost * 0.15

        after_long_stay_discount = base_cost - discount

        # Loyalty discount: 10% starting from the customer's 3rd booking
        previous_bookings = sum(
            1 for booking in customer.booking_history
            if booking.status == "Active"
        )

        loyalty_discount = 0
        if previous_bookings >= 2:
            loyalty_discount = after_long_stay_discount * 0.10

        total_cost = after_long_stay_discount - loyalty_discount

        booking = Booking(
            self.next_booking_id,
            customer,
            room,
            check_in,
            check_out,
            total_cost
        )

        self.bookings.append(booking)
        customer.booking_history.append(booking)
        self.next_booking_id += 1

        print("\nBooking successful!")
        print("Booking ID:", booking.booking_id)
        print("Room number:", room.room_number)
        print("Total nights:", total_stay)
        print(f"Base cost: €{base_cost:.2f}")
        print(f"Long-stay discount: €{discount:.2f}")
        print(f"Loyalty discount: €{loyalty_discount:.2f}")
        print(f"Final cost: €{total_cost:.2f}")

    def cancel_booking(self):
        booking_id = int(input("Enter booking ID to cancel: "))

        for booking in self.bookings:
            if booking.booking_id == booking_id:
                if booking.status == "Cancelled":
                    print("This booking is already cancelled.")
                    return

                booking.status = "Cancelled"
                print("Booking cancelled.")
                return

        print("Booking ID not found.")

    def show_report(self):
        total_bookings = len(self.bookings)
        active_bookings = [
            booking for booking in self.bookings
            if booking.status == "Active"
        ]
        cancelled_bookings = [
            booking for booking in self.bookings
            if booking.status == "Cancelled"
        ]

        total_revenue = sum(
            booking.total_cost for booking in active_bookings
        )

        print("\n--- HOTEL REPORT ---")
        print("Total bookings:", total_bookings)
        print("Active bookings:", len(active_bookings))
        print("Cancelled bookings:", len(cancelled_bookings))
        print(f"Total revenue: €{total_revenue:.2f}")

        # Revenue by room type
        revenue_by_type = {}

        for booking in active_bookings:
            room_type = booking.room.room_type
            revenue_by_type[room_type] = (
                revenue_by_type.get(room_type, 0) + booking.total_cost
            )

        if revenue_by_type:
            highest_revenue_type = max(
                revenue_by_type, key=revenue_by_type.get
            )
            print(
                "Highest revenue room type:",
                highest_revenue_type,
                f"(€{revenue_by_type[highest_revenue_type]:.2f})"
            )

        # Customer with the most booked nights
        nights_by_customer = {}

        for booking in active_bookings:
            name = booking.customer.name
            nights_by_customer[name] = (
                nights_by_customer.get(name, 0) + booking.total_stay
            )

        if nights_by_customer:
            top_customer = max(nights_by_customer, key=nights_by_customer.get)
            print(
                "Customer with most nights:",
                top_customer,
                f"({nights_by_customer[top_customer]} nights)"
            )

    def show_occupancy(self):
        period_start = int(input("Enter report start day: "))
        period_end = int(input("Enter report end day: "))

        if period_end <= period_start:
            print("Invalid date range.")
            return

        period_nights = period_end - period_start

        print("\n--- ROOM OCCUPANCY ---")

        for room in self.rooms:
            booked_nights = 0

            for booking in self.bookings:
                if (
                    booking.room.room_number == room.room_number
                    and booking.status == "Active"
                ):
                    overlap_start = max(period_start, booking.check_in)
                    overlap_end = min(period_end, booking.check_out)

                    if overlap_end > overlap_start:
                        booked_nights += overlap_end - overlap_start

            occupancy_rate = (booked_nights / period_nights) * 100

            print(
                f"Room {room.room_number}: "
                f"{occupancy_rate:.2f}% occupancy"
            )

    def show_available_rooms(self):
        check_in = int(input("Enter check-in day: "))
        check_out = int(input("Enter check-out day: "))

        if check_out <= check_in:
            print("Invalid date range.")
            return

        available_rooms = [
            room for room in self.rooms
            if self.is_room_available(room, check_in, check_out)
        ]

        print("\nAvailable rooms:")
        if available_rooms:
            for room in available_rooms:
                print(
                    room.room_number,
                    room.room_type,
                    f"€{room.price_per_night:.2f} per night"
                )
        else:
            print("No rooms available for those dates.")

    def run(self):
        self.add_rooms()

        while True:
            print("\n--- HOTEL MENU ---")
            print("1. Add booking")
            print("2. Cancel booking")
            print("3. Show report")
            print("4. Show room occupancy")
            print("5. Find available rooms")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_booking()
            elif choice == "2":
                self.cancel_booking()
            elif choice == "3":
                self.show_report()
            elif choice == "4":
                self.show_occupancy()
            elif choice == "5":
                self.show_available_rooms()
            elif choice == "6":
                print("Program closed.")
                break
            else:
                print("Invalid option.")


hotel = Hotel()
hotel.run()