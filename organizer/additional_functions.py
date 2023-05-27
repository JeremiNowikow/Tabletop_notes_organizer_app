def validate_age_or_level(number):
    if number == '':
        return None
    if int(number) < 0:
        return str(int(number) * -1)
    else:
        return number
