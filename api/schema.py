from pydantic import BaseModel
from typing import List

class Record(BaseModel):
    date: str
    sku: str
    demand_diff: float
    demand_zscore: float
    inventory_diff: float
    lead_time_diff: float
    inventory_rolling_mean: float
    lead_time_diff: float
    lead_time_rolling_mean: float


class AnomalyRequest(BaseModel):
    records: List[Record]