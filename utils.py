
def format_date(date_value):
    """Format a date as MM/DD/YYYY if not None."""
    if date_value is not None:
        return date_value.strftime('%m/%d/%Y')
    return None

def format_date_time(date_value):
    """Format a date as MM/DD/YYYY HH:MM:SS if not None."""
    if date_value is not None:
        return date_value.strftime('%m/%d/%Y %H:%M:%S')
    return None