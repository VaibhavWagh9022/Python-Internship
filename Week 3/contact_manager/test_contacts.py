import re

# ---------------- VALIDATION ----------------


def validate_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return digits if 10 <= len(digits) <= 15 else None


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
