from fastapi import FastAPI
from controllers.appointment_controller import router as appointment_router

app = FastAPI()

# Include routers
app.include_router(appointment_router)

# Run with uvicorn (explained below)
