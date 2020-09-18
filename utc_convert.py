import datetime
import pytz

def convert_to_UTC(datestring):
    split_text = datestring.split(sep = '-')
    first_half = split_text[0].strip()
    first_half_UTC = first_half+'+0000'
    date_UTC = datetime.datetime.strptime(first_half_UTC, "%d.%m.%Y %H:%M%z")
    london_tz = pytz.timezone('Europe/London')
    date_UK_time = date_UTC.astimezone(london_tz)
    
    return date_UK_time