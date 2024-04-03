from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class Attendee(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z\s]*$", description="Name of the attendee")
    email: str
    age: int

class Event(BaseModel):
    name: str = Field(..., pattern=r"^[a-zA-Z\s]*$", description="Name of the event")
    date: str
    location: str

class TicketType(str, Enum):
    VIP = "VIP"
    Regular = "Regular"

class BookingRequest(BaseModel):
    attendee: Attendee
    event: Event
    ticket_type: TicketType = TicketType.Regular

class BookingConfirmation(BaseModel):
    attendee: Attendee
    event: Event
    ticket_type: TicketType
