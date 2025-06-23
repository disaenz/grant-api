from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Grant(Base):
    __tablename__ = "grants"
    __table_args__ = {'schema': 'grantmaking_schema'}

    id = Column(Integer, primary_key=True, index=True)
    calendar_id = Column(Integer, ForeignKey("grantmaking_schema.calendars.id"), nullable=False)
    grant_making_process = Column(String(255), nullable=False)
    program = Column(String(255))
    competitive = Column(String(255))
    types_of_application = Column(String(255))
    internal_or_external_review = Column(String(255))
    egrants_or_new_system = Column(String(255))
    expected_applicants = Column(String(255))
    deadline_for_kickoff = Column(Date)
    system_prep_date = Column(Date)
    outreach_start_date = Column(Date)
    recommendation_plan_date = Column(String(50))
    publish_development = Column(String(255))
    application_due_date = Column(Date)
    review_period = Column(String(255))
    applicant_clarification = Column(String(255))
    oro_clarification = Column(String(255))
    program_prep_for_decision = Column(String(255))
    award_decision = Column(String(255))
    applicant_notification = Column(String(255))
    finish_terms = Column(Date)
    oro_award_processing = Column(String(255))
    budget_office_fund_commitment = Column(String(255))
    oga_award_processing = Column(String(255))
    award_target = Column(String(255))
    notes = Column(Text)

    # Establish relationship with Calendar
    calendar = relationship("Calendar", back_populates="grants")
