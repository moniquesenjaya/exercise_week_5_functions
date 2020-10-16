def convert_to_days():
    hours = eval(input("Enter number of hours: "))
    mins = eval(input("Enter number of minutes: "))
    secs = eval(input("Enter number of seconds: "))
    days = get_days(hours, mins, secs)
    print("\nThe number of days is: ", days)

def get_days(hours, mins, secs):
    total_seconds = hours*60*60 + mins*60 + secs
    days = round((total_seconds/86400), 4)
    return days

convert_to_days()