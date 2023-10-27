from datetime import datetime


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
