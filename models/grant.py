from sqlalchemy import Column, Integer, String, Date, DateTime, Text, func
from database import Base

class Grant(Base):
    __tablename__ = "grants"
    __table_args__ = {"schema": "grant_schema"}

    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String(255), nullable=False)
    program       = Column(String(255), nullable=False)
    grant_type    = Column("type", String(100), nullable=False)
    status        = Column(String(50), nullable=False)
    start_date    = Column(Date, nullable=False)
    deadline      = Column(Date, nullable=False)
    budget_range  = Column(String(50), nullable=False)
    created_at    = Column(
                     DateTime(timezone=True),
                     nullable=False,
                     server_default=func.now()
                   )
    updated_at    = Column(
                     DateTime(timezone=True),
                     nullable=False,
                     server_default=func.now(),
                     onupdate=func.now()
                   )
    notes         = Column(Text)