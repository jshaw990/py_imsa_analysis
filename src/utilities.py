import os
import json
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

"""
Utility methods:
    - check_for_current_date @see
    - read_data_from_file
    - write_data_to_file
    - iterate_date_string
    - get_unix
"""


def get_utc_datetime_string():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def check_for_current_date(date_string):
    """
    Check if provided date_string is today (True),

    Returns:
        bool : if True - date is today, if False - date is in the past, if None - Date is in the future or invalid

    Raises:
        ValueError: Date is in the future
        Exception: Date is invalid
    """
    current_date = datetime.now().strftime("%Y-%m-%d")

    if date_string == current_date:
        return True
    elif date_string < current_date:
        return False
    elif date_string > current_date:
        raise ValueError(f"Date cannot be in the future.")
    else:
        raise Exception(f"Date is not valid. Date provided: {date_string}")


def iterate_date_string(start_date, num):
    """
    Convert the provided date string into a date object,
    SUBTRACT the provided number of days,
    and return the resultiing date object in a string.

    Args:
        start_date(str) : start date in the format of '2023-09-20'
        num(int) : number of days to subtract from the start_date

    Returns:
        str : date which is num days different than the start_date
    """
    date_obj = (
        datetime.strptime(start_date, "%Y-%m-%d") - datetime.timedelta(days=num)
    ).date()

    return date_obj.strftime("%Y-%m-%d")


def read_data_from_file(file_name="data.txt"):
    """
    Read data from the file_name provided and return it in a dictionary

    Args:
        file_name(str) : file name to be returned

    Returns:
        dict: file's data in a dictionary
    """
    file = open(f"../data/{file_name}", "r")
    return json.loads(file.read())


def write_data_to_file(data, file_name="data.txt"):
    """
    Write provided data to a text file

    Args:
        data(str) : data to be written to the file
        file_name(str) : file name for the created file (default = 'data.txt')
    """
    file = open(f"./data/{file_name}", "w")
    file.write(data)
    file.close()


def get_unix():
    """
    Get the current Unix Time

    Returns:
        str: Unix Timestamp in seconds as a string
    """
    time_stamp = round(datetime.timestamp(datetime.now()))

    return str(time_stamp)


def check_dev_mode():
    return os.getenv("IS_DEBUG_MODE").lower().strip() == "true"


def get_formatted_time():
    """Create a datetime object for the current time

    Returns:
        (str) datetime object like: 'Oct 25, 2023 @ 23:15:30'
    """
    # Create a datetime object for Oct 25, 2023 @ 23:15:30
    return datetime.now().strftime("%b %d, %Y @ %H:%M:%S")


def lap_time_to_seconds(lap_time_str):
    """Get a float for 'Lap Time' column from dataframe

    Args:
        lap_time_str (str) - Lap Time string as MM:SS.ms

    Returns:
        (float) Lap Time converted to a float
    """
    if isinstance(lap_time_str, float):
        return lap_time_str

    components = lap_time_str.split(":")
    minutes = 0
    seconds = 0
    milliseconds = 0

    if len(components) >= 1:
        minutes = float(components[0])
    if len(components) >= 2:
        seconds = float(components[1])
    if len(components) >= 3:
        milliseconds = float(components[2])

    return minutes * 60 + seconds + milliseconds / 1000
