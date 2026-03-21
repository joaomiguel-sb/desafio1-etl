from pydantic import BaseModel
from typing import Optional


class FinancialImpactPut(BaseModel):

    
    incident_id: str
    direct_loss_usd: float
    direct_loss_method: str
    ransom_demanded_usd: float
    ransom_paid_usd: float
    ransom_source: str
    recovery_cost_usd: float
    legal_fees_usd: float
    regulatory_fine_usd: float
    insurance_payout_usd: float
    total_loss_usd: float
    total_loss_method: str
    total_loss_lower_bound: float
    total_loss_upper_bound: float
    inflation_adjusted_usd: float
    cpi_index_used: str
    notes: str
    created_at: str
    updated_at: str

class FinancialImpactGet(BaseModel):
    id: int
    incident_id: str
    direct_loss_usd: Optional[float]
    direct_loss_method: Optional[str]
    ransom_demanded_usd: Optional[float]
    ransom_paid_usd: Optional[float]
    ransom_source: Optional[str]
    recovery_cost_usd: Optional[float]
    legal_fees_usd: Optional[float]
    regulatory_fine_usd: Optional[float]
    insurance_payout_usd: Optional[float]
    total_loss_usd: Optional[float]
    total_loss_method: Optional[str]
    total_loss_lower_bound: Optional[float]
    total_loss_upper_bound: Optional[float]
    inflation_adjusted_usd: Optional[float]
    cpi_index_used: Optional[str]
    notes: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    
    class Config:
        from_attributes = True