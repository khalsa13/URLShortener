from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_Url(value):
    url_validator=URLValidator()
    val_1=True
    val_2=True

    try:
        url_validator(value)
    except:
        val_1=False

    val_Changed="http://"+value

    try:
        url_validator(val_Changed)
    except:
        val_2=False

    if val_2==False and val_1==False:
        raise ValidationError("Invalid Url")
    return value


def validate_dot_com(value):
    if not( ('com' in value) or ('co.in' in value) or('.in' in value)):
        raise ValidationError("Their is no .com/.co.in in the Url")
    return value