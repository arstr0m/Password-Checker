import re


def check_password(password):
    score = 0

    if len(password) >= 14:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        return "Password too short, must be at least 8 characters."

    if re.search(r'[A-Z]', password):
        score += 1

    # Lowercase letter
    if re.search(r'[a-z]', password):
        score += 1

    # Digit
    if re.search(r'[0-9]', password):
        score += 1

    # Special character
    if re.search(r'[@$!%*?&]', password):
        score += 1

    if score >= 8:
        return "Password is very strong."
    elif score >= 4:
        return "Password is strong."
    elif score >= 3:
        return "Password is moderate."
    else:
        return "Password is weak."
