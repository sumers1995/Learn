from fastapi import Depends, FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from typing import Any

from sqlmodel import Session
from app.models import ShipmentCreate, ShipmentRead, ShipmentUpdate
from app.repo import Database
from contextlib import asynccontextmanager
from app.database.async_session import create_db_tables, get_session

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    print("Server started...")
    await create_db_tables()
    yield
    print("...stopped!")

app = FastAPI(lifespan=lifespan_handler)
db = Database()

@app.get("/")
def root():
    return {"message": "Welcome to Shipment Management."}

@app.post("/shipment", response_model=None)
def create_shipment(shipment: ShipmentCreate) -> dict[str, Any] | None:
    new_id = db.create(shipment=shipment)
    return db.get(id=new_id)

@app.get("/shipment/", response_model=ShipmentRead)
async def get_shipment(id: int, session: Session = Depends(get_session)):
    shipment = await session.get(id=id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn't exist!",
        )
    return shipment

@app.get("/shipment/all/")
def get_all_shipments():
    return db.get_all()

# @app.put("/shipment")
# def update_shipment(id: int, ) -> dict[str, Any]:
#     shipments[id]= {"content": content, "weight": weight, "status": status}
#     return shipments[id]

@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, shipment: ShipmentUpdate):
    return db.update(id=id, shipment=shipment)

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    db.delete(id=id)
    return {"detail": f"Shipment with id #{id} is deleted."}

# for scalar docs
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():

    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )