from pydantic import BaseModel, validator


# Pydantic model for creating an address
class AddressCreate(BaseModel):
    address: str
    latitude: float
    longitude: float

    @validator("address")
    def address_must_be_non_empty(cls, v):
        if not v:
            raise ValueError("Address must not be empty")
        return v


# Pydantic model for updating an address
class AddressUpdate(BaseModel):
    address: str
    latitude: float
    longitude: float

    @validator("address")
    def address_must_be_non_empty(cls, v):
        if not v:
            raise ValueError("Address must not be empty")
        return v
