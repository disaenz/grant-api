
from utils import format_date

def map_grant_response(grant):
    return {
        "id": grant.id,
        "calendarId": grant.calendar_id,  # if you want to expose this; otherwise, omit it.
        "grantMakingProcess": grant.grant_making_process,
        "program": grant.program,
        "competitive": grant.competitive,
        "typesOfApplication": grant.types_of_application,
        "internalOrExternalReview": grant.internal_or_external_review,
        "eGrantsOrNewSystem": grant.egrants_or_new_system,
        "expectedApplicants": grant.expected_applicants,
        "deadlineForKickOff": format_date(grant.deadline_for_kickoff),
        "systemPrepDate": format_date(grant.system_prep_date),
        "outreachStartDate": format_date(grant.outreach_start_date),
        "recommendationPlanDate": grant.recommendation_plan_date,
        "publishDevelopment": grant.publish_development,
        "applicationDueDate": format_date(grant.application_due_date),
        "reviewPeriod": grant.review_period,
        "applicantClarification": grant.applicant_clarification,
        "oroClarification": grant.oro_clarification,
        "programPrepForDecision": grant.program_prep_for_decision,
        "awardDecision": grant.award_decision,
        "applicantNotification": grant.applicant_notification,
        "finishTerms": format_date(grant.finish_terms),
        "oroAwardProcessing": grant.oro_award_processing,
        "budgetOfficeFundCommitment": grant.budget_office_fund_commitment,
        "ogaAwardProcessing": grant.oga_award_processing,
        "awardTarget": grant.award_target,
        "notes": grant.notes,
    }

def map_grants_response(grants):
    return [map_grant_response(grant) for grant in grants]
