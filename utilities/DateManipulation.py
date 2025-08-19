from datetime import datetime


def lao_date_to_iso(lao_date):
    # return lao_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return datetime.strptime(str(lao_date), "%d-%m-%Y").date()


def iso_to_lao_date(iso_date):
    formatted_date = datetime.strptime(str(iso_date), "%Y-%m-%d").strftime("%d-%m-%Y")

    return formatted_date
