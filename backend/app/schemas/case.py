from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CaseCreate(BaseModel):
    title: str
    description: str


class CaseRead(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime

    class Config:
        orm_mode = True
