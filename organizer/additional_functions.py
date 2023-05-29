# called to make sure the age and level of a character are positive, and changes the value to none
# if it's an empty string
def validate_age_or_level(number):
    if number == '':
        return None
    if int(number) < 0:
        return str(int(number) * -1)
    else:
        return number
