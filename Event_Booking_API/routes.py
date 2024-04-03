from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from models import BookingRequest, BookingConfirmation
from services import book_event

router = APIRouter(prefix="/booking", tags=["events"])

@router.post("/book_event", response_model=BookingConfirmation)
async def book_event_route(booking_request: BookingRequest):
    confirmation = book_event(booking_request)
    return JSONResponse(status_code=201, content={"data": confirmation, "message": "Event booking successful"})

# async def book_event_route(booking_request: BookingRequest):
#     try:
#         confirmation = book_event(booking_request)
#         return JSONResponse(status_code=201, content={"data": confirmation, "message": "Event booking successful"})
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
