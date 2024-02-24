from fastapi import FastAPI
from . import address_component, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(address_component.router)
