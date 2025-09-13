from datetime import date ,time, datetime, timedelta


def date_validation(str_date):
    try:
        str_date = str_date.replace("/","-").strip()
        return datetime.strptime(str_date, "%Y-%m-%d").date()
    except Exception as e:
        return f"Error: {e}"

