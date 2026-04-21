from sqlalchemy import Column, Integer, Numeric, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FinancialImpact(Base):
    __tablename__ = 'financial_impact'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    incident_id = Column(String(50), nullable=False, unique=True, index=True)
    direct_loss_usd = Column(Numeric(12,2))
    direct_loss_method = Column(String(100))
    ransom_demanded_usd = Column(Numeric(12,2))
    ransom_paid_usd = Column(Numeric(12,2))
    ransom_source = Column(String(100))
    recovery_cost_usd = Column(Numeric(12,2))
    legal_fees_usd = Column(Numeric(12,2))
    regulatory_fine_usd = Column(Numeric(12,2))
    insurance_payout_usd = Column(Numeric(12,2))
    total_loss_usd = Column(Numeric(12,2))
    total_loss_method = Column(String(100))
    total_loss_lower_bound = Column(Numeric(12,2))
    total_loss_upper_bound = Column(Numeric(12,2))
    inflation_adjusted_usd = Column(Numeric(12,2))
    cpi_index_used = Column(String(100))
    notes = Column(String(500))
    incident_date = Column(Date)