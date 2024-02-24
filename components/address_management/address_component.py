from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .models import Address
from .database import init_db, get_db
from utils.geocode_utils import calculate_distance
from validators.address_validator import AddressCreate, AddressUpdate

router = APIRouter()

init_db()


@router.post("/address")
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    """
    To add a new address to the database.
    """
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


@router.put("/addresses/{address_id}")
def update_address(
    address_id: int, address_data: AddressUpdate, db: Session = Depends(get_db)
):
    """
    Update an address by ID.

    This endpoint updates the address with the specified ID using the provided address data.

    :param address_id: The ID of the address to be updated.
    :param address_data: The updated address data.
    :param db: Database session dependency.
    :return: Updated address.
    """
    address = get_address(address_id, db)
    if address is None:
        raise HTTPException(status_code=404, detail="Address not found")

    updated_address = update_address(address, address_data, db)
    return updated_address


def get_address(address_id: int, db: Session = Depends(get_db)):
    return db.query(Address).filter(Address.id == address_id).first()


def update_address(
    address: Address, address_data: AddressUpdate, db: Session = Depends(get_db)
):
    for key, value in address_data.dict().items():
        setattr(address, key, value)
    db.commit()
    return address


@router.delete("/address/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    """
    To remove the address for particular id from the database.
    :param address_id: The unique identifier of the address to be deleted.
    :return: A success message if deleted. Otherwise a failure message is returned.
    """
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    return {"message": "Address deleted successfully"}


@router.get("/distance")
def get_addresses_within_distance(
    lat: float = Query(..., description="Latitude of the location"),
    lon: float = Query(..., description="Longitude of the location"),
    max_distance: float = Query(..., description="Maximum distance in kilometers"),
    db: Session = Depends(get_db),
):
    """
    To retrieve the addresses that are within
    a given distance and location coordinates.
    :param lat: Latitude of the location.
    :param lon: Longitude of the location.
    :param max_distance: Maximum distance in kilometers.
    :param db: Database session dependency.
    :return: List of addresses within the specified distance.
    """
    addresses_within_distance = []

    # Query addresses from the database
    addresses = db.query(Address).all()

    # Iterate over addresses and calculate distance for each
    for address in addresses:
        distance = calculate_distance(lat, lon, address.latitude, address.longitude)
        if distance <= max_distance:
            addresses_within_distance.append(address)

    return addresses_within_distance
