from datetime import datetime

def access_granted(date=""):
    birth_date = datetime.strptime(date, "%Y-%m-%d").date()
    todays_date = datetime.strptime("2025-04-11", "%Y-%m-%d").date()
    delta = todays_date - birth_date
    if delta.days >= 5844:
        return "Access granted!"
    return "Access denied!"