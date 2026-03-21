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
# ENDPOINTS
# ========================================


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