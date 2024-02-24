**ADDRESS BOOK API**

This code comprises an API built using FastAPI framework for managing addresses in a database. It provides endpoints for CRUD operations (Create, Read, Update, Delete) on addresses, as well as a method to retrieve addresses within a specified distance from a given location.

![image](https://github.com/PujaShaw123/address-book/assets/47145081/e60b735b-12a6-4e7b-b43f-5d959385e23f)

**Setup**
Before running the API, ensure you have the necessary dependencies installed. You can typically install them via pip:

_pip install fastapi sqlalchemy_

**Database**
The code assumes the existence of a database and utilizes SQLAlchemy for ORM (Object-Relational Mapping). Ensure you have a compatible database set up and configure the connection details in the database.py module.

**Running the API**
To run the API, execute the main Python script:

_uvicorn main:app --reload_

This will start the API server locally. You can then access the endpoints described below.

**Endpoints**

**1. Create Address**
   Method: POST
   URL: /address
   Description: Adds a new address to the database.
   Request Body: JSON payload with address details.
   Response: JSON response with the added address details.

**2. Update Address**
   Method: PUT
   URL: /addresses/{address_id}
   Description: Updates an existing address by ID.
   Request Parameters:
   address_id: ID of the address to be updated.
   Request Body: JSON payload with updated address details.
   Response: JSON response with the updated address details.

**3. Delete Address**
   Method: DELETE
   URL: /address/{address_id}
   Description: Deletes an address by ID.
   Request Parameters:
   address_id: ID of the address to be deleted.
   Response: JSON response confirming successful deletion.

**4. Get Addresses Within Distance**
   Method: GET
   URL: /distance
   Description: Retrieves addresses within a specified distance from a given location.
   Query Parameters:
   lat: Latitude of the location.
   lon: Longitude of the location.
   max_distance: Maximum distance in kilometers.
   Response: JSON response containing a list of addresses within the specified distance.
