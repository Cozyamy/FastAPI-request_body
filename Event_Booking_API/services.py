import json
from datetime import datetime
from models import BookingRequest, BookingConfirmation
from models import TicketType, Event, Attendee

def read_database():
    with open("database.json", "r") as file:
        return json.load(file)

def write_database(data):
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)

def validate_booking_request(booking_request: BookingRequest):
    if booking_request.attendee.age < 18:
        raise ValueError("Attendee must be at least 18 years old to book.")
    
    event_date = datetime.strptime(booking_request.event.date, '%Y-%m-%d')
    if event_date <= datetime.now():
        raise ValueError("Event date must be in the future.")
    pass

def book_event(booking_request: BookingRequest) -> dict: 
    validate_booking_request(booking_request)

    database = read_database()

    booking_data = {
        "attendee": booking_request.attendee.model_dump(),
        "event": booking_request.event.model_dump(),
        "ticket_type": booking_request.ticket_type
    }
    database.append(booking_data)

    write_database(database)

    return booking_data