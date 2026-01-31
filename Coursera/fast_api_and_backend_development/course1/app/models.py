from pydantic import BaseModel, Field
from app.database.models import ShipmentStatus

class BaseShipment(BaseModel):
    content: str = Field(description="Contents of the shipment.", max_length=30, min_length=3)
    weight: float = Field(description="weight of the shipment.", ge=0.01, le=25)
    destination: int = Field(description="Zipcode of the destination.", default=110010)
    

class ShipmentRead(BaseShipment):
    status: ShipmentStatus = Field(description="status", default=ShipmentStatus.placed)


class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    status: ShipmentStatus = Field(description="status of the shipment", default=ShipmentStatus.placed)
