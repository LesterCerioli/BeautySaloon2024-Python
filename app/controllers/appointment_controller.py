from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime
from uuid import UUID
from services.appointment_service import AppointmentService
from models.appointment import Appointment  # Ensure this is correctly imported

router = APIRouter()

# Create appointment
@router.post("/appointments", response_model=Appointment)
async def create_appointment(
    date: datetime, 
    appointment_hour: datetime, 
    customer_name: str, 
    attendant_names: Optional[List[str]] = None
):
    # The service method should return an Appointment instance
    appointment = AppointmentService.create_appointment(date, appointment_hour, customer_name, attendant_names)
    return appointment

# Get appointments by date
@router.get("/appointments/by_date", response_model=List[Appointment])
async def get_appointments_by_date(date: datetime):
    # Fetch appointments based on date from the service
    appointments = AppointmentService.get_appointments_by_date(date)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for the specified date")
    return appointments

# Get appointments by hour
@router.get("/appointments/by_hour", response_model=List[Appointment])
async def get_appointments_by_hour(appointment_hour: datetime):
    # Fetch appointments based on appointment hour from the service
    appointments = AppointmentService.get_appointments_by_hour(appointment_hour)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for the specified hour")
    return appointments

# Get appointments by attendant name
@router.get("/appointments/by_attendant", response_model=List[Appointment])
async def get_appointments_by_attendant(attendant_name: str):
    # Fetch appointments based on attendant name from the service
    appointments = AppointmentService.get_appointments_by_attendant(attendant_name)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for the specified attendant")
    return appointments

# Get appointments by customer name
@router.get("/appointments/by_customer", response_model=List[Appointment])
async def get_appointments_by_customer(customer_name: str):
    # Fetch appointments based on customer name from the service
    appointments = AppointmentService.get_appointments_by_customer(customer_name)
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found for the specified customer")
    return appointments

# Get appointment by UUID (for future use if needed)
@router.get("/appointments/{appointment_id}", response_model=Appointment)
async def get_appointment_by_id(appointment_id: UUID):
    # Fetch appointment by UUID from the service
    appointment = AppointmentService.get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
