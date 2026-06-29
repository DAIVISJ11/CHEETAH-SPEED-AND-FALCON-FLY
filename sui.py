class Seat:
    def __init__(self, seat_id, free=True, seat_type="aisle"):
        self.seat_id = seat_id
        self.free = free
        self.seat_type = seat_type

    def __repr__(self):
        status = "Free" if self.free else "Taken"
        return f"{self.seat_id} ({self.seat_type}, {status})"


class TrainCoach:
    def __init__(self):
        self.seats = []
        self.create_default_layout()

    def create_default_layout(self):
        # Example layout: 4 rows × 4 seats
        layout = [
            ("1A", "window"), ("1B", "aisle"), ("1C", "aisle"), ("1D", "window"),
            ("2A", "window"), ("2B", "aisle"), ("2C", "aisle"), ("2D", "window"),
            ("3A", "window"), ("3B", "aisle"), ("3C", "aisle"), ("3D", "window"),
            ("4A", "window"), ("4B", "aisle"), ("4C", "aisle"), ("4D", "window"),
        ]

        # Mark some seats as taken
        taken = {"1B", "2C", "3A", "4B"}

        for seat_id, seat_type in layout:
            free = seat_id not in taken
            self.seats.append(Seat(seat_id, free, seat_type))

    def find_free_seat(self, preferred_type=None):
        free_seats = [s for s in self.seats if s.free]

        if preferred_type:
            free_seats = [s for s in free_seats if s.seat_type == preferred_type]

        if not free_seats:
            return None

        return free_seats[0]  # return first available seat

    def show_all_seats(self):
        for seat in self.seats:
            print(seat)


# -------------------------
# Main Program
# -------------------------

coach = TrainCoach()

print("All seats:")
coach.show_all_seats()

print("\nFinding any free seat...")
seat = coach.find_free_seat()
print("Suggested seat:", seat)

print("\nFinding a free window seat...")
window_seat = coach.find_free_seat(preferred_type="window")
print("Suggested window seat:", window_seat)
