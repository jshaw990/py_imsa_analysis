from datetime import datetime


def get_formatted_time():
    # Create a datetime object for Oct 25, 2023 @ 23:15:30
    desired_datetime = datetime(2023, 10, 25, 23, 15, 30)

    # Format the datetime object
    return desired_datetime.strftime("%b %d, %Y @ %H:%M:%S")
