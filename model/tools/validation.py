import re
from datetime import datetime, timedelta, date, time


def validation_name_family(*function):
    try :
        if re.match(r"^[a-zA-Z\s]{3,100}$", *function):
            return True
        else:
            return False , "!! invalid characters !!"

    except Exception as e:
        return None , f"Error : {e}"


def date_validation(str_date):
    try :
        str_date = str_date.replace('/','-').strip()
        return datetime.strptime(str_date, '%Y-%m-%d').date()

    except Exception as e:
        pass


def validation_general(*function):
    try :
        if re.match(r"^[a-zA-Z0-9*+_\-\s]{3,100}$", *function):
            return True
        else:
            return False , "!! invalid characters !!"

    except Exception as e:
        return None , f"Error : {e}"


def validation_account_number(function):
    try :
        if re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$", function):
            return True
        else:
            return False , "!! invalid account number !!"

    except Exception as e:
        return None , f"Error : {e}"


