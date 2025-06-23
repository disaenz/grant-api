
def format_date(date_value):
    """Format a date as MM/DD/YYYY if not None."""
    if date_value is not None:
        return date_value.strftime('%m/%d/%Y')
    return None