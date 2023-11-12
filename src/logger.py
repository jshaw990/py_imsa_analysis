import os

from dotenv import load_dotenv

import utilities

# from src import utilities

load_dotenv()


class Log:
    """
    Data logger

    Available:
        - __init__
        - error
        - info
    """

    def __init__(self, is_debug=None, module_name="", show_timestamp=False):
        """
        Initialize the Log

        Args:
            is_debug (bool) : Is the application, or instantiating method in debug mode?
            module_name (str) : Module instantiating the log
            show_timestamp (bool) : Is the Log class to show the timestamp
        """
        if is_debug is None:
            is_debug = os.getenv("IS_DEBUG_MODE")

        self.is_debug = is_debug
        self.module_name = module_name
        self.show_timestamp = show_timestamp

    def error(self, message):
        """
        Error log

        Args:
            self (Log): Inititalized Log class
            message (str): Error message as string
        """
        module_tag = f"<{self.module_name}> -" if len(self.module_name) > 0 else ""
        print(f"[ERROR] - {module_tag} {message}. {utilities.get_unix()}")

    def info(self, message, show_timestamp=False):
        """
        Information log

        Args:
            self (Log): Inititalized Log class
            message (str): Info message as string
            show_timestamp (Bool): Show_Timestamp override
        """
        if self.is_debug == "True":
            module_tag = f"<{self.module_name}> -" if len(self.module_name) > 0 else ""
            timestamp = (
                f"[TIME] - {utilities.get_unix()}"
                if self.show_timestamp or show_timestamp
                else ""
            )

            print(f"[INFO] - {module_tag} {message} {timestamp}")
