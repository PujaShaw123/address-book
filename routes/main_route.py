from fastapi import APIRouter
from components.address_management.address_component import router as address_router

router = APIRouter()

router.include_router(address_router, prefix="", tags=["address"])
