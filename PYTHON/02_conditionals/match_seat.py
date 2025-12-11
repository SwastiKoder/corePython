seat_type = input("Enter seat type (sleeper/AC/general/luxury) : ").lower()

match seat_type:
    case "sleeper":
        print(f"You Booked Sleeper coach")
    case "ac":
        print(f"You Booked AC coach")
    case "general":
        print(f"You Booked General coach")
    case "luxury":
        print(f"You booked Luxury Seat")
    case _:
        print(f"Invalid Option")
