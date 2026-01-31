from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel

class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"

class Shipment(SQLModel, table=True):
    # table_name is set to lower case class_name
    id: int = Field(primary_key=True)
    content: str
    weight: float = Field(le=25, ge=0.01)
    destination: int
    status: ShipmentStatus
    # estimated_delivery: datetime