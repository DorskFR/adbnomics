from pydantic import BaseModel
from typing import Optional, Any


class CleanedData(BaseModel):
    provider: Optional[str]
    dataset_code: Optional[str]
    dataset_name: Optional[str]
    series_code: Optional[str]
    frequency: Optional[str]
    df: Any  # pandas.DataFrame
