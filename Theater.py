# Define the Theater class to manage bookings
class Theater:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        # Initialize all seats as available ('O' for Open, 'X' for Booked)
        self.seats = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seats(self):
        print("\n--- Seat Availability ---")
        print("   " + " ".join(str(i + 1) for i in range(self.seats_per_row)))
        for idx, row in enumerate(self.seats):
            print(f"{idx + 1} | {' '.join(row)}")
        print()

    def book_seat(self, row, seat):
        if self.is_seat_available(row, seat):
            self.seats[row - 1][seat - 1] = 'X'
            print(f"Seat {row}-{seat} successfully booked!")
        else:
            print(f"Seat {row}-{seat} is already booked. Please choose another seat.")

    def is_seat_available(self, row, seat):
        return self.seats[row - 1][seat - 1] == 'O'

    def cancel_booking(self, row, seat):
        if not self.is_seat_available(row, seat):
            self.seats[row - 1][seat - 1] = 'O'
            print(f"Booking for seat {row}-{seat} has been canceled.")
        else:
            print(f"Seat {row}-{seat} is not currently booked.")

# Main function to interact with the Theater booking system
def main():
    # Initialize the theater with 5 rows and 10 seats per row
    theater = Theater(rows=5, seats_per_row=10)

    while True:
        print("\n--- Ticket Booking System ---")
        print("1. View Seats")
        print("2. Book a Seat")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            theater.display_seats()

        elif choice == '2':
            try:
                row = int(input("Enter row number: "))
                seat = int(input("Enter seat number: "))
                theater.book_seat(row, seat)
            except ValueError:
                print("Invalid input. Please enter a valid row and seat number.")

        elif choice == '3':
            try:
                row = int(input("Enter row number: "))
                seat = int(input("Enter seat number: "))
                theater.cancel_booking(row, seat)
            except ValueError:
                print("Invalid input. Please enter a valid row and seat number.")

        elif choice == '4':
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
