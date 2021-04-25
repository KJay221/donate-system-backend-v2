from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProposalCreate(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str
    img_url: List[str]


class DBProposal(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    project_description: str
    start_time: datetime
    project_name: str
    representative: str
    email: str
    phone: str


class ProposalItem(BaseModel):
    proposal_addr: str
    owner_addr: str
    target_price: int
    current_price: int
    project_description: str
    start_time: datetime
    left_time: str
    project_name: str
    representative: str
    email: str
    phone: str
    img_url: List[str]
