
import pytz
import datetime


zones = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('US/Pacific'),
    pytz.timezone('Europe/Amsterdam'),
    pytz.timezone('Australia/Sydney'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('America/New_York')
    ]
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

def usr_input():
    while True:
        date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM format. ")
        try:
            local_date = datetime.datetime.strptime(date_input, '%m/%d/%Y %H:%M')
        except ValueError:
            print("{} doesn't seem to be a valid date & time.".format(date_input))
        else:
            local_date = pytz.timezone('US/Pacific').localize(local_date)
            utc_date = local_date.astimezone(pytz.utc)

            output = []
            for timezone in zones:
                output.append(utc_date.astimezone(timezone))
            for appointment in output:
                print(appointment.strftime(fmt))
            break
usr_input()