from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional
from utils.session import get_db
from utils.models1 import FinancialImpact
from utils.models import BaseModel, FinancialImpactPut, FinancialImpactGet

app = FastAPI(
    title="Financial Impact API",
    description="API de análise de impacto financeiro de incidentes de cibersegurança",
    version="1.0.0"
)

# ========================================
# SCHEMAS PYDANTIC
# ========================================

# Schema para resposta (GET)
""" class FinancialImpactResponse(BaseModel):
    id: int
    incident_id: str
    direct_loss_usd: Optional[float]
    total_loss_usd: Optional[float]
    
    class Config:
        from_attributes = True """


# Schema para criar/atualizar (POST/PUT)
""" class FinancialImpactCreate(BaseModel):
    incident_id: str
    direct_loss_usd: Optional[float] = None
    direct_loss_method: Optional[str] = None
    ransom_demanded_usd: Optional[float] = None
    ransom_paid_usd: Optional[float] = None
    ransom_source: Optional[str] = None
    recovery_cost_usd: Optional[float] = None
    legal_fees_usd: Optional[float] = None
    regulatory_fine_usd: Optional[float] = None
    insurance_payout_usd: Optional[float] = None
    total_loss_usd: Optional[float] = None
    total_loss_method: Optional[str] = None
    total_loss_lower_bound: Optional[float] = None
    total_loss_upper_bound: Optional[float] = None
    inflation_adjusted_usd: Optional[float] = None
    cpi_index_used: Optional[str] = None
    notes: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
 """

# ========================================
# ENDPOINTS
# ========================================

@app.get("/")
def root():
    """Página inicial"""
    return {
        "message": "Financial Impact API",
        "docs": "/docs",
        "endpoints": {
            "list_all": "GET /financial/",
            "get_by_id": "GET /financial/{incident_id}",
            "create": "POST /financial/",
            "update": "PUT /financial/{incident_id}",
            "delete": "DELETE /financial/{incident_id}",
            "top_losses": "GET /financial/loss/top"
        }
    }


@app.get("/financial/", response_model=List[FinancialImpactGet])
def listar_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todos os impactos financeiros (com paginação)"""
    return db.query(FinancialImpact).offset(skip).limit(limit).all()


@app.get("/financial/{incident_id}", response_model=FinancialImpactGet)
def buscar_por_id(incident_id: str, db: Session = Depends(get_db)):
    """Buscar impacto financeiro por incident_id"""
    result = db.query(FinancialImpact).filter(
        FinancialImpact.incident_id == incident_id
    ).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    return result


@app.post("/financial/", response_model=FinancialImpactPut, status_code=201)
def criar_incidente(
    incidente: FinancialImpactPut, 
    db: Session = Depends(get_db)
):
    """Criar novo incidente de impacto financeiro"""
    
    # Verificar se incident_id já existe
    existe = db.query(FinancialImpact).filter(
        FinancialImpact.incident_id == incidente.incident_id
    ).first()
    
    if existe:
        raise HTTPException(
            status_code=400, 
            detail=f"Incident ID '{incidente.incident_id}' já existe!"
        )
    
    # Criar novo registro
    novo_incidente = FinancialImpact(**incidente.dict())
    
    db.add(novo_incidente)
    db.commit()
    db.refresh(novo_incidente)
    
    return novo_incidente


@app.put("/financial/{incident_id}", response_model=FinancialImpactPut)
def atualizar_incidente(
    incident_id: str,
    incidente: FinancialImpactPut,
    db: Session = Depends(get_db)
):
    """Atualizar incidente existente"""
    
    # Buscar incidente
    incidente_existente = db.query(FinancialImpact).filter(
        FinancialImpact.incident_id == incident_id
    ).first()
    
    if not incidente_existente:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    # Atualizar campos
    for campo, valor in incidente.dict(exclude_unset=True).items():
        setattr(incidente_existente, campo, valor)
    
    db.commit()
    db.refresh(incidente_existente)
    
    return incidente_existente


@app.get("/financial/loss/top")
def maiores_perdas(limit: int = 10, db: Session = Depends(get_db)):
    """Top N incidentes com maiores perdas"""
    return db.query(FinancialImpact)\
        .order_by(desc(FinancialImpact.total_loss_usd))\
        .limit(limit)\
        .all()


@app.delete("/financial/{incident_id}")
def deletar(incident_id: str, db: Session = Depends(get_db)):
    """Deletar registro"""
    impact = db.query(FinancialImpact).filter(
        FinancialImpact.incident_id == incident_id
    ).first()
    
    if not impact:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    db.delete(impact)
    db.commit()
    return {"message": f"Incident {incident_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)