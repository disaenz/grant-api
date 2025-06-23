from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from database import Base

class Calendar(Base):
    __tablename__ = "calendars"
    __table_args__ = {'schema': 'grantmaking_schema'}

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False)

    # One calendar can have multiple grants
    grants = relationship("Grant", back_populates="calendar")
