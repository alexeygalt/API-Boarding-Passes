from typing import Optional, Literal
from pydantic import BaseModel


class BoardingPass(BaseModel):
    """Custom Model of boarding data"""

    transport_type: Literal["train", "bus", "fly"]
    departure_point: str
    arrival_point: str
    number: Optional[str] = None
    seat_place: Optional[str] = None
    gate: Optional[str] = None
    baggage: Optional[int] = None


class BaseInputData(BaseModel):
    """Model and validate of expected input data"""

    # departure_point: str
    # arrival_point: str
    boarding_passes: list[BoardingPass]

    # @property
    # def check_points(self):
    #     if self.departure_point not in [
    #         item.departure_point for item in self.boarding_passes
    #     ] or self.arrival_point not in [
    #         item.arrival_point for item in self.boarding_passes
    #     ]:
    #         return False
    #     return True
